from sqlalchemy.orm import Session

from app.models.dns_record import DNSRecord


class DNSRecordRepository:

    def __init__(
        self,
        db: Session
    ):
        self.db = db

    def get_all(
        self,
        hosted_zone_id: int
    ):
        return (
            self.db.query(DNSRecord)
            .filter(
                DNSRecord.hosted_zone_id == hosted_zone_id
            )
            .all()
        )

    def get_by_id(
        self,
        record_id: int
    ):
        return (
            self.db.query(DNSRecord)
            .filter(
                DNSRecord.id == record_id
            )
            .first()
        )

    def get_by_id_and_zone(
        self,
        record_id: int,
        hosted_zone_id: int
    ):
        return (
            self.db.query(DNSRecord)
            .filter(
                DNSRecord.id == record_id,
                DNSRecord.hosted_zone_id == hosted_zone_id
            )
            .first()
        )
        
    def create(
        self,
        record: DNSRecord
    ):
        self.db.add(record)
        self.db.commit()
        self.db.refresh(record)

        return record

    def update(
        self,
        record: DNSRecord
    ):
        self.db.commit()
        self.db.refresh(record)

        return record

    def delete(
        self,
        record: DNSRecord
    ):
        self.db.delete(record)
        self.db.commit()
    
