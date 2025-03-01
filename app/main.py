from fastapi import FastAPI
from app.api.routes import router as api_router
from app.models import Base
from app.databases import engine

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(api_router, prefix="/api")