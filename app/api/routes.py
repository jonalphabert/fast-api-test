from fastapi import APIRouter
from app.api.products.routes import router as product_router
from app.api.auth.routes import router as auth_router
from app.api.transactions.routes import router as transactions_router

router = APIRouter()

router.include_router(product_router)
router.include_router(auth_router)
router.include_router(transactions_router)