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