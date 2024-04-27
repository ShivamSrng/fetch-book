import sqlite3
from prettytable import PrettyTable
from src.database.db_utilities import DBUtilities


class RetrieveData:
  """
  It is responsible for providing the functionality to retrieve the data from the database
  """


  def __init__(self, 
               connection: sqlite3.Connection) -> None:
    self.db_utilities = DBUtilities(
      connection=connection
    )
  

  def __tabulate_data(self,
                      attributes: list,
                      data: list) -> None:
    """
    It is responsible for tabulating the data
    
    Args:
      attributes (list): provides the attributes of the relation
      data (list): provides the data of the relation
    
    Returns:
      None
    """
    
    table = PrettyTable()
    table.field_names = attributes
    table.align = "l"

    for tuple in data:
      table.add_row(tuple)
    
    print(table)
  

  def execute(self) -> dict:
    """
    It is responsible for retrieving the data from the database
    
    Args:
      None
    
    Returns:
      dict: provides the status, description, query and result of the query
    """
    
    query_to_retrieve_data = (
      """
      SELECT * FROM BOOKS;
      """
    )

    books_data_response = self.db_utilities.execute_query(
      query=query_to_retrieve_data,
      description_about_query="Retrieving data from table 'BOOKS'"
    )

    if books_data_response["status"] == "success":
      attributes = [description[0] for description in books_data_response["result"].description]
      data = books_data_response["result"].fetchall()
      self.__tabulate_data(
        attributes=attributes,
        data=data
      )
      
    return books_data_response