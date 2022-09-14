from routers.common.schema import Response
from routers.user.schema import User, UserList
from repository import user
from sqlalchemy.orm import Session

def get_user_list(session: Session):
  user_list = user.select_all(session)
  return Response(data = UserList(
    user_list=[
      User(id=user.id,name=user.name,age=user.age) for user in user_list
    ]
  ))