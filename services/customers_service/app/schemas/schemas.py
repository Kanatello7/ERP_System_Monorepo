from pydantic import BaseModel, Field, ConfigDict
from datetime import datetime

class CustomerAdd(BaseModel):
    first_name: str = Field(max_length=150)
    last_name: str = Field(max_length=150)
    email: str = Field(max_length=150)
    phone: str | None = Field(max_length=30, default=None)

class CustomerUpdate(BaseModel):
    first_name: str | None = Field(max_length=150, default=None)
    last_name: str | None = Field(max_length=150, default=None)
    email: str | None = Field(max_length=150, default=None)
    phone: str | None = Field(max_length=30, default=None)
    
class CustomerRead(CustomerAdd):
    id: int 
    created_at: datetime
    updated_at: datetime
    
    model_config = ConfigDict(from_attributes=True)