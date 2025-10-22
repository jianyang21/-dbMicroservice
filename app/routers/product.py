from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from .. import models
from ..database import get_db

router = APIRouter(prefix="/products", tags=["Products"])

@router.get("/")
def get_products(db: Session = Depends(get_db)):
    products = db.query(models.Product).all()
    return products

@router.get("/{product_id}")
def get_product(product_id: str, db: Session = Depends(get_db)):
    product = db.query(models.Product).filter(models.Product.id == product_id).first()
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    return product

@router.post("/")
def create_product(product: dict, db: Session = Depends(get_db)):
    new_product = models.Product(**product)
    db.add(new_product)
    db.commit()
    db.refresh(new_product)
    return {"message": "Product created successfully", "data": new_product}

@router.put("/{product_id}")
def update_product(product_id: str, product: dict, db: Session = Depends(get_db)):
    existing = db.query(models.Product).filter(models.Product.id == product_id).first()
    if not existing:
        raise HTTPException(status_code=404, detail="Product not found")
    for key, value in product.items():
        setattr(existing, key, value)
    db.commit()
    db.refresh(existing)
    return {"message": "Product updated successfully", "data": existing}

@router.delete("/{product_id}")
def delete_product(product_id: str, db: Session = Depends(get_db)):
    product = db.query(models.Product).filter(models.Product.id == product_id).first()
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    db.delete(product)
    db.commit()
    return {"message": "Product deleted successfully"}
