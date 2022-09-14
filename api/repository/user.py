from sqlalchemy.orm import Session

from models.user import User

def select(session: Session, id: int):
  return session.query(User).filter(User.id == id).one_or_none()

def select_all(session: Session):
  return session.query(User).all()

def insert(session: Session, user: User):
  session.add(user)
  session.flush()
  
  return user
  
def delete(session: Session, id: int):
  session.query(User).filter(User.id == id).delete()
  session.flush()
