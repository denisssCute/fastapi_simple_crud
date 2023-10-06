from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from users import crud
from users.schemas import CreateUser
from db.database import get_db

routerUsers = APIRouter(prefix="/users") # создаём и импортируем так называемый роутер для того,
                                    # чтобы обрабатывать определённые типы запросов. В данном модуле находится
                                    # всё что связано с users

@routerUsers.get('/hello')
async def print_hello(name : str = "World!"):
    return crud.hello(name_u=name)

@routerUsers.post('/create')
async def create_user(user : CreateUser, db: Session = Depends(get_db)):
    return crud.create_user(user, db)

@routerUsers.get('/all')
async def get_all(db: Session = Depends(get_db)):
    return crud.get_all(db)

@routerUsers.put(f'/update/{id}/')
async def update_user(user : CreateUser, db: Session = Depends(get_db)):
    return crud.update_user(user, db)

@routerUsers.delete(f'/delete/{id}/')
async def delete_user(user_id : int, db: Session = Depends(get_db)):
    return crud.delete_user(user_id, db)