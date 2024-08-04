from fastapi import APIRouter
from api.api_V1.handdlers import products_handlers

router = APIRouter()

router.include_router(products_handlers.products_router, prefix='/products')