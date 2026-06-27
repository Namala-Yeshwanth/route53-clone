from fastapi import Depends, Query, HTTPException, status
from sqlalchemy.orm import Session

from app.database.session import SessionLocal

from app.schemas.query_params import QueryParams

from app.repositories.hosted_zone_repository import HostedZoneRepository
from app.repositories.dns_record_repository import DNSRecordRepository
from app.repositories.user_repository import UserRepository

from app.services.hosted_zone_service import HostedZoneService
from app.services.dns_record_service import DNSRecordService
from app.services.auth_service import AuthService

from app.security.jwt import (
    verify_access_token
)
from app.security.oauth2 import (
    oauth2_scheme
)
from app.models.user import User

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


def get_auth_service(
    db: Session = Depends(get_db)
):
    repository = UserRepository(db)

    return AuthService(repository)


def get_query_params(

    page: int = Query(
        default=1,
        ge=1
    ),

    size: int = Query(
        default=20,
        ge=1,
        le=100
    ),

    search: str | None = Query(
        default=None
    ),

    sort: str | None = Query(
        default=None,
        description="Sort field. Prefix with '-' for descending."
    )
):

    return QueryParams(
        page=page,
        size=size,
        search=search,
        sort=sort
    )

def get_current_user(

    token: str = Depends(
        oauth2_scheme
    ),

    db = Depends(
        get_db
    )

) -> User:

    payload = verify_access_token(
        token
    )

    if not payload:

        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid or expired token",
            headers={
                "WWW-Authenticate": "Bearer"
            }
        )

    email = payload.get(
        "sub"
    )

    if not email:

        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid token",
            headers={
                "WWW-Authenticate": "Bearer"
            }
        )

    repository = UserRepository(
        db
    )

    user = repository.get_by_email(
        email
    )

    if not user:

        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="User not found",
            headers={
                "WWW-Authenticate": "Bearer"
            }
        )

    return user