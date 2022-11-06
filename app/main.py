from fastapi import FastAPI, APIRouter
from app.random_string import router as random_string_router

app = FastAPI()
router = APIRouter()
router.include_router(random_string_router)
app.include_router(router)

