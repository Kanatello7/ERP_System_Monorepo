from typing import List
from app.schemas.schemas import ProductAdd, ProductUpdate, ProductRead
from app.repositories.utils import AbstractRepository
from shared_lib.universal_table import UniversalTable

TABLE_SCHEMA = {
    "id":         ("ID",        "number"),
    "name":       ("Product",   "string"),
    "price":      ("Price",     "number"),
    "created_at": ("Created",   "date"),
    "updated_at": ("Updated",   "date"),

}

class ProductsService:
    def __init__(self, repository: AbstractRepository):
        self.product_repo = repository

    async def get_all(self) -> List[ProductRead]:
        rows = await self.product_repo.get_all()
        return [ProductRead.model_validate(r) for r in rows]

    async def get_one(self, id: int) -> ProductRead | None:
        row = await self.product_repo.get_one(id)
        return ProductRead.model_validate(row) if row else None

    async def add_one(self, product: ProductAdd) -> ProductRead:
        row = await self.product_repo.add_one(product.model_dump())
        return ProductRead.model_validate(row)

    async def update_one(self, id: int, new_product: ProductUpdate) -> ProductRead | None:
        row = await self.product_repo.update_one(id, new_product.model_dump(exclude_unset=True))
        return ProductRead.model_validate(row) if row else None

    async def delete_one(self, id: int) -> None:
        await self.product_repo.delete_one(id)
    
    async def universal_table(self) -> UniversalTable:
        products = await self.product_repo.get_all()
        return UniversalTable.from_instances(products, TABLE_SCHEMA)