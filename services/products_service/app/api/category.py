from fastapi import APIRouter, Depends, HTTPException, status

from app.schemas.schemas import CategoryAdd, CategoryRead
from app.services.category import CategoryService
from .dependencies import category_service
from shared_lib.universal_table import UniversalTable

from typing import Annotated

router = APIRouter(prefix="/category", tags=['category'])
CategoryServiceDep = Annotated[CategoryService, Depends(category_service)]

@router.get("/table", response_model=UniversalTable)
async def category_table(service: CategoryServiceDep):
    return await service.universal_table()

@router.get("", response_model=list[CategoryRead])
async def list_categories(service: CategoryServiceDep):
    return await service.get_all()

@router.post("", response_model=CategoryRead, status_code=status.HTTP_201_CREATED)
async def add_category(category: CategoryAdd, service: CategoryServiceDep):
    return await service.add_one(category)

@router.get("/{category_id}", response_model=CategoryRead)
async def get_category(category_id: int, service: CategoryServiceDep):
    category = await service.get_one(category_id) 
    if not category:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail="Category not found by id")
    return category


@router.delete("/{category_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_category(category_id: int, service: CategoryServiceDep):
    await service.delete_one(category_id)

