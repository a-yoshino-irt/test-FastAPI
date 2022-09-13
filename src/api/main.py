from urllib.request import Request
from fastapi import  FastAPI
from fastapi.responses import JSONResponse
from routers.common.response_message import ResponseMessage
from routers.common.response_code import ResponseCode
from routers.common.schema import Response

from routers import set_router

app = FastAPI()

set_router(app)


@app.middleware("http")
async def http_request(request: Request, call_next):
    try:
        response = await call_next(request)
        response.headers["X-Frame-Options"] = "Deny"
        return response
    except BaseException as e:
        print(e)
        body = Response(result_cd=ResponseCode.SYSTEM_ERROR, message=ResponseMessage.SYSTEM_ERROR).__dict__
        return JSONResponse(status_code=500, content=body)
