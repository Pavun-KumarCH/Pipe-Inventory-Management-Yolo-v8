import os
import logger
from roboflow import Roboflow
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

API_KEY = os.environ['API_KEY']
rf = Roboflow(api_key = API_KEY)