import uuid
from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession

from app.db import get_session
from app.models import Wallet
from app.schemas import WalletResponse

SessionDep = Annotated[AsyncSession, Depends(get_session)]

router = APIRouter(prefix="/api/v1/wallets")


@router.post("", status_code=status.HTTP_201_CREATED, response_model=WalletResponse)
async def create_wallet(session: SessionDep):
    wallet = Wallet()
    session.add(wallet)
    await session.commit()
    return wallet


@router.get("/{wallet_id}", response_model=WalletResponse)
async def get_wallet(wallet_id: uuid.UUID, session: SessionDep):
    wallet = await session.get(Wallet, wallet_id)
    if wallet is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Wallet not found"
        )
    return wallet
