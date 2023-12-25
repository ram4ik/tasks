from fastapi import FastAPI
from fastapi import APIRouter

from task import task_router

app = FastAPI()
router = APIRouter()

@router.get('/hello')
async def hello_world():
    return {'hello': 'world'}

app.include_router(router)
app.include_router(task_router)
app.include_router(task_router, prefix="/tasks")