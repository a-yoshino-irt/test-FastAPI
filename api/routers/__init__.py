from fastapi import FastAPI
from routers import user

def set_router(app: FastAPI):
  app.include_router(user.router, prefix="/user", tags=["User"])
