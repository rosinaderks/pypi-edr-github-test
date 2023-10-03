from pydantic import BaseModel
from pydantic import ConfigDict


class MyBaseModel(BaseModel):
    model_config = ConfigDict(
        populate_by_name=True,
        str_strip_whitespace=True,
        extra="forbid",
        str_min_length=1,
        validate_default=True,
        validate_assignment=True,
    )
