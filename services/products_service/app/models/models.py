from sqlalchemy.orm import Mapped, mapped_column, relationship, declarative_base
from sqlalchemy import ForeignKey, text, String, Numeric, Integer, DateTime, func
from datetime import datetime
from decimal import Decimal

Base = declarative_base()

class Category(Base):
    __tablename__ = "categories"
    
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(80), unique=True, nullable=False)
    
    products: Mapped[list["Product"]] = relationship(
        back_populates="category"
    )
    
    def __repr__(self) -> str:
        return f"<Category id={self.id} name={self.name!r}>"

    
class Product(Base):
    __tablename__ = "products"
    
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(120), nullable=False)
    price: Mapped[float] = mapped_column(Numeric(10, 2), nullable=False)
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), server_default=text("TIMEZONE('utc', now())"), nullable=False)
    updated_at: Mapped[datetime] = mapped_column(DateTime(timezone=True),
                                                 server_default=text("TIMEZONE('utc', now())"),
                                                 onupdate=func.now(),
                                                 nullable=False)
    
    category_id: Mapped[int] = mapped_column(ForeignKey("categories.id", ondelete="CASCADE"))
    
    category: Mapped["Category"] = relationship(
        back_populates="products"
    )
    
    def __repr__(self) -> str:
        return f"<Product id={self.id} name={self.name!r} price={self.price}>"
