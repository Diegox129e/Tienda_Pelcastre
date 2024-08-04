from datetime import datetime

from beanie import Document, Indexed


class Debtors(Document):
    name: Indexed (str,unique=True)
    debt: float
    owner: str
    date: datetime
