from pydantic import BaseModel

from uuid import UUID


class InputObject(BaseModel):
    feature1: float
    feature2: float
    feature3: int
    feature4: bool
    identity: UUID


class Prediction(BaseModel):
    identity: UUID
    label: int | None
