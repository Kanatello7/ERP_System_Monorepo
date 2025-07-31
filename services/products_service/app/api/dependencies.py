from typing import Annotated
from fastapi import Depends
from app.core.database import get_session, AsyncSession
from app.repositories.category import CategoryRepository
from app.repositories.products import ProductsRepository
from app.services.category import CategoryService
from app.services.products import ProductsService


async def products_repo(
    session: Annotated[AsyncSession, Depends(get_session)]
) -> ProductsRepository:
    return ProductsRepository(session)

async def category_repo(
    session: Annotated[AsyncSession, Depends(get_session)]
) -> CategoryRepository:
    return CategoryRepository(session)

def products_service(
    repo: Annotated[ProductsRepository, Depends(products_repo)]
) -> ProductsService:
    return ProductsService(repo)

def category_service(
    repo: Annotated[CategoryRepository, Depends(category_repo)]
) -> CategoryService:
    return CategoryService(repo)