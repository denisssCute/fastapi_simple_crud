from pydantic import BaseModel #базовая модель для валидации данных, на её основе можно создавать
from pydantic import EmailStr

class CreateUser(BaseModel):
    id : int
    email : EmailStr
    username: str