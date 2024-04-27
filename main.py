from src.engine import Engine
from consts import SQLiteDBConsts, APIConsts


if __name__ == "__main__":
  db_configurations = SQLiteDBConsts().get_database_configurations()
  api_configurations = APIConsts().get_api_configurations()
  engine = Engine(
    db_configurations=db_configurations,
    api_configurations=api_configurations
  )
  response = engine.run()
  if response["status"] == "error":
    print(response)