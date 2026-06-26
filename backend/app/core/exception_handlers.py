from fastapi import FastAPI
from fastapi import Request
from fastapi.responses import JSONResponse

from app.core.exceptions import (
    HostedZoneNotFoundException,
    DuplicateHostedZoneException
)


def register_exception_handlers(
    app: FastAPI
):

    @app.exception_handler(
        HostedZoneNotFoundException
    )
    async def hosted_zone_not_found_handler(
        request: Request,
        exc: HostedZoneNotFoundException
    ):
        return JSONResponse(
            status_code=404,
            content={
                "detail":
                "Hosted Zone not found"
            }
        )

    @app.exception_handler(
        DuplicateHostedZoneException
    )
    async def duplicate_zone_handler(
        request: Request,
        exc: DuplicateHostedZoneException
    ):
        return JSONResponse(
            status_code=409,
            content={
                "detail":
                "Zone name already exists"
            }
        )