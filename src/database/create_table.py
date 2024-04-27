import sqlite3
from src.database.db_utilities import DBUtilities


class CreateTable:
  """
  It is responsible for creating the tables in the database
  """


  def __init__(self, 
               connection: sqlite3.Connection) -> None:
    self.db_utilities = DBUtilities(
      connection=connection
    )
  

  def execute(self) -> None:
    """
    It is responsible for creating the table in the database
    
    Args:
      None
    
    Returns:
      None
    """
    
    try:
      query_to_create_table = (
        """
        CREATE TABLE IF NOT EXISTS BOOKS (
          BOOKID VARCHAR(32) NOT NULL UNIQUE,
          TITLE VARCHAR(64) NOT NULL,
          AUTHOR VARCHAR(64),
          FIRST_PUBLISH_YEAR INT,

          CONSTRAINT BOOKS_PK
          PRIMARY KEY (BOOKID)
        );
        """
      )
      return self.db_utilities.execute_query(
        query=query_to_create_table,
        description_about_query="Creating table 'BOOKS'"
      )
    except sqlite3.Error as error:
      return {
        "status": "error",
        "error_code": error.args[0],
        "description": "Error while creating table",
        "query": query_to_create_table,
        "result": None
      }