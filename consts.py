import configparser


class SQLiteDBConsts:
  """
  SQLite database constants
  """


  def __init__(self) -> None:
    self.config_parser = configparser.ConfigParser()
    self.config_parser.read("config.ini")
  

  def get_database_configurations(self) -> dict:
    """
    Provides the database configurations
    
    Args:
      None
    
    Returns:
      dict: provides the necessary database configurations
    """
    
    database_configurations = self.config_parser["BOOKSDB"]
    return database_configurations


class APIConsts:
  """
  API constants
  """


  def __init__(self) -> None:
    self.config_parser = configparser.ConfigParser()
    self.config_parser.read("config.ini")
  

  def get_api_configurations(self) -> dict:
    """
    Provides the API configurations
    
    Args:
      None
    
    Returns:
      dict: provides the necessary API configurations
    """
    
    api_configurations = self.config_parser["OPENLIBRARYAPI"]
    return api_configurations