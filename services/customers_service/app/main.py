from fastapi import FastAPI, Request, status
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware

from .api.customer import router as customer_router 
from .core.config import settings
from .repositories.exceptions import DuplicateKeyError

app = FastAPI(title="Customer-Service")

app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.all_cors_origins,
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE", "OPTIONS"],
    allow_headers=["*"],
    
)

app.include_router(customer_router)

@app.exception_handler(DuplicateKeyError)
async def duplicate_key_handler(_: Request, exc: DuplicateKeyError):
    return JSONResponse(
        status_code=status.HTTP_409_CONFLICT,
        content={"detail": "Unique constraint violation"},
    )

