# Task Tracker API

A RESTful task tracker API built with FastAPI, SQLModel and Python that supports CRUD operations for tasks stored in PostgreSQL.


## Overview
This project is a backend-focused API for managing tasks. It allows clients to create, read, update, and delete tasks.
The goal of this project was to practice backend development fundamentals including route design, request validation, database integration, CRUD operations, and building an API that can be tested through Swagger UI, Postman, or another frontend client.

## Features
- Create new tasks
- Read all tasks
- Read a task by ID
- Update existing tasks
- Delete tasks
- Automatic interactive API documentation with FastAPI
- 
## Tech Stack
- Python
- FastAPI
- SQLModel
- PostgreSQL

## API Endpoints
- `POST /tasks` — create a new task
- `GET /tasks` — get all tasks
- `GET /tasks/{id}` — get a task by id
- `PUT /tasks/{id}` — update a task
- `DELETE /tasks/{id}` — delete a task

## How It Works
The API receives HTTP requests, validates incoming data with FastAPI and SQLModel models, performs database operations through a SQLModel session, and returns JSON responses. PostgreSQL stores the task records permanently, while FastAPI handles routing and automatic documentation.

## Run Locally
1. Clone the repository:
```bash
git clone https://github.com/SalsaBandit/Task-tracker-api.git
cd task-tracker-api
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Set your database connection string.

5. Run the server:
```bash
uvicorn main:app --reload
```

## Project Structure
```bash
task-tracker-api/
├── main.py
├── .gitignore
├── pyproject.toml
├── requirements.txt
└── README.md
```

## Challenges and Learnings
This project helped build a stronger understanding of how APIs accept data, validate it, and persist it in a relational database. It also helped reinforce the difference between table models and request/response schemas in FastAPI and SQLModel.

A useful lesson from this project was learning how sessions work in SQLModel, especially the purpose of `add()`, `commit()`, and `refresh()` when creating or updating rows. 

## Future Improvements
- Add authentication and user-specific task ownership
- Add due dates and task priorities
- Add filtering by completion status
- Add automated tests

## Author
Avi Aaron Batchu
