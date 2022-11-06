from fastapi import FastAPI, APIRouter
from random_string import router as random_string_router
from health import router as health_router

app = FastAPI()
router = APIRouter()
router.include_router(random_string_router)
router.include_router(health_router)
app.include_router(router)
