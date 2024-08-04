from pydantic import BaseModel


class ProductsCreate (BaseModel):
    product_category: str
    product_name: str
    product_quantity: int
    product_brand: str
    product_variant: str
    product_type: str
    product_code: str
    product_status: str
    product_price_for_clients: int
    product_price_for_providers: int
    product_description: str
    product_image: str