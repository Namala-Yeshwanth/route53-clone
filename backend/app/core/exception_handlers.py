from fastapi import FastAPI
from fastapi import Request
from fastapi.responses import JSONResponse

from app.core.exceptions import (
    HostedZoneNotFoundException,
    DNSRecordNotFoundException,
    DuplicateHostedZoneException,
    InvalidDNSRecordException
)


def register_exception_handlers(
    app: FastAPI
):

    @app.exception_handler(
        HostedZoneNotFoundException
    )
    async def hosted_zone_not_found(
        request: Request,
        exc: HostedZoneNotFoundException
    ):
        return JSONResponse(
            status_code=404,
            content={
                "detail": "Hosted Zone not found"
            }
        )

    @app.exception_handler(
        DNSRecordNotFoundException
    )
    async def dns_record_not_found(
        request: Request,
        exc: DNSRecordNotFoundException
    ):
        return JSONResponse(
            status_code=404,
            content={
                "detail": "DNS Record not found"
            }
        )

    @app.exception_handler(
        DuplicateHostedZoneException
    )
    async def duplicate_zone(
        request: Request,
        exc: DuplicateHostedZoneException
    ):
        return JSONResponse(
            status_code=409,
            content={
                "detail": "Hosted Zone already exists"
            }
        )

    @app.exception_handler(
        InvalidDNSRecordException
    )
    async def invalid_record(
        request: Request,
        exc: InvalidDNSRecordException
    ):
        return JSONResponse(
            status_code=400,
            content={
                "detail": "Invalid DNS Record"
            }
        )