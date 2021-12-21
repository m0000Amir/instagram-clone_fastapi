from fastapi import APIRouter
from fastapi.param_functions import Depends
from sqlalchemy.orm.session import Session
from routers.shemas import UserBase, UserDisplay
from db.database import get_db
from db.db_user import create_user
from db import db_user

router = APIRouter(
    prefix="/user",
    tags=["user"]
)


@router.post("", response_model=UserDisplay)
def create_user(request: UserBase, db: Session = Depends(get_db)):
    return  db_user.create_user(db, request)
