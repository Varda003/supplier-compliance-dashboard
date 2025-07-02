from sqlalchemy import Column, Integer, String, Date, ForeignKey, JSON
from sqlalchemy.orm import relationship
from database import Base

class Supplier(Base):
    __tablename__ = "suppliers"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String, nullable=False)
    country = Column(String, nullable=False)
    contract_terms = Column(JSON)
    compliance_score = Column(Integer)
    last_audit = Column(Date)

    compliance_records = relationship("ComplianceRecord", back_populates="supplier")


class ComplianceRecord(Base):
    __tablename__ = "compliance_records"

    id = Column(Integer, primary_key=True, index=True)
    supplier_id = Column(Integer, ForeignKey("suppliers.id"))
    metric = Column(String)
    date_recorded = Column(Date)
    result = Column(String)
    status = Column(String)

    supplier = relationship("Supplier", back_populates="compliance_records")
