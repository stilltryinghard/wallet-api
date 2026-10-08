import uuid
from decimal import Decimal

from sqlalchemy import CheckConstraint, Numeric
from sqlalchemy.orm import Mapped, mapped_column

from app.db import Base


class Wallet(Base):
    __tablename__ = "wallets"
    
    id: Mapped[uuid.UUID] = mapped_column(default=uuid.uuid4, primary_key=True)
    balance: Mapped[Decimal] = mapped_column(Numeric(precision=15, scale=2), default=Decimal(0))
    __table_args__ = (CheckConstraint('balance >= 0', name="check_balance_non_negative"),)