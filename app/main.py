from fastapi import FastAPI

from app.routes import router as wallet_router

app = FastAPI(
    title="wallet-app",
    description="A simple wallet application",
    version="0.1.0",
)


@app.get("/health", tags=["health check"])
async def health_check():
    return {"status": "ok"}


app.include_router(wallet_router)
