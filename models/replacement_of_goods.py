from datetime import datetime

from beanie import Document, Indexed


class ReplacementOfGoods(Document):
    product_id: Indexed (int, unique=True)
    replacement_id: int
    reason_for_replacement: str
    date_and_time_of_replacement: datetime
    owner: str