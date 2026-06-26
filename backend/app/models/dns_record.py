from datetime import datetime

from sqlalchemy import DateTime, ForeignKey, Integer, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database.base import Base

from sqlalchemy import Enum

from app.models.enums import RecordType

class DNSRecord(Base):
    __tablename__ = "dns_records"

    id: Mapped[int] = mapped_column(
        primary_key=True
    )

    hosted_zone_id: Mapped[int] = mapped_column(
        ForeignKey("hosted_zones.id")
    )

    record_name: Mapped[str] = mapped_column(
        String(255)
    )

    record_type: Mapped[RecordType] = mapped_column(
        Enum(RecordType)
    )

    record_value: Mapped[str] = mapped_column(
        String(500)
    )

    ttl: Mapped[int] = mapped_column(
        Integer,
        default=300
    )

    priority: Mapped[int | None] = mapped_column(
        Integer,
        nullable=True
    )

    created_at: Mapped[datetime] = mapped_column(
        DateTime,
        default=datetime.utcnow
    )

    hosted_zone = relationship(
        "HostedZone",
        back_populates="dns_records"
    )