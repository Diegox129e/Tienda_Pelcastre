from datetime import datetime

from beanie import Document, Indexed


class DoubtToSupplier(Document):
    supplier_name: Indexed (str,unique=True)
    amount: float
    date: datetime