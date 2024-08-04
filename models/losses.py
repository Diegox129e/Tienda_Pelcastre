from datetime import datetime

from beanie import Document, Indexed


class Losses(Document):
    product_id: Indexed (int, unique=True)
    quantity: int
    date_and_time_of_losses: datetime
    reason_for_losses: str
    responsible_person: str
    comment: str
    created_at: datetime
    updated_at: datetime
    deleted_at: datetime