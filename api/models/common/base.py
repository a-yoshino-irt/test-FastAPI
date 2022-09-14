from typing import Any
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


def create_table_all(engine: Any):
  Base.metadata.create_all(bind=engine, checkfirst=False)