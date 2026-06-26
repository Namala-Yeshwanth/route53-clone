from pydantic import BaseModel, Field


class QueryParams(BaseModel):

    page: int = Field(
        default=1,
        ge=1
    )

    size: int = Field(
        default=20,
        ge=1,
        le=100
    )

    search: str | None = None

    sort: str | None = None