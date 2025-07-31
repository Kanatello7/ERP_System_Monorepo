from .utils import SQLAlchemyRepository
from ..models.models import Customer

class CustomerRepository(SQLAlchemyRepository):
    model = Customer