import pymongo.errors
from fastapi import APIRouter, HTTPException, status

from models.product import Products
from schemas.product_schema import ProductsCreate
from services.product_services import ProductsServices

products_router = APIRouter()


@products_router.post('/products', response_model=Products, tags=["Products"])
async def get_products(data: ProductsCreate):
    try:
        result = await ProductsServices.create_product(data)
        return result
    except pymongo.errors.OperationFailure:
        raise HTTPException(
            status_code= status.HTTP_400_BAD_REQUEST,
            detail= "Error al crear el producto"
        )
