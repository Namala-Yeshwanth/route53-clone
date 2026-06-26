import ipaddress
import re

from app.models.enums import RecordType

from app.core.exceptions import (
    InvalidDNSRecordException
)

HOSTNAME_REGEX = re.compile(
    r"^(?=.{1,253}$)(?!-)[A-Za-z0-9-]{1,63}(?<!-)"
    r"(\.(?!-)[A-Za-z0-9-]{1,63}(?<!-))*\.?$"
)


class DNSValidator:

    @staticmethod
    def validate(
        record_type: RecordType,
        record_value: str,
        priority: int | None
    ):

        match record_type:

            case RecordType.A:
                try:
                    ipaddress.IPv4Address(record_value)
                except ValueError:
                    raise InvalidDNSRecordException(
                        "Invalid IPv4 address"
                    )

            case RecordType.AAAA:
                try:
                    ipaddress.IPv6Address(record_value)
                except ValueError:
                    raise InvalidDNSRecordException(
                        "Invalid IPv6 address"
                    )

            case RecordType.CNAME:
                if not HOSTNAME_REGEX.match(record_value):
                    raise InvalidDNSRecordException(
                        "Invalid hostname"
                    )

            case RecordType.NS:
                if not HOSTNAME_REGEX.match(record_value):
                    raise InvalidDNSRecordException(
                        "Invalid name server"
                    )

            case RecordType.MX:

                if priority is None:
                    raise InvalidDNSRecordException(
                        "MX record requires priority"
                    )

                if not HOSTNAME_REGEX.match(record_value):
                    raise InvalidDNSRecordException(
                        "Invalid mail server"
                    )

            case RecordType.TXT:
                pass