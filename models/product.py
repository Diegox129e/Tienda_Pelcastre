from datetime import datetime
from uuid import UUID, uuid4

from beanie import Document, Indexed
from pydantic import Field


class Products(Document):
    product_id: UUID = Field(default_factory=uuid4)
    product_category: str
    product_name: Indexed(str, unique=False)
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
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)
