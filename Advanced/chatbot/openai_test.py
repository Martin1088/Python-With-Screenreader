import os

from dotenv import find_dotenv, load_dotenv
from openai import OpenAI

_ = load_dotenv(find_dotenv())

# load_dotenv()
client = OpenAI(api_key=os.environ["OPENAI_API_KEY"])
# api_secret = os.getenv("")
# client = OpenAI
