from dotenv import load_dotenv
import os
load_dotenv()

print("GROQ_API_KEY =", os.getenv("GROQ_API_KEY"))

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import SessionLocal
import models
from pydantic import BaseModel, validator
from typing import Optional, List
from datetime import date
import ast
import requests

router = APIRouter(prefix="/suppliers", tags=["Suppliers"])

GROQ_API_KEY = os.getenv("GROQ_API_KEY")
if not GROQ_API_KEY:
    raise Exception("GROQ_API_KEY not found in environment variables")

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Pydantic schemas

class ComplianceRecordResponse(BaseModel):
    id: int
    metric: str
    date_recorded: date
    result: str
    status: str

    class Config:
        from_attributes = True  # ✅ Updated for Pydantic v2

class SupplierCreate(BaseModel):
    name: str
    country: str
    contract_terms: dict
    compliance_score: Optional[int] = None
    last_audit: Optional[date] = None

class SupplierResponse(BaseModel):
    id: int
    name: str
    country: str
    contract_terms: dict
    compliance_score: Optional[int]
    last_audit: Optional[date]
    compliance_records: List[ComplianceRecordResponse] = []

    @validator('contract_terms', pre=True)
    def parse_contract_terms(cls, v):
        if isinstance(v, str):
            try:
                return ast.literal_eval(v)
            except Exception:
                return {}
        return v

    class Config:
        from_attributes = True  # ✅ Fixed here as well

class ComplianceRecordCreate(BaseModel):
    supplier_id: int
    metric: str
    date_recorded: date
    result: str
    status: str

@router.post("/", response_model=SupplierResponse)
def add_supplier(supplier: SupplierCreate, db: Session = Depends(get_db)):
    new_supplier = models.Supplier(**supplier.dict())
    db.add(new_supplier)
    db.commit()
    db.refresh(new_supplier)
    return new_supplier

@router.get("/", response_model=List[SupplierResponse])
def get_suppliers(db: Session = Depends(get_db)):
    try:
        suppliers = db.query(models.Supplier).all()
        return suppliers
    except Exception as e:
        raise HTTPException(status_code=500, detail="Failed to fetch suppliers")

@router.get("/insights")
def get_compliance_insights(db: Session = Depends(get_db)):
    try:
        compliance_records = db.query(models.ComplianceRecord).all()
        compliance_data = ""
        for rec in compliance_records:
            compliance_data += f"Supplier ID {rec.supplier_id} had metric {rec.metric} on {rec.date_recorded} with status {rec.status}. "

        if not compliance_data:
            return {"message": "No compliance data available to analyze."}

        url = "https://api.groq.com/openai/v1/chat/completions"
        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {GROQ_API_KEY}"
        }
        payload = {
            "model": "meta-llama/llama-4-scout-17b-16e-instruct",
            "messages": [
                {
                    "role": "user",
                    "content": (
                        "Analyze the following supplier compliance data and provide actionable suggestions "
                        "to improve supplier performance and contract terms:\n\n" + compliance_data
                    )
                }
            ]
        }

        response = requests.post(url, json=payload, headers=headers)
        response.raise_for_status()
        data = response.json()
        ai_message = data["choices"][0]["message"]["content"]

        return {"insights": ai_message}

    except requests.HTTPError as e:
        raise HTTPException(status_code=500, detail=f"LLM API request failed: {str(e)}")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to get AI insights: {str(e)}")

@router.get("/{supplier_id}", response_model=SupplierResponse)
def get_supplier_by_id(supplier_id: int, db: Session = Depends(get_db)):
    supplier = db.query(models.Supplier).filter(models.Supplier.id == supplier_id).first()
    if not supplier:
        raise HTTPException(status_code=404, detail="Supplier not found")
    return supplier

@router.post("/check-compliance")
def check_compliance(record: ComplianceRecordCreate, db: Session = Depends(get_db)):
    try:
        new_record = models.ComplianceRecord(**record.dict())
        db.add(new_record)
        db.commit()
        db.refresh(new_record)
    except Exception as e:
        raise HTTPException(status_code=500, detail="Something went wrong")

    pattern = "Late deliveries detected" if record.metric.lower() == "delivery time" and record.status.lower() == "non-compliant" else "No major issues"

    return {
        "message": "Compliance data recorded.",
        "pattern_analysis": pattern
    }
