import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# postgresql
PG_DATABASE_URL = os.environ.get("POSTGRES_DATABASE_URL", "")

engine_pg = create_engine(
    PG_DATABASE_URL
)
sessionPostgres = sessionmaker(autocommit=False, autoflush=False, bind=engine_pg)


SQLITE_DATABASE_URL = os.environ.get("SQLITE_DATABASE_URL", "")

# sqlite
engine_sqlite = create_engine(
    SQLITE_DATABASE_URL
)
sessionSQLite = sessionmaker(autocommit=False, autoflush=False, bind=engine_sqlite)

# common
def get_session(test_flg: bool = False):
  if test_flg:
    return sessionSQLite
  else:
    return sessionPostgres
