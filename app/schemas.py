import uuid
from decimal import Decimal

from pydantic import BaseModel, ConfigDict


class WalletResponse(BaseModel):
    id: uuid.UUID
    balance: Decimal

    model_config = ConfigDict(from_attributes=True)
