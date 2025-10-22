from fastapi import FastAPI
from .routers import merchant, product, materialized
from .database import engine, Base

# Create all database tables
Base.metadata.create_all(bind=engine)

# Initialize app
app = FastAPI(title="Swipefit Microservice", version="1.0")

# Include routers
app.include_router(merchant.router)
app.include_router(product.router)
app.include_router(materialized.router)

# ✅ Root route
@app.get("/")
def root():
    return {"message": "Swipefit FastAPI microservice running 🚀"}
