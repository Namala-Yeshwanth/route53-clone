from typing import Generic, TypeVar, Type

from sqlalchemy.orm import Session

T = TypeVar("T")


class BaseRepository(
    Generic[T]
):

    def __init__(
        self,
        db: Session,
        model: Type[T]
    ):
        self.db = db
        self.model = model

    def get_by_id(
        self,
        entity_id: int
    ):
        return (
            self.db.query(
                self.model
            )
            .filter(
                self.model.id == entity_id
            )
            .first()
        )

    def create(
        self,
        entity: T
    ):
        self.db.add(entity)

        self.db.commit()

        self.db.refresh(entity)

        return entity

    def update(
        self,
        entity: T
    ):
        self.db.commit()

        self.db.refresh(entity)

        return entity

    def delete(
        self,
        entity: T
    ):
        self.db.delete(entity)

        self.db.commit()