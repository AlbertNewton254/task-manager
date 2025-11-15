from fastapi import FastAPI, Depends, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from schemas import Task, TaskCreate
from datetime import datetime
import models
from database import engine, get_db

# Create database tables
models.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=['http://localhost:3000'],
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*']
)

@app.get('/')
def read_root():
    return {'message': 'Task Manager API is running!'}

@app.get('/health')
def health_check():
    return {'status': 'healthy', 'version': '1.0.0'}

@app.get('/tasks', response_model=list[Task])
def get_tasks(db: Session = Depends(get_db)):
    return db.query(models.Task).all()

@app.post('/tasks', response_model=Task)
def create_task(task: TaskCreate, db: Session = Depends(get_db)):
    new_task = models.Task(
        title=task.title,
        description=task.description,
        priority=task.priority
    )
    
    db.add(new_task)
    db.commit()
    db.refresh(new_task)
    
    return new_task

@app.put('/task/{task_id}', response_model=Task)
def update_task(task_id: int, task_update: TaskCreate, db: Session = Depends(get_db)):
    task = db.query(models.Task).filter(models.Task.id == task_id).first()
    
    if not task:
        raise HTTPException(status_code=404, detail='Task not found')
    
    task.title = task_update.title
    task.description = task_update.description
    task.priority = task_update.priority
    
    db.commit()
    db.refresh(task)
    
    return task

@app.patch("/tasks/{task_id}/complete", response_model=Task)
def toggle_task_completion(task_id: int, db: Session = Depends(get_db)):
    task = db.query(models.Task).filter(models.Task.id == task_id).first()
    
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    
    task.completed = not task.completed
    
    db.commit()
    db.refresh(task)
    
    return task

@app.delete("/tasks/{task_id}")
def delete_task(task_id: int, db: Session = Depends(get_db)):
    task = db.query(models.Task).filter(models.Task.id == task_id).first()
    
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    
    db.delete(task)
    db.commit()
    
    return {"message": "Task deleted successfully"}
