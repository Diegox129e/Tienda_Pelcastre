from datetime import datetime

from beanie import Document, Indexed


class ReceiveSupplier(Document):
    supplier_id: int
    product_id: Indexed (int, unique=True)
    received_amount: int
    exchange: int
    date_and_time_of_receive: datetime
    owner: str
