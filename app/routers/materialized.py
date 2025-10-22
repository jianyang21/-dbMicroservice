from fastapi import APIRouter, Depends
from sqlalchemy import text
from ..database import get_db

router = APIRouter(prefix="/materialized", tags=["Materialized Views"])

@router.post("/create")
def create_materialized_view(db=Depends(get_db)):
    """Creates a materialized view summarizing product data."""
    query = text("""
        CREATE MATERIALIZED VIEW IF NOT EXISTS product_summary_mv AS
        SELECT 
            m.name AS merchant_name,
            COUNT(p.id) AS total_products,
            AVG(p.price) AS avg_price,
            SUM(p.price * (1 - p.discount/100)) AS total_value
        FROM "Product" p
        JOIN "Merchant" m ON p.merchant_id = m.id
        GROUP BY m.name;
    """)
    db.execute(query)
    db.commit()
    return {"message": "Materialized view created successfully"}

@router.post("/refresh")
def refresh_materialized_view(db=Depends(get_db)):
    """Refresh materialized view manually."""
    query = text("REFRESH MATERIALIZED VIEW product_summary_mv;")
    db.execute(query)
    db.commit()
    return {"message": "Materialized view refreshed successfully"}

@router.get("/view")
def get_materialized_data(db=Depends(get_db)):
    """Retrieve materialized view data."""
    result = db.execute(text("SELECT * FROM product_summary_mv;")).fetchall()
    return [dict(row) for row in result]
