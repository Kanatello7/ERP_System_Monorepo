from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .api.customer import router as customer_router 
from .core.config import settings

app = FastAPI(title="Customer-Service")

app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.all_cors_origins,
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE", "OPTIONS"],
    allow_headers=["*"],
    
)

app.include_router(customer_router)



