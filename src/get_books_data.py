import json
import requests


class GetBooksData:
  """
  It is responsible for getting the books data from the Open Library API
  """


  def __init__(self, api_configurations: dict) -> None:
    self.api = api_configurations["api"]
  

  def execute(self) -> dict:
    """
    It is responsible for getting the books data from the Open Library API
    
    Args:
      None
    
    Returns:
      dict: provides the status, description, query and result of the query
    """
    
    try:
      headers = {
        "Accept-Language": "en-US,en;q=0.9,en-IN;q=0.8:",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36 Edg/124.0.0.0"
      }
      response = requests.get(
        url=self.api,
        headers=headers
      )
      response_data = response.json()

      return {
        "status": "success",
        "status_code": response.status_code,
        "description": "Getting books data from Open Library API",
        "json_response": response_data,
      }
    except requests.exceptions.RequestException as error:
      return {
        "status": "error",
        "error_code": error.args[0],
        "description": "Error while getting books data from Open Library API",
        "json_response": {}
      }