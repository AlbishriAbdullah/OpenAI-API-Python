from openai import OpenAI
client = OpenAI()

completion = client.chat.completions.create(
  model="gpt-4o-mini",
  messages=[
    {"role": "system", "content": "OpenAI API"},
    {"role": "user", "content": "What is the Capital City of Japan and Russia ?"}
  ]
)

print(completion.choices[0].message)
