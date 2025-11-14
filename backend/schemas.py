from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class TaskBase(BaseModel):
    title: str
    description: Optional[str] = None
    priority: str = 'medium'

class TaskCreate(TaskBase):
    pass

class Task(TaskBase):
    id: int
    completed: bool = False
    created_at: datetime

    class Config:
        orm_mode = True
