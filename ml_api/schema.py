from math import isinf, isnan

from pydantic import BaseModel

from uuid import UUID


class InputObject(BaseModel):
    feature1: float
    feature2: float
    feature3: int
    feature4: bool
    identity: UUID

    def list(self):
        return list(self.model_dump(exclude={'identity'}).values())

    def has_nan_or_inf(self) -> bool:
        """Обычно модели не работают с сущнастями nan или inf. Их надо отдельно обрабатывать"""
        for field_name, field_properties in self.model_fields.items():
            if field_properties.annotation is float:
                value = getattr(self, field_name)
                if isnan(value) or isinf(value):
                    return True
        return False


class Prediction(BaseModel):
    identity: UUID
    label: int | None
