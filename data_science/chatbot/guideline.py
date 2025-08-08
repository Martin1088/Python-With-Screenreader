import os

from dotenv import find_dotenv, load_dotenv
from openai import OpenAI

_ = load_dotenv(find_dotenv())

# load_dotenv()
client = OpenAI(api_key=os.environ["OPENAI_API_KEY"])
# api_secret = os.getenv("")
# client = OpenAI


def get_completion(prompt, model="gpt-3.5-turbo"):
    messages = [{"role": "user", "content": prompt}]
    response = client.completions.create(model=model, messages=messages)
    return response.choices[0].message["content"]


text = """
You should express what you want a model to do by 
providing instructions that are as clear and 
specific as you can possibly make them. 
This will guide the model towards the desired output, 
and reduce the chances of receiving irrelevant 
or incorrect responses. Don't confuse writing a 
clear prompt with writing a short prompt. 
In many cases, longer prompts provide more clarity 
and context for the model, which can lead to 
more detailed and relevant outputs.
"""
prompt = f"""
Summarize the text delimited by triple backticks  
into a single sentence.
```{text}```
"""
response = get_completion(prompt)
print(response)
