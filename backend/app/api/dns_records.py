from fastapi import APIRouter, Depends, status
from fastapi.responses import Response

from app.schemas.dns_record import (
    DNSRecordCreate,
    DNSRecordUpdate,
    DNSRecordResponse
)

from app.services.dns_record_service import (
    DNSRecordService
)

from app.core.dependencies import (
    get_dns_record_service
)

router = APIRouter(
    prefix="/zones/{hosted_zone_id}/records",
    tags=["DNS Records"]
)


@router.post(
    "/",
    response_model=DNSRecordResponse,
    status_code=status.HTTP_201_CREATED
)
def create_record(
    hosted_zone_id: int,
    data: DNSRecordCreate,
    service: DNSRecordService = Depends(
        get_dns_record_service
    )
):
    return service.create_record(
        hosted_zone_id=hosted_zone_id,
        record_name=data.record_name,
        record_type=data.record_type,
        record_value=data.record_value,
        ttl=data.ttl,
        priority=data.priority
    )


@router.get(
    "/",
    response_model=list[DNSRecordResponse]
)
def list_records(
    hosted_zone_id: int,
    service: DNSRecordService = Depends(
        get_dns_record_service
    )
):
    return service.list_records(
        hosted_zone_id
    )


@router.get(
    "/{record_id}",
    response_model=DNSRecordResponse
)
def get_record(
    hosted_zone_id: int,
    record_id: int,
    service: DNSRecordService = Depends(
        get_dns_record_service
    )
):
    return service.get_record(
        hosted_zone_id,
        record_id
    )


@router.put(
    "/{record_id}",
    response_model=DNSRecordResponse
)
def update_record(
    hosted_zone_id: int,
    record_id: int,
    data: DNSRecordUpdate,
    service: DNSRecordService = Depends(
        get_dns_record_service
    )
):
    return service.update_record(
        hosted_zone_id=hosted_zone_id,
        record_id=record_id,
        record_name=data.record_name,
        record_type=data.record_type,
        record_value=data.record_value,
        ttl=data.ttl,
        priority=data.priority
    )


@router.delete(
    "/{record_id}",
    status_code=status.HTTP_204_NO_CONTENT
)
def delete_record(
    hosted_zone_id: int,
    record_id: int,
    service: DNSRecordService = Depends(
        get_dns_record_service
    )
):
    service.delete_record(
        hosted_zone_id=hosted_zone_id,
        record_id=record_id
    )

    return Response(
        status_code=status.HTTP_204_NO_CONTENT
    )