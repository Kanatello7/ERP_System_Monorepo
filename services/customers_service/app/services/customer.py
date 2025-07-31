from typing import List
from ..repositories.utils import AbstractRepository
from ..schemas.schemas import CustomerAdd, CustomerUpdate, CustomerRead
from shared_lib.universal_table import UniversalTable


TABLE_SCHEMA = {
    "id":         ("ID",        "number"),
    "first_name": ("Name",      "string"),
    "last_name":  ("Surname",   "string"),
    "email":      ("Email",     "string"),
    "phone":      ("Phone",     "string"),
    "created_at": ("Created",   "date"),
    "updated_at": ("Updated",   "date"),

}

class CustomerService:
    def __init__(self, repo: AbstractRepository):
        self.customer_repo = repo
    
    async def get_all(self) -> List[CustomerRead]:
        rows = await self.customer_repo.get_all()
        return [CustomerRead.model_validate(r) for r in rows]

    async def get_one(self, id: int) -> CustomerRead | None:
        row = await self.customer_repo.get_one(id)
        return CustomerRead.model_validate(row) if row else None

    async def add_one(self, customer: CustomerAdd) -> CustomerRead:
        row = await self.customer_repo.add_one(customer.model_dump())
        return CustomerRead.model_validate(row)

    async def update_one(self, id: int, new_customer: CustomerUpdate) -> CustomerRead | None:
        row = await self.customer_repo.update_one(id, new_customer.model_dump(exclude_unset=True))
        return CustomerRead.model_validate(row) if row else None

    async def delete_one(self, id: int) -> None:
        await self.customer_repo.delete_one(id)
    
    async def universal_table(self) -> UniversalTable:
        customers = await self.customer_repo.get_all()
        return UniversalTable.from_instances(customers, TABLE_SCHEMA)