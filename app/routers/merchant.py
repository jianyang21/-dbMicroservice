from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from .. import models
from ..database import get_db

router = APIRouter(prefix="/merchants", tags=["Merchants"])

@router.get("/")
def get_merchants(db: Session = Depends(get_db)):
    merchants = db.query(models.Merchant).all()
    return merchants

@router.get("/{merchant_id}")
def get_merchant(merchant_id: str, db: Session = Depends(get_db)):
    merchant = db.query(models.Merchant).filter(models.Merchant.id == merchant_id).first()
    if not merchant:
        raise HTTPException(status_code=404, detail="Merchant not found")
    return merchant

@router.post("/")
def create_merchant(merchant: dict, db: Session = Depends(get_db)):
    new_merchant = models.Merchant(**merchant)
    db.add(new_merchant)
    db.commit()
    db.refresh(new_merchant)
    return {"message": "Merchant created successfully", "data": new_merchant}

@router.put("/{merchant_id}")
def update_merchant(merchant_id: str, merchant: dict, db: Session = Depends(get_db)):
    existing = db.query(models.Merchant).filter(models.Merchant.id == merchant_id).first()
    if not existing:
        raise HTTPException(status_code=404, detail="Merchant not found")
    for key, value in merchant.items():
        setattr(existing, key, value)
    db.commit()
    db.refresh(existing)
    return {"message": "Merchant updated successfully", "data": existing}

@router.delete("/{merchant_id}")
def delete_merchant(merchant_id: str, db: Session = Depends(get_db)):
    merchant = db.query(models.Merchant).filter(models.Merchant.id == merchant_id).first()
    if not merchant:
        raise HTTPException(status_code=404, detail="Merchant not found")
    db.delete(merchant)
    db.commit()
    return {"message": "Merchant deleted successfully"}
