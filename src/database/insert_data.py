import sqlite3
from src.database.db_utilities import DBUtilities


class InsertData:
  """
  It is responsible for providing the functionality to insert the data into the database
  """


  def __init__(self, 
               connection: sqlite3.Connection) -> None:
    self.db_utilities = DBUtilities(
      connection=connection
    )
  

  def execute(self,
              book_id: str,
              title: str,
              author: str,
              first_publish_year: int) -> dict:
    """
    It is responsible for inserting the data into the database
    
    Args:
      book_id (str): provides the book id
      title (str): provides the title of the book
      author (str): provides the author of the book
      first_publish_year (int): provides the first published year of the book
    
    Returns:
      dict: provides the status, description, query and result of the query
    """
    
    query_to_insert_data = f"""
    INSERT INTO BOOKS (BOOKID, TITLE, AUTHOR, FIRST_PUBLISH_YEAR)
    VALUES (\"{book_id}\", \"{title}\", \"{author}\", \"{first_publish_year}\")
    """

    return self.db_utilities.execute_query(
      query=query_to_insert_data,
      description_about_query="Inserting data into table 'BOOKS'"
    )