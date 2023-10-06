from fastapi import APIRouter

routerHr = APIRouter(prefix="/hr") # создаём и импортируем так называемый роутер для того,
                                    # чтобы обрабатывать определённые типы запросов. В данном модуле находится
                                    # всё что связано с hr

@routerHr.get("/junior/")
def show_latest_hr():
    return {'name' : 'Nastya'}

@routerHr.get("/{id}/")
def show_hr(id: int):
    hr = {1:'Maria', 2:'Nastya'}
    return {
        "id" : id,
        'name' : hr[id]
    }