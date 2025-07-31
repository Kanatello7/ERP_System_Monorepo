from abc import ABC, abstractmethod
from sqlalchemy import select, insert, delete, update
from sqlalchemy.exc import IntegrityError

from app.core.database import async_session_maker, AsyncSession
from .exceptions import DuplicateKeyError


class AbstractRepository(ABC):
 
    @abstractmethod
    async def get_one(self):
        raise NotImplementedError
    
    @abstractmethod
    async def get_all(self):
        raise NotImplementedError
    
    @abstractmethod
    async def add_one(self):
        raise NotImplementedError
    
    @abstractmethod
    async def update_one(self):
        raise NotImplementedError
    
    @abstractmethod
    async def delete_one(self):
        raise NotImplementedError

class SQLAlchemyRepository(AbstractRepository):
    model = None

    def __init__(self, session: AsyncSession):
        self.session = session

    async def get_one(self, id: int):
        return await self.session.get(self.model, id)

    async def get_all(self):
        res = await self.session.execute(select(self.model))
        return res.scalars().all()

    async def add_one(self, data: dict):
        obj = self.model(**data)
        self.session.add(obj)
        try:
            await self.session.commit()
            
        except IntegrityError as exc:
            await self.session.rollback()
            raise DuplicateKeyError from exc
        
        await self.session.refresh(obj)
        return obj 

    async def update_one(self, id: int, data: dict):
        obj = await self.session.get(self.model, id)
        if not obj:
            return None

        for k, v in data.items():
            setattr(obj, k, v)

        try:
            await self.session.commit()
        except IntegrityError as exc:
            await self.session.rollback()
            raise DuplicateKeyError from exc

        await self.session.refresh(obj)
        return obj

    async def delete_one(self, id: int):
        await self.session.execute(delete(self.model).where(self.model.id == id))
        await self.session.commit()
