from models.common.base import create_table_all
from config.db_config import engine_sqlite

def set_test_data():
  create_table_all(engine_sqlite)
