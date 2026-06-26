from app.repositories.hosted_zone_repository import (
    HostedZoneRepository
)

from app.core.exceptions import (
    HostedZoneNotFoundException,
    DuplicateHostedZoneException
)

class HostedZoneService:

    def __init__(
        self,
        repository: HostedZoneRepository
    ):
        self.repository = repository

    def list_zones(self):

        return self.repository.get_all()

    def create_zone(
        self,
        zone_name: str,
        description: str | None
    ):

        existing_zone = (
            self.repository.get_by_name(
                zone_name
            )
        )

        if existing_zone:
            raise DuplicateHostedZoneException()

        return self.repository.create(
            zone_name,
            description
        )

    def get_zone(
        self,
        zone_id: int
    ):

        zone = self.repository.get_by_id(
            zone_id
        )

        if not zone:
            raise HostedZoneNotFoundException()

        return zone
    
    def update_zone(
        self,
        zone_id: int,
        zone_name: str,
        description: str | None
    ):

        existing_zone = (
            self.repository.get_by_name(
                zone_name
            )
        )

        if (
            existing_zone
            and existing_zone.id != zone_id
        ):
            raise DuplicateHostedZoneException()
        zone = self.repository.update(
            zone_id,
            zone_name,
            description
        )

        if not zone:
            raise HostedZoneNotFoundException()

        return zone
    
    def delete_zone(
        self,
        zone_id: int
    ):
        zone = self.repository.delete(
            zone_id
        )

        if not zone:
            raise HostedZoneNotFoundException()

        return zone
    