import re
import sqlite3


class DBUtilities:
  """
  It contians the generic utility functions for the database that can be used by other classes
  """


  def __init__(self, 
               connection: sqlite3.Connection) -> None:
    self.connection = connection
  

  def execute_query(
      self,
      query: str,
      description_about_query: str) -> dict:
    """
    It is responsible for executing the query and providing the description about the query
    
    Args:
      query (str): query to be executed
      description_about_query (str): description about the query
    
    Returns:
      dict: provides the status, description, query and result of the query
    """
    
    try:
      query = re.sub(' +', ' ', query.replace("\n", "").replace("\t", "").strip())
      cursor = self.connection.cursor()
      result = cursor.execute(query)
      self.connection.commit()

      format_query_result = {
      "status": "success",
      "description": description_about_query,
      "query": query,
      "result": result
    }
      
    except sqlite3.Error as sql_error:
      format_query_result = {
        "status": "error",
        "error_code": sql_error.args[0],
        "description": description_about_query,
        "query": query,
        "result": str(sql_error)
      }

    finally:
      return format_query_result