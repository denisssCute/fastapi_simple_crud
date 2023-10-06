from sqlalchemy import select
from sqlalchemy import update

from db.models import Colleagues
from users.schemas import CreateUser
from sqlalchemy.orm import Session

def print_hello(name_u):
    return {
        'message' : f"Hello {name_u}"
    }

def create_user(user_in : CreateUser, db: Session):
    user = Colleagues(username=user_in.username, email=user_in.email)
    flag = 0
    try:
        db.add(user)
        db.commit()
        db.refresh(user)
        flag = 1
    except Exception as e:
        print(e)

        return user
    finally:
        if flag:
            return {
                'succes': 1
            }

def get_all(db: Session):
    all = {}
    users = db.query(Colleagues).all()
    i = 1
    for user in users:
        all["user"+str(i)] = {
            "id" : user.id,
            "username" : f"{user.username}"
          , "email" : f"{user.email}"
        }
        i += 1
    return all

def update_user(user : CreateUser, db : Session):
    flag = 0
    try:
        stmt = update(Colleagues).where(Colleagues.id == int(user.id)).values(username=user.username, email=user.email)
        db.execute(stmt)
        db.commit()
        flag = 1
    except Exception as e:
        print(e)
    return {'succes': flag}

def delete_user(id: CreateUser, db : Session):
    flag = 0
    try:
        user_to_delete = db.query(Colleagues).filter_by(id=id).first()
        db.delete(user_to_delete)
        db.commit()
        flag = 1
    except Exception as e:
        print(e)

    return {
        'succes': flag
    }