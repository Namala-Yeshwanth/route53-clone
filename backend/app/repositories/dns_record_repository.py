from sqlalchemy.orm import Session

from app.models.dns_record import DNSRecord
from app.repositories.base_repository import BaseRepository


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