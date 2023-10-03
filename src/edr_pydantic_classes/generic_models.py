from typing import List
from typing import Optional

from covjson_pydantic.domain import DomainType

from .my_base_model import MyBaseModel


class Variables(MyBaseModel):
    model_config = {"json_schema_extra": {"examples": [{"query_type": "position"}]}}
    query_type: str
    output_formats: Optional[List[str]] = None
    default_output_format: Optional[str] = None


class CubeVariables(Variables):
    model_config = {"json_schema_extra": {"examples": [{"height_units": "m"}]}}
    height_units: str


class Link(MyBaseModel):
    model_config = {
        "json_schema_extra": {
            "templated": {
                "description": "defines if the link href value is a template with values requiring replacement"
            },
            "examples": [
                {
                    "href": "https://data.example.com/collections/monitoringsites/locations/1234",
                    "rel": "alternate",
                    "type": "application/geo+json",
                    "title": "Monitoring site name",
                    "hreflang": "en",
                }
            ],
        }
    }
    href: str
    rel: str
    type: Optional[str] = None
    hreflang: Optional[str] = None
    title: Optional[str] = None
    length: Optional[int] = None
    templated: Optional[bool] = None


class SupportedQueries(MyBaseModel):
    model_config = {
        "json_schema_extra": {
            "domain_types": {
                "description": "A list of domain types from which can be determined what endpoints are allowed."
            },
            "has_location": {
                "description": "A boolean from which can be determined if the backend has the /locations endpoint."
            },
            "examples": [
                {
                    "domain_types": "When [DomainType.point_series] is returned, "
                    "the /position endpoint is allowed but /cube is not allowed.",
                    "has_locations": "When True is returned, the backend has the /locations endpoint.",
                }
            ],
        }
    }
    domain_types: List[DomainType]
    has_locations: bool
