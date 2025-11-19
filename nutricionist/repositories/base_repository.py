from tinydb import table
from nutricionist.database.engine import Engine

class BaseRepository:
  def get_table(self, table_name: str) -> table.Table:
    return self.db.table(table_name)