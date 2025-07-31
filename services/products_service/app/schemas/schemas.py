from pydantic import BaseModel, Field, ConfigDict
from datetime import datetime
from decimal import Decimal

class CategoryAdd(BaseModel):
    name: str = Field(max_length=80)

class CategoryRead(CategoryAdd):
    id: int
    model_config = ConfigDict(from_attributes=True)


class ProductAdd(BaseModel):
    name: str = Field(max_length=120)
    price: Decimal = Field(ge=0)
    category_id: int

class ProductUpdate(BaseModel):
    name: str | None = Field(default=None, max_length=120)
    price: Decimal | None = Field(default=None, ge=0)
    category_id: int | None = None

class ProductRead(ProductAdd):
    id: int
    created_at: datetime
    updated_at: datetime
    
    model_config = ConfigDict(from_attributes=True)
    