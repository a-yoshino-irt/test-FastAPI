from urllib import response
from fastapi import APIRouter
from routers.common.schema import Response, ResponseCode
from routers.user.schema import UserGet

router = APIRouter()

@router.get(
    "",
    response_model=Response[UserGet],
    response_model_exclude=["debug_message"]
)
def get_user(
):
    resp = Response(result_cd=ResponseCode.OK)
    return resp