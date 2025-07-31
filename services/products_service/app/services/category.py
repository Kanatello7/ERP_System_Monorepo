from typing import List
from app.schemas.schemas import CategoryAdd, CategoryRead
from app.repositories.utils import AbstractRepository
from shared_lib.universal_table import UniversalTable

TABLE_SCHEMA = {
    "id":         ("ID",        "number"),
    "name":       ("Category",   "string"),
}

class CategoryService:
    def __init__(self, repository: AbstractRepository):
        self.category_repo = repository

    async def get_all(self) -> List[CategoryRead]:
        rows = await self.category_repo.get_all()
        return [CategoryRead.model_validate(r) for r in rows]

    async def get_one(self, id: int) -> CategoryRead | None:
        row = await self.category_repo.get_one(id)
        return CategoryRead.model_validate(row) if row else None

    async def add_one(self, category: CategoryAdd) -> CategoryRead:
        row = await self.category_repo.add_one(category.model_dump())
        return CategoryRead.model_validate(row)

    async def delete_one(self, id: int) -> None:
        await self.category_repo.delete_one(id)
    
    async def universal_table(self) -> UniversalTable:
        products = await self.category_repo.get_all()
        return UniversalTable.from_instances(products, TABLE_SCHEMA)