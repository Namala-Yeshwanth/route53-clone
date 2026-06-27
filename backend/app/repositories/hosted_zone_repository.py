from sqlalchemy.orm import Session
from sqlalchemy import asc, desc

from app.models.hosted_zone import HostedZone
from app.repositories.base_repository import BaseRepository


class HostedZoneRepository(
    BaseRepository[HostedZone]
):

    def __init__(
        self,
        db: Session
    ):
        super().__init__(
            db,
            HostedZone
        )

    def get_all(
        self,
        user_id: int,
        offset: int,
        limit: int,
        search: str | None = None,
        sort: str | None = None
    ):

        query = (
            self.db.query(
                HostedZone
            )
            .filter(
                HostedZone.user_id == user_id
            )
        )

        if search:

            query = query.filter(
                HostedZone.zone_name.ilike(
                    f"%{search}%"
                )
            )

        if sort:

            descending = sort.startswith("-")

            field = sort.lstrip("-")

            allowed_fields = {
                "zone_name": HostedZone.zone_name,
                "created_at": HostedZone.created_at
            }

            if field in allowed_fields:

                column = allowed_fields[field]

                query = query.order_by(
                    desc(column)
                    if descending
                    else asc(column)
                )

        return (
            query
            .offset(offset)
            .limit(limit)
            .all()
        )

    def update(
        self,
        zone_id: int,
        user_id: int,
        zone_name: str,
        description: str | None
    ):

        zone = self.get_by_id_and_user(
            zone_id,
            user_id
        )

        if not zone:
            return None

        zone.zone_name = zone_name
        zone.description = description

        self.db.commit()
        self.db.refresh(zone)

        return zone

    def delete(
        self,
        zone_id: int,
        user_id: int
    ):

        zone = self.get_by_id_and_user(
            zone_id,
            user_id
        )

        if not zone:
            return None

        self.db.delete(zone)
        self.db.commit()

        return zone

    def get_by_name(
        self,
        zone_name: str
    ):

        return (
            self.db.query(
                HostedZone
            )
            .filter(
                HostedZone.zone_name == zone_name
            )
            .first()
        )
    
    def get_by_id_and_user(
        self,
        zone_id: int,
        user_id: int
    ):
        return (
            self.db.query(
                HostedZone
            )
            .filter(
                HostedZone.id == zone_id,
                HostedZone.user_id == user_id
            )
            .first()
        )