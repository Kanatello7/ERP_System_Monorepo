from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .api.products import router as products_router 
from .api.category import router as category_router
from .core.config import settings

app = FastAPI(title="Product-Service")

app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.all_cors_origins,
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE", "OPTIONS"],
    allow_headers=["*"],
    
)

app.include_router(products_router)
app.include_router(category_router)


