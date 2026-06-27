from sqlalchemy.orm import Session

from app.models.dns_record import DNSRecord
from app.repositories.base_repository import BaseRepository
from app.models.enums import RecordType

class DNSRecordRepository(
    BaseRepository[DNSRecord]
):

    def __init__(
        self,
        db: Session
    ):
        super().__init__(
            db,
            DNSRecord
        )

    def get_all(
        self,
        hosted_zone_id: int
    ):

        return (
            self.db.query(
                DNSRecord
            )
            .filter(
                DNSRecord.hosted_zone_id == hosted_zone_id
            )
            .all()
        )

    def get_by_id_and_zone(
        self,
        record_id: int,
        hosted_zone_id: int
    ):

        return (
            self.db.query(
                DNSRecord
            )
            .filter(
                DNSRecord.id == record_id,
                DNSRecord.hosted_zone_id == hosted_zone_id
            )
            .first()
        )
    
    def get_duplicate(
        self,
        hosted_zone_id: int,
        record_name: str,
        record_type: RecordType,
        record_value: str
    ):

        return (
            self.db.query(
                DNSRecord
            )
            .filter(
                DNSRecord.hosted_zone_id == hosted_zone_id,
                DNSRecord.record_name == record_name,
                DNSRecord.record_type == record_type,
                DNSRecord.record_value == record_value
            )
            .first()
        )