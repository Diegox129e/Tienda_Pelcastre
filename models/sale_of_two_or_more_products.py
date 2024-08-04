from datetime import datetime

from beanie import Document, Indexed


class SaleOfTwoOrMoreProducts(Document):
    product_id: Indexed(int, unique=True)
    list_of_products: list
    received_amount: int
    exchange: int
    total_price: int
    owner: str
    date_and_time_of_sale: datetime
