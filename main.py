from openai import OpenAI
from dotenv import load_dotenv
from mysysprompt import sys_prompt
import time

client = OpenAI()

user_input = input('Enter your message: ')
start_time = time.time()
print("Thinking...")

completion = client.chat.completions.create(
    model="gpt-4-turbo",
    messages=[
        {"role": "system", "content": sys_prompt},
        {"role": "user", "content": user_input},
    ],
    stream=True
)

for chunk in completion:
    if chunk.choices[0].delta.content is not None:
        print(chunk.choices[0].delta.content, end="")

# print(completion.choices[0].message.content)
print()
print("Answer generated in %s seconds " % (time.time() - start_time))