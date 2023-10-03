from typing import List
from typing import Optional

from .my_base_model import MyBaseModel


class Category(MyBaseModel):
    id: str
    label: str
    description: Optional[str] = None


class ObservedProperty(MyBaseModel):
    id: Optional[str] = None
    label: str
    description: Optional[str] = None
    categories: Optional[List[Category]] = None
