from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException, status 

from .dependencies import customer_service
from ..services.customer import CustomerService
from ..schemas.schemas import CustomerAdd, CustomerUpdate, CustomerRead
from shared_lib.universal_table import UniversalTable

router = APIRouter(prefix="/customers", tags=['customers'])
CustomerServiceDep = Annotated[CustomerService, Depends(customer_service)]

@router.get("/table", response_model=UniversalTable)
async def customers_table(service: CustomerServiceDep):
    return await service.universal_table()


@router.get("", response_model=list[CustomerRead])
async def list_customers(service: CustomerServiceDep):
    return await service.get_all()

@router.post("", response_model=CustomerRead, status_code=status.HTTP_201_CREATED)
async def add_customer(customer: CustomerAdd, service: CustomerServiceDep):
    return await service.add_one(customer)

@router.get("/{customer_id}", response_model=CustomerRead)
async def get_customer(customer_id: int, service: CustomerServiceDep):
    customer = await service.get_one(customer_id)
    if not customer:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail="Customer not found by id")
    return customer
    

@router.put("/{customer_id}", response_model=CustomerRead)
async def update_customer(customer_id: int, new_customer: CustomerUpdate, service: CustomerServiceDep):
    updated = await service.update_one(customer_id, new_customer)
    if not updated:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail="Customer not found by id")
    return updated
    
@router.delete("/{customer_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_customer(customer_id: int, service: CustomerServiceDep):
    await service.delete_one(customer_id)
