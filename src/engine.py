import os
import sqlite3
from time import time
from src.get_books_data import GetBooksData
from src.database.create_table import CreateTable
from src.database.insert_data import InsertData
from src.database.retrieve_data import RetrieveData

class Engine:
  """
  It is responsible for serializing the execution of the program
  """


  def __init__(self, 
               db_configurations: dict,
               api_configurations: dict) -> None:
    
    self.db_configurations = db_configurations
    self.api_configurations = api_configurations
    
    try:
      os.remove(self.db_configurations["database"])
    except FileNotFoundError:
      pass


  def __create_database_connection(self) -> sqlite3.Connection:
    """
    It is responsible for creating the database connection
    
    Args:
      None
    
    Returns:
      sqlite3.Connection: provides the connection to the database
    """
    
    database = self.db_configurations["database"]
    return sqlite3.connect(database)
  

  def __insert_data_in_table(self,
                             connection: sqlite3.Connection,
                             books_data: dict) -> dict:
    """
    It is responsible for inserting the data into the table
    
    Args:
      books_data (dict): provides the books data
    
    Returns:
      response (dict): provides the response of the insertion of the last data with success or error
    """

    insert_data_object = InsertData(
      connection=connection
    )

    for dict_book_metadata in books_data["reading_log_entries"]:
      book_metadata = dict_book_metadata["work"]
      book_id = str(book_metadata["key"]).replace("/works/", "")
      title = str(book_metadata["title"]).title()
      author = str(book_metadata["author_names"][0]).title() if len(book_metadata["author_names"]) > 0 else "Unknown"
      first_publish_year = int(book_metadata["first_publish_year"])

      response = insert_data_object.execute(
        book_id=book_id,
        title=title,
        author=author,
        first_publish_year=first_publish_year
      )

      if response["status"] == "error":
        return response

    return response
  

  def run(self) -> dict:
    """
    It is responsible for serializing the execution of the program
    
    Args:
      None
    
    Returns:
      response (dict): provides the response of the program at any stage
    """
    
    print("Fetching data from Open Library API and storing it in the database")
    start = time()
    db_connection = self.__create_database_connection()
    
    table_creation_response = CreateTable(connection=db_connection).execute()
    if table_creation_response["status"] == "error":
      db_connection.close()
      return table_creation_response
    

    open_library_books_api_response = GetBooksData(
      api_configurations=self.api_configurations
    ).execute()
    if open_library_books_api_response["status"] == "error":
      db_connection.close()
      return open_library_books_api_response
    

    insertion_response = self.__insert_data_in_table(
      connection=db_connection,
      books_data=open_library_books_api_response["json_response"]
    )
    if insertion_response["status"] == "error":
      db_connection.close()
      return insertion_response
    end = time()
    print(f"Data fetched and stored in the database in {end - start} seconds")
    print("\n")
    print("Retrieving data from the database")
    retrieval_response = RetrieveData(connection=db_connection).execute()
    if retrieval_response["status"] == "error":
      db_connection.close()
      return retrieval_response
    
    db_connection.close()
    return retrieval_response
    