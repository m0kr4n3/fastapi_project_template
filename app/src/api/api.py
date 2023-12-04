from src.api.endpoints import login, users, items
from fastapi import FastAPI, APIRouter
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

root_router = APIRouter()

@root_router.get("/")
def root():
    return {"message": "welcome! go to /docs for API documentation."}

api_router.include_router(root_router,  tags=["root"])
api_router.include_router(login.router, prefix='/login', tags=["login"])
api_router.include_router(users.router, prefix="/users", tags=["users"])
api_router.include_router(items.router, prefix="/items", tags=["items"])