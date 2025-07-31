from fastapi import APIRouter, Depends, HTTPException, status

from app.schemas.schemas import ProductAdd, ProductRead, ProductUpdate
from .dependencies import products_service
from app.services.products import ProductsService
from shared_lib.universal_table import UniversalTable

from typing import Annotated

router = APIRouter(prefix="/products", tags=["products"])
ProductsServiceDep = Annotated[ProductsService, Depends(products_service)]

@router.get("/table", response_model=UniversalTable)
async def products_table(service: ProductsServiceDep):
    return await service.universal_table()


@router.get("", response_model=list[ProductRead])
async def list_products(service: ProductsServiceDep):
    return await service.get_all()

@router.post("", response_model=ProductRead, status_code=status.HTTP_201_CREATED)
async def add_product(product: ProductAdd, service: ProductsServiceDep):
    return await service.add_one(product)

@router.get("/{product_id}", response_model=ProductRead)
async def get_product(product_id: int, service: ProductsServiceDep):
    product = await service.get_one(product_id)
    if not product:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail="Product not found by id")
    return product
    

@router.put("/{product_id}", response_model=ProductRead)
async def update_product(product_id: int, new_product: ProductUpdate, service: ProductsServiceDep):
    updated = await service.update_one(product_id, new_product)
    if not updated:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail="Product not found by id")
    return updated
    
@router.delete("/{product_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_product(product_id: int, service: ProductsServiceDep):
    await service.delete_one(product_id)

