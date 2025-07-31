from .utils import SQLAlchemyRepository
from app.models.models import Product

class ProductsRepository(SQLAlchemyRepository):
    model = Product