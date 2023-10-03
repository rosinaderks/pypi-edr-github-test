from __future__ import annotations

from typing import List
from typing import Optional

from pydantic import Field

from .generic_models import Link
from .my_base_model import MyBaseModel


class Provider(MyBaseModel):
    name: str
    url: Optional[str] = None


class Contact(MyBaseModel):
    email: Optional[str] = None
    phone: Optional[str] = None
    fax: Optional[str] = None
    hours: Optional[str] = None
    instructions: Optional[str] = None
    address: Optional[str] = None
    postalCode: Optional[str] = None  # noqa: N815
    city: Optional[str] = None
    stateorprovince: Optional[str] = None
    country: Optional[str] = None


class LandingPageModel(MyBaseModel):
    links: List[Link] = Field(
        ...,
        example=[
            {
                "href": "http://www.example.org/edr",
                "hreflang": "en",
                "rel": "service-desc",
                "type": "application/vnd.oai.openapi+json;version=3.0",
                "title": "",
            },
            {
                "href": "http://www.example.org/edr/conformance",
                "hreflang": "en",
                "rel": "data",
                "type": "application/json",
                "title": "",
            },
            {
                "href": "http://www.example.org/edr/collections",
                "hreflang": "en",
                "rel": "data",
                "type": "application/json",
                "title": "",
            },
        ],
    )
    title: Optional[str] = None
    description: Optional[str] = None
    keywords: Optional[List[str]] = None
    provider: Optional[Provider] = None
    contact: Optional[Contact] = None


class ConformanceModel(MyBaseModel):
    conformsTo: List[str]  # noqa: N815
