from datetime import datetime, timezone
from typing import Optional

from bson import ObjectId
from pydantic import BaseModel, BaseConfig, Field, EmailStr, validator


class RealModel(BaseModel):
    class Config(BaseConfig):
        allow_population_by_field_name = True
        json_encoders = {
            datetime: lambda dt: dt.replace(tzinfo=timezone.utc)
            .isoformat()
            .replace("+00:00", "Z")
        }


class DateTimeMixin(BaseModel):
    created_at: Optional[datetime] = Field(..., alias="createdAt")
    updated_at: Optional[datetime] = Field(..., alias="updatedAt")


class DBModelMixin(DateTimeMixin):
    id: Optional[str] = None


class Author(BaseModel):
    id: str = 'askfl'
    email: EmailStr = 'john@example.com'
    name: str = 'John Doe'
