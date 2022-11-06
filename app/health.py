from fastapi import APIRouter

router = APIRouter()


@router.get("/health")
async def read_root():
    return {"code": 200, "success": True}
