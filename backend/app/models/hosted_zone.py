from datetime import datetime

from sqlalchemy import (
    String,
    DateTime,
    ForeignKey
)

from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship

from app.database.base import Base

class HostedZone(Base):
    __tablename__ = "hosted_zones"

    id: Mapped[int] = mapped_column(
        primary_key=True
    )
    user_id: Mapped[int] = mapped_column(
        ForeignKey("users.id")
    )

    zone_name: Mapped[str] = mapped_column(
        String(255),
        unique=True,
        index=True
    )

    description: Mapped[str | None] = mapped_column(
        nullable=True
    )

    created_at: Mapped[datetime] = mapped_column(
        DateTime,
        default=datetime.utcnow
    )

    user = relationship(
        "User",
        back_populates="hosted_zones"
    )

    dns_records = relationship(
        "DNSRecord",
        back_populates="hosted_zone",
        cascade="all, delete-orphan"
    )