import pandas as pd
from database import SessionLocal, engine
import models
from sqlalchemy.exc import IntegrityError

# Make sure tables exist
models.Base.metadata.create_all(bind=engine)

def import_suppliers():
    df = pd.read_excel("Task_Supplier_Data.xlsx")
    db = SessionLocal()
    try:
        for _, row in df.iterrows():
            supplier = models.Supplier(
                id = row['supplier_id'],
                name = row['name'],
                country = row['country'],
                compliance_score = row.get('compliance_score'),
                contract_terms = row.get('contract_terms') if 'contract_terms' in row else None,
                last_audit = row.get('last_audit')
            )
            # To avoid duplicates, you can try merge or check if id exists
            try:
                db.merge(supplier)
                db.commit()
            except IntegrityError:
                db.rollback()
        print("Suppliers imported successfully")
    finally:
        db.close()

def import_compliance_records():
    df = pd.read_excel("Task_Compliance_Records.xlsx")
    db = SessionLocal()
    try:
        for _, row in df.iterrows():
            record = models.ComplianceRecord(
                id = row['compliance_record_id'],
                supplier_id = row['supplier_id'],
                metric = row['metric'],
                date_recorded = row['date_recorded'],
                result = row['result'],
                status = row['status']
            )
            try:
                db.merge(record)
                db.commit()
            except IntegrityError:
                db.rollback()
        print("Compliance records imported successfully")
    finally:
        db.close()

if __name__ == "__main__":
    import_suppliers()
    import_compliance_records()
