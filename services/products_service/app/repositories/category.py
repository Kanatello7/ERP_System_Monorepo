from .utils import SQLAlchemyRepository
from app.models.models import Category

class CategoryRepository(SQLAlchemyRepository):
    model = Category
    
    async def update_one(self, id, data):
        raise NotImplementedError