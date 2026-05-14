from typing import Annotated
from fastapi import FastAPI, Depends, HTTPException, Query 
from sqlmodel import Field, SQLModel, Session, create_engine, select

#postgresql://[user]@[host]:[port]/[database_name]
DATABASE_URL = "postgresql://avi@localhost:5432/avi"
engine = create_engine(DATABASE_URL)

class task (SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    title: str
    description: str | None = None
    status: str

class taskCreate(SQLModel):
    title: str
    description: str | None = None
    status: str

def create_tables():
    SQLModel.metadata.create_all(engine)

def get_session():
    with Session(engine) as session:
        yield session

SessionDep = Annotated[Session, Depends(get_session)]

app = FastAPI()

@app.on_event("startup")
def on_startup():
    create_tables()

@app.get("/")
async def read_root():
    return {"message": "Welcome to the Task Tracker API please navigate to /docs for API documentation"}

@app.post("/taskscreate")
async def create_task(task_data: taskCreate, session: SessionDep):
    db_task = task.model_validate(task_data)
    session.add(db_task)
    session.commit()
    session.refresh(db_task)
    return db_task

@app.get("/tasks")
def read_tasks(session: SessionDep):
    tasks = session.exec(select(task)).all()
    return tasks
@app.get("/tasks/{task_id}")
def read_task(task_id: int, session: SessionDep):
    task_item = session.get(task, task_id)
    return task_item

@app.put("/tasks/{task_id}")
def update_task(task_id: int, task_data: taskCreate, session: SessionDep):
    task_item = session.get(task, task_id)
    if not task_item:
        raise HTTPException(status_code=404, detail="Task not found")
    task_item.title = task_data.title
    task_item.description = task_data.description
    task_item.status = task_data.status
    session.add(task_item)
    session.commit()
    session.refresh(task_item)
    return task_item

@app.delete("/tasks/{task_id}")
def delete_task(task_id: int, session: SessionDep):
    task_item = session.get(task, task_id)
    if not task_item:
        raise HTTPException(status_code=404, detail="Task not found")
    session.delete(task_item)
    session.commit()
    return {"message": "Task deleted successfully"}

@app.get("/tasks/{status}")
def sort_tasks(status: str, session: SessionDep):
    tasks = session.exec(select(task).where(task.status == status)).all()
    return tasks