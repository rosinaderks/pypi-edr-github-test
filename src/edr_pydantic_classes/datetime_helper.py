import re
from datetime import datetime

from dateutil import parser

# Matches correct ISO-8601 with dashes, UTC or local time, optional colon in local time. Allows milliseconds.
# 2016-07-08T12:30:00Z
# 2000-01-03T12:30:01.999Z
# 2000-01-03T12:30:01.0Z
ISO_8601_WITH_TZ_REGEX = r"\d{4}-(?:0[1-9]|1[0-2])-(?:0[1-9]|[1-2]\d|3[0-1])T(?:[0-1]\d|2[0-3]):[0-5]\d:[0-5]\d(?:\.\d+|)(?:Z|(?:\+|\-)(?:\d{2}):?(?:\d{2}))$"  # noqa: E501


def datetime_to_iso_string(value: datetime) -> str:
    """If the datetime does not have a time zone adds a `Z` as timezone indicator.
    Changes timezone +00:00 to the military time zone indicator (Z).
    And returns the datetime as ISO 8601 string.

    Keyword arguments:
    value -- A datetime

    Returns:
    datetime string -- Returns the datetime as an ISO 8601 string with the military indicator.
    """
    iso_8601_regex = re.compile(ISO_8601_WITH_TZ_REGEX)
    iso_8601_str = value.isoformat()
    greenwich = "+00:00"
    if iso_8601_str.endswith(greenwich):
        return f"{iso_8601_str[:-len(greenwich)]}Z"
    elif re.search(iso_8601_regex, iso_8601_str):
        return iso_8601_str
    else:
        return f"{iso_8601_str}Z"


def parse_datetime_with_tz(dt_str: str) -> datetime:
    try:
        dt = parser.isoparse(dt_str)
    except Exception as e:
        raise ValueError(f"invalid date-time string '{dt_str}', should be in ISO 8601 format with timezone") from e
    if dt.tzinfo is None:
        raise ValueError(f"no time zone in '{dt_str}', date-time string should be in ISO 8601 format with timezone")
    return dt
