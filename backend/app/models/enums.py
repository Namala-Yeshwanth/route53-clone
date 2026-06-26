from enum import Enum


class RecordType(str, Enum):

    A = "A"

    AAAA = "AAAA"

    CNAME = "CNAME"

    MX = "MX"

    TXT = "TXT"

    NS = "NS"