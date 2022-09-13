from pydantic import BaseModel, Field

class UserGet(BaseModel):
  id: int = Field(description="id")
  name: str = Field(description="ユーザー名")
  age: int = Field(description="年齢")