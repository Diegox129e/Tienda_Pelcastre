from models.product import Products
from schemas.product_schema import ProductsCreate


class ProductsServices:
    @staticmethod
    async def create_product(data: ProductsCreate) -> Products:
        result = Products(**data.model_dump())
        await result.save()
        return result
