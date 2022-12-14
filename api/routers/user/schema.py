from typing import List
from pydantic import BaseModel, Field

class User(BaseModel):
  id: int = Field(description="id")
  name: str = Field(description="ユーザー名")
  age: int = Field(description="年齢")

class UserList(BaseModel):
  user_list: List[User] = Field(description="ユーザーリスト")
