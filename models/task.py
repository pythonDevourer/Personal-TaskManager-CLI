from pydantic import BaseModel, Field
from itertools import count

id_gen = count(1)

class Task(BaseModel):
    id: int = Field(title="Task Id", description="unique identifier for tasks", default_factory=lambda: next(id_gen))
    name: str = Field(title="Task name", description="name for the task")
    