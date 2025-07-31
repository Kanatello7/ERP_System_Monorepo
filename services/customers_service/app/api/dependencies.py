from fastapi import Depends
from ..repositories.customer import CustomerRepository
from ..services.customer import CustomerService
from ..core.database import get_session, AsyncSession
from typing import Annotated


def customer_repo(session: Annotated[AsyncSession, Depends(get_session)]):
    return CustomerRepository(session)

def customer_service(repository: Annotated[CustomerRepository, Depends(customer_repo)]):
    return CustomerService(repository)