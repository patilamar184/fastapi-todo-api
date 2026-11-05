from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from . import models, schemas, crud
from .database import engine, get_db
models.Base.metadata.create_all(bind=engine)

app = FastAPI(title = "Todo api")

@app.get("/")
def root():
    return {
        "message":"todo app running"
    }

@app.post("/todos", response_model=schemas.TodoResponse, status_code=201)
def create_todo(todo:schemas.TodCreate , db:Session = Depends(get_db)):
    return crud.create_todo(db=db, todo=todo)

@app.get("/todos", response_model=list[schemas.TodoResponse])
def read_todos(db: Session = Depends(get_db)):
    return crud.get_todos(db=db)

@app.get("todos/{todo_id}" , response_model=schemas.TodoResponse)
def read_todos(todo_id:int , db:Session = Depends(get_db)):
    db_todo = crud.get_todo(db=db , todo_id = todo_id)
    if not db_todo:
        raise HTTPException(status_code=404 , detail= "todo not found")
    return db_todo

@app.patch("/todos/{todo_id} , response_model = schemas.TodoResponse")
def update_todo(todo_id :int , todo:schemas.TodoUpdate ,db:Session = Depends(get_db)):
    db_todo= crud.update_todo(db=db , todo=todo , todo_id=todo_id)
    if not db_todo:
        raise HTTPException(status_code=404 , detail="todo not found")
    return db_todo

@app.delete("/todos/{todo_id}")
def delete_todo(todo_id:int , db:Session = Depends(get_db)):
    db_todo=crud.delete_todo(db=db , todo_id = todo_id)
    if not db_todo:
        raise HTTPException(status_code=404 , detail="todo not found")
    return {
        "message":"tod deleted"
    }




