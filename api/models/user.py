# from sqlalchemy.dialects.postgresql import TIMESTAMP, UUID, VARCHAR
from sqlalchemy.dialects.sqlite import TIMESTAMP, VARCHAR, TEXT
from sqlalchemy import Column
from models.common.base import Base
from models.common.datetime import JstNow


class User(Base):
    __tablename__ = "t_user"

    id = Column(TEXT, nullable=False, primary_key=True)
    name = Column(VARCHAR(8), nullable=False, primary_key=True)
    created_at = Column(TIMESTAMP, nullable=False, server_default=JstNow())
