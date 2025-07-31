from sqlalchemy.orm import Mapped, mapped_column, declarative_base
from sqlalchemy import text, String, Integer, DateTime
from datetime import datetime

Base = declarative_base()

class Customer(Base):
    __tablename__ = "customers"
    
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    first_name: Mapped[str] = mapped_column(String(150), nullable=False)
    last_name: Mapped[str] = mapped_column(String(150),nullable=False)
    email: Mapped[str] = mapped_column(String(150), unique=True, nullable=False)
    phone: Mapped[str] = mapped_column(String(30), unique=True, nullable=True)
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), server_default=text("TIMEZONE('utc', now())"), nullable=False)
    updated_at: Mapped[datetime] = mapped_column(DateTime(timezone=True),
                                                 server_default=text("TIMEZONE('utc', now())"),
                                                 onupdate=datetime.utcnow,
                                                 nullable=False)
    
    def __repr__(self) -> str:
        return f"<Customer {self.id=} {self.email=}>"