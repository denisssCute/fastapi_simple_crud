from fastapi import APIRouter

from admins import crud

routerAdmins = APIRouter(prefix="/admins") # создаём и импортируем так называемый роутер для того,
                                    # чтобы обрабатывать определённые типы запросов. В данном модуле находится
                                    # всё что связано с admins


@routerAdmins.get("/all")
def show_admins():
    return crud.all()