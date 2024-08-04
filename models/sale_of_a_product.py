from datetime import datetime

from beanie import Document, Indexed


class SaleOfAProduct(Document):
    product_id: Indexed (int, unique=True)
    received_amount:int
    exchange:int
    product_name: str
    product_price: int
    total_price: int
    owner: str
    date_and_time_of_sale: datetime