from fastapi import APIRouter, Depends

from app.core.dependencies import get_hosted_zone_service, get_current_user

from app.schemas.hosted_zone import (
    HostedZoneCreate,
    HostedZoneResponse,
    HostedZoneUpdate
)

from app.schemas.query_params import (
    QueryParams
)

from app.services.hosted_zone_service import (
    HostedZoneService
)

from fastapi import status, Query
from fastapi.responses import Response

from app.models.user import User

from app.core.dependencies import (
    get_current_user
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
        default=None
    ),

    current_user: User = Depends(
        get_current_user
    ),

    service: HostedZoneService = Depends(
        get_hosted_zone_service
    )
):

    return service.list_zones(
        user_id=current_user.id,
        page=page,
        size=size,
        search=search,
        sort=sort
    )

@router.post(
    "/",
    response_model=HostedZoneResponse,
    status_code=status.HTTP_201_CREATED
)
def create_zone(
    data: HostedZoneCreate,

    current_user: User = Depends(
        get_current_user
    ),

    service: HostedZoneService = Depends(
        get_hosted_zone_service
    )
):

    return service.create_zone(
        user_id=current_user.id,
        zone_name=data.zone_name,
        description=data.description
    )

@router.get(
    "/{zone_id}",
    response_model=HostedZoneResponse
)
def get_zone(
    zone_id: int,

    current_user: User = Depends(
        get_current_user
    ),

    service: HostedZoneService = Depends(
        get_hosted_zone_service
    )
):
    return service.get_zone(
        zone_id,
        current_user.id
    )
    
@router.put(
    "/{zone_id}",
    response_model=HostedZoneResponse
)
def update_zone(
    zone_id: int,
    data: HostedZoneUpdate,

    current_user: User = Depends(
        get_current_user
    ),

    service: HostedZoneService = Depends(
        get_hosted_zone_service
    )
):
    return service.update_zone(
        zone_id=zone_id,
        user_id=current_user.id,
        zone_name=data.zone_name,
        description=data.description
    )

@router.delete(
    "/{zone_id}",
    status_code=status.HTTP_204_NO_CONTENT
)
def delete_zone(
    zone_id: int,

    current_user: User = Depends(
        get_current_user
    ),

    service: HostedZoneService = Depends(
        get_hosted_zone_service
    )
):
    service.delete_zone(
        zone_id,
        current_user.id
    )

    return Response(
        status_code=status.HTTP_204_NO_CONTENT
    )