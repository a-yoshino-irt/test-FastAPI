import json
from typing import Generic, Optional, TypeVar
from pydantic import BaseModel, Field

from routers.common.response_code import ResponseCode
from routers.common.response_message import ResponseMessage

T = TypeVar('T')
class Response(BaseModel, Generic[T]):
  result_cd: ResponseCode = Field(description="結果コード")
  message: Optional[ResponseMessage] = Field(description="メッセージ")
  data: Optional[T] = Field(description="返却データ")
