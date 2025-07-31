from fastapi import FastAPI, Request, status
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse

from .api.products import router as products_router 
from .api.category import router as category_router
from .core.config import settings
from app.repositories import DuplicateKeyError

app = FastAPI(title="Product-Service")

app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.all_cors_origins,
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE", "OPTIONS"],
    allow_headers=["*"],
    
)
@app.exception_handler(DuplicateKeyError)
async def duplicate_key_handler(_: Request, exc: DuplicateKeyError):
    return JSONResponse(
        status_code=status.HTTP_409_CONFLICT,
        content={"detail": "Unique constraint violation"},
    )

app.include_router(products_router)
app.include_router(category_router)


