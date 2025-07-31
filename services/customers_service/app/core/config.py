from pydantic_settings import BaseSettings, SettingsConfigDict
from pathlib import Path

class Settings(BaseSettings):
    DB_HOST: str 
    DB_PORT: str    
    DB_USER: str 
    DB_PASSWORD: str 
    DB_NAME: str 
    
    @property
    def DATABASE_URL(self):
        return f"postgresql+asyncpg://{self.DB_USER}:{self.DB_PASSWORD}@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}"
    
  
    
    CORS_ORIGINS: str 
    
    @property
    def all_cors_origins(self):
        return [origin for origin in self.CORS_ORIGINS.split(",")]
        
    model_config = SettingsConfigDict(
        env_file=str(Path(__file__).resolve().parent / ".env"),  # /app/app/.env
        env_file_encoding="utf-8",
    )

settings = Settings()
print(settings.all_cors_origins)