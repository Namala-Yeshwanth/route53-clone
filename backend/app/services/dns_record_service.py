from app.models.dns_record import DNSRecord

from app.repositories.dns_record_repository import (
    DNSRecordRepository
)

from app.repositories.hosted_zone_repository import (
    HostedZoneRepository
)

from app.validators.dns_validator import (
    DNSValidator
)

from app.core.exceptions import (
    HostedZoneNotFoundException,
    DNSRecordNotFoundException,
    DuplicateDNSRecordException
)

from app.models.enums import RecordType


class DNSRecordService:

    def __init__(
        self,
        dns_repository: DNSRecordRepository,
        hosted_zone_repository: HostedZoneRepository
    ):
        self.dns_repository = dns_repository
        self.hosted_zone_repository = hosted_zone_repository

    def _get_hosted_zone(
        self,
        user_id: int,
        hosted_zone_id: int
    ):

        zone = self.hosted_zone_repository.get_by_id_and_user(
            hosted_zone_id,
            user_id
        )

        if not zone:
            raise HostedZoneNotFoundException()

        return zone

    def list_records(
        self,
        user_id: int,
        hosted_zone_id: int
    ):

        self._get_hosted_zone(
            user_id,
            hosted_zone_id
        )

        return self.dns_repository.get_all(
            hosted_zone_id
        )

    def get_record(
        self,
        user_id: int,
        hosted_zone_id: int,
        record_id: int
    ):

        self._get_hosted_zone(
            user_id,
            hosted_zone_id
        )

        record = self.dns_repository.get_by_id_and_zone(
            record_id,
            hosted_zone_id
        )

        if not record:
            raise DNSRecordNotFoundException()

        return record

    def create_record(
        self,
        user_id: int,
        hosted_zone_id: int,
        record_name: str,
        record_type: RecordType,
        record_value: str,
        ttl: int,
        priority: int | None
    ):

        self._get_hosted_zone(
            user_id,
            hosted_zone_id
        )

        DNSValidator.validate(
            record_type=record_type,
            record_value=record_value,
            priority=priority
        )

        existing = self.dns_repository.get_duplicate(
            hosted_zone_id,
            record_name,
            record_type,
            record_value
        )

        if existing:
            raise DuplicateDNSRecordException()
        
        record = DNSRecord(
            hosted_zone_id=hosted_zone_id,
            record_name=record_name,
            record_type=record_type,
            record_value=record_value,
            ttl=ttl,
            priority=priority
        )

        return self.dns_repository.create(
            record
        )

    def update_record(
        self,
        user_id: int,
        hosted_zone_id: int,
        record_id: int,
        record_name: str,
        record_type: RecordType,
        record_value: str,
        ttl: int,
        priority: int | None
    ):

        self._get_hosted_zone(
            user_id,
            hosted_zone_id
        )

        record = self.dns_repository.get_by_id_and_zone(
            record_id,
            hosted_zone_id
        )

        if not record:
            raise DNSRecordNotFoundException()

        DNSValidator.validate(
            record_type=record_type,
            record_value=record_value,
            priority=priority
        )

        existing = self.dns_repository.get_duplicate(
            hosted_zone_id,
            record_name,
            record_type,
            record_value
        )

        if existing and existing.id != record.id:
            raise DuplicateDNSRecordException()

        record.record_name = record_name
        record.record_type = record_type
        record.record_value = record_value
        record.ttl = ttl
        record.priority = priority

        return self.dns_repository.update(
            record
        )

    def delete_record(
        self,
        user_id: int,
        hosted_zone_id: int,
        record_id: int
    ):

        self._get_hosted_zone(
            user_id,
            hosted_zone_id
        )

        record = self.dns_repository.get_by_id_and_zone(
            record_id,
            hosted_zone_id
        )

        if not record:
            raise DNSRecordNotFoundException()

        self.dns_repository.delete(
            record
        )