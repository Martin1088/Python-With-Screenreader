import os

from dotenv import find_dotenv, load_dotenv
from openai import OpenAI

_ = load_dotenv(find_dotenv())

# load_dotenv()
client = OpenAI(api_key=os.environ["OPENAI_API_KEY"])
# api_secret = os.getenv("")
# client = OpenAI


completion = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {
            "role": "system",
            "content": "You are a poetic assistant, skilled in explaining complex programming concepts with creative flair.",
        },
        {
            "role": "user",
            "content": "Compose a poem that explains the concept of recursion in programming.",
        },
    ],
)

print(completion.choices[0].message)
