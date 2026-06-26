from pydantic import BaseModel, Field
from app.models.enums import RecordType


class DNSRecordCreate(BaseModel):
    record_name: str = Field(
        min_length=1,
        max_length=255
    )

    record_type: RecordType

    record_value: str = Field(
        min_length=1,
        max_length=500
    )

    ttl: int = Field(
        default=300,
        ge=60,
        le=86400
    )

    priority: int | None = Field(
        default=None,
        ge=0
    )


class DNSRecordUpdate(BaseModel):
    record_name: str = Field(
        min_length=1,
        max_length=255
    )

    record_type: RecordType

    record_value: str = Field(
        min_length=1,
        max_length=500
    )

    ttl: int = Field(
        default=300,
        ge=60,
        le=86400
    )

    priority: int | None = Field(
        default=None,
        ge=0
    )


class DNSRecordResponse(BaseModel):
    id: int
    hosted_zone_id: int
    record_name: str
    record_type: RecordType
    record_value: str
    ttl: int
    priority: int | None

    model_config = {
        "from_attributes": True
    }