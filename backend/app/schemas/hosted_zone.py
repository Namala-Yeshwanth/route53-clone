from pydantic import BaseModel, Field

class HostedZoneCreate(BaseModel):
    zone_name: str = Field(
        min_length=3,
        max_length=255
    )

    description: str | None = Field(
        default=None,
        max_length=500
    )


class HostedZoneResponse(BaseModel):
    id: int
    zone_name: str
    description: str | None

    model_config = {
        "from_attributes": True
    }

class HostedZoneUpdate(BaseModel):
    zone_name: str = Field(
        min_length=3,
        max_length=255
    )
    description: str | None = Field(
        default=None,
        max_length=500
    )