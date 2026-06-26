from sqlalchemy.orm import Session

from app.models.hosted_zone import HostedZone


class HostedZoneRepository:

    def __init__(
        self,
        db: Session
    ):
        self.db = db

    def get_all(self):

        return (
            self.db.query(
                HostedZone
            ).all()
        )

    def create(
        self,
        zone_name: str,
        description: str | None
    ):

        zone = HostedZone(
            zone_name=zone_name,
            description=description
        )

        self.db.add(zone)

        self.db.commit()

        self.db.refresh(zone)

        return zone
    def get_by_id(self, zone_id: int):
        return (
            self.db.query(HostedZone)
            .filter(
                HostedZone.id == zone_id
            )
            .first()
        )
    def update(
        self,
        zone_id: int,
        zone_name: str,
        description: str | None
    ):
        zone = self.get_by_id(zone_id)

        if not zone:
            return None

        zone.zone_name = zone_name
        zone.description = description

        self.db.commit()
        self.db.refresh(zone)

        return zone
    def delete(
        self,
        zone_id: int
    ):
        zone = self.get_by_id(zone_id)

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
            self.db.query(HostedZone)
            .filter(
                HostedZone.zone_name == zone_name
            )
            .first()
        )