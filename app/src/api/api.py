from src.api.endpoints import login, users
from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware
from src.core.config import settings

api_router = FastAPI()

# Set all CORS enabled origins
if settings.BACKEND_CORS_ORIGINS:
    api_router.add_middleware(
        CORSMiddleware,
        allow_origins=[str(origin) for origin in settings.BACKEND_CORS_ORIGINS],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )
api_router.include_router(login.router, tags=["login"])
api_router.include_router(users.router, prefix="/users", tags=["users"])