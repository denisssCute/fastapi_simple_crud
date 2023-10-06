import uvicorn #веб сервер для запуска приложения
from fastapi import FastAPI #импорт класса FastAPI для создания web-приложения

from users.views import routerUsers
from admins.views import routerAdmins

from db.database import engine, SessionLocal,Base
Base.metadata.create_all(bind=engine)

app = FastAPI(title="Create Read Updtae Delete приложение")

app.include_router(routerUsers, tags=['Users'])
app.include_router(routerAdmins, tags=['Admins'])

@app.get("/") #когда в приложение приходит get запрос на эндпоинт "/", мы даём приложению знать что надо его обработать
def hello():
    return {
        'message' : 'Hello 100% World !'
    }

if __name__ == "__main__":
    uvicorn.run(app="main:app", reload=True)