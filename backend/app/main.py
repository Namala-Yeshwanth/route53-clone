from fastapi import FastAPI

from app.api.hosted_zones import router as zone_router

from app.core.exception_handlers import (
    register_exception_handlers
)

from app.api.dns_records import router as dns_record_router

from app.core.config import settings
from app.api.auth import (
    router as auth_router
)
app = FastAPI(
    title=settings.APP_NAME,
    version=settings.APP_VERSION
)
register_exception_handlers(app)
app.include_router(
    auth_router
)

app.include_router(zone_router)
app.include_router(dns_record_router)

@app.get("/")
def root():
    return {
        "message": "Route53 Clone API"
    }