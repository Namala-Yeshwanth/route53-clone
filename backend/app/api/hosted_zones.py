from fastapi import APIRouter, Depends

from app.core.dependencies import get_hosted_zone_service

from app.schemas.hosted_zone import (
    HostedZoneCreate,
    HostedZoneResponse,
    HostedZoneUpdate
)


from app.services.hosted_zone_service import (
    HostedZoneService
)

router = APIRouter(
    prefix="/zones",
    tags=["Hosted Zones"]
)


@router.get(
    "/",
    response_model=list[HostedZoneResponse]
)
def list_zones(
    service: HostedZoneService = Depends(
        get_hosted_zone_service
    )
):
    return service.list_zones()


@router.post(
    "/",
    response_model=HostedZoneResponse
)
def create_zone(
    data: HostedZoneCreate,
    service: HostedZoneService = Depends(
        get_hosted_zone_service
    )
):
    return service.create_zone(
        data.zone_name,
        data.description
    )

@router.get(
    "/{zone_id}",
    response_model=HostedZoneResponse
)
def get_zone(
    zone_id: int,
    service: HostedZoneService = Depends(
        get_hosted_zone_service
    )
):
    return service.get_zone(
        zone_id
    )
    
@router.put(
    "/{zone_id}",
    response_model=HostedZoneResponse
)
def update_zone(
    zone_id: int,
    data: HostedZoneUpdate,
    service: HostedZoneService = Depends(
        get_hosted_zone_service
    )
):
    return service.update_zone(
        zone_id,
        data.zone_name,
        data.description
    )

@router.delete(
    "/{zone_id}"
)
def delete_zone(
    zone_id: int,
    service: HostedZoneService = Depends(
        get_hosted_zone_service
    )
):
    service.delete_zone(
        zone_id
    )

    return {
        "message": "Hosted Zone deleted"
    }
