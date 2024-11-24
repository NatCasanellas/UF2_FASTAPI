from sqlalchemy.orm import Session
from app.schemas.user import UserOut
from app.db_connect.connection import SessionLocal
from app.schemas.user import User

def get_users(db: Session):
    return db.query(User).all()