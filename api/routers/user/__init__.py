from fastapi import APIRouter
from config.db_config import get_session
from service.user import get_user_list
from routers.common.schema import Response
from routers.user.schema import User

router = APIRouter()

@router.get(
    "",
    response_model=Response[User],
    response_model_exclude=["debug_message"]
)
def get_user(
):
    try:
        session = get_session()
        resp = get_user_list(session)
        return resp
    finally:
        session.close()
        