from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from schemas import Task, TaskCreate
from datetime import datetime
from fastapi import HTTPException

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=['http://localhost:3000'],
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*']
)

tasks_db = []
task_id_counter = 1

@app.get('/')
def read_root():
    return {'message': 'Task Manager API is running!'}

@app.get('/health')
def health_check():
    return {'status': 'healthy', 'version': '1.0.0'}

@app.get('/tasks', response_model=list[Task])
def get_tasks():
    return tasks_db

@app.post('/tasks', response_model=Task)
def create_task(task: TaskCreate):
    global task_id_counter

    new_task = Task(
        id=task_id_counter,
        title=task.title,
        description=task.description,
        priority=task.priority,
        completed=False,
        created_at=datetime.now()
    )

    tasks_db.append(new_task)
    task_id_counter += 1

    return new_task

@app.put('/task/{task_id}', response_model=Task)
def update_task(task_id: int, task_update=TaskCreate):
    for i, task in enumerate(tasks_db):
        if task.id == task_id:
            update_task = Task(
                id=task.id,
                title=task_update.title,
                description=task_update.description,
                priority=task_update.priority,
                completed=tasks_db[i].completed,
                created_at=tasks_db[i].created_at
            )
            tasks_db[i] = updated_task
            return update_task
    raise HTTPException(status_code=404, detail='Task not found')

@app.delete("/tasks/{task_id}")
def delete_task(task_id: int):
    global tasks_db

    task_exists = any(task.id == task_id for task in tasks_db)

    if not task_exists:
        raise HTTPException(status_code=404, detail="Task not found")

    tasks_db = [task for task in tasks_db if task.id != task_id]
    return {"message": "Task deleted successfully"}
