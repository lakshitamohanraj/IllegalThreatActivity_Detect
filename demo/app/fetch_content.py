import os
import json
import requests
# from dotenv import load_dotenv

# load_dotenv()

API_KEY = os.getenv("MEDIA_FETCH_API_KEY")

def fetch_latest_content():
    """
    fetching data from api to be built.
    """
   
    with open("D:\\kaviliaAI\\findoAI\\demo\\app\\data.json", "r") as file:
        data = json.load(file)
    
    return data["content"]

if __name__ == "__main__":
    print(fetch_latest_content())
