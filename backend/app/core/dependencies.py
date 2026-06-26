from app.database.session import SessionLocal

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

from fastapi import Depends
from sqlalchemy.orm import Session

from app.database.session import SessionLocal

from app.repositories.hosted_zone_repository import (
    HostedZoneRepository
)

from app.services.hosted_zone_service import (
    HostedZoneService
)

from app.repositories.dns_record_repository import (
    DNSRecordRepository
)

from app.services.dns_record_service import (
    DNSRecordService
)

def get_db():
    db = SessionLocal()

    try:
        yield db

    finally:
        db.close()


def get_hosted_zone_service(
    db: Session = Depends(get_db)
):

    repository = HostedZoneRepository(db)

    return HostedZoneService(
        repository
    )

def get_dns_record_service(
    db: Session = Depends(get_db)
):

    dns_repository = DNSRecordRepository(db)

    hosted_zone_repository = HostedZoneRepository(db)

    return DNSRecordService(
        dns_repository,
        hosted_zone_repository
    )