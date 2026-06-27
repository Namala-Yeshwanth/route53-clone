from fastapi import FastAPI
from fastapi import Request
from fastapi.responses import JSONResponse

from app.core.exceptions import (
    HostedZoneNotFoundException,
    DNSRecordNotFoundException,
    DuplicateHostedZoneException,
    InvalidDNSRecordException,
    UserAlreadyExistsException,
    InvalidCredentialsException
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
    
    @app.exception_handler(
        UserAlreadyExistsException
    )
    async def user_exists_handler(
        request: Request,
        exc: UserAlreadyExistsException
    ):

        return JSONResponse(
            status_code=409,
            content={
                "detail": "User already exists"
            }
        )
    
    @app.exception_handler(
        InvalidCredentialsException
    )
    async def invalid_credentials(
        request: Request,
        exc: InvalidCredentialsException
    ):
        return JSONResponse(
            status_code=401,
            content={
                "detail": "Invalid email or password"
            }
        )