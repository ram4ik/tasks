from fastapi import APIRouter

from models import StatusType

task_router = APIRouter()
task_list = []

@task_router.get('/')
async def get():
    return {'tasks': task_list}

@task_router.post('/{task}')
async def add(task: str):
    task_list.append({
        "task": task,
        "status": StatusType.PENDING,
    })
    return {'tasks': task_list}

@task_router.put('/')
async def update(index: int, task: str, status: StatusType):
    task_list[index] = {
        "task": task,
        "status": status,
    }
    return {'tasks': task_list}

@task_router.delete('/')
async def delete(index: int):
    del task_list[index]
    return {'tasks': task_list}
