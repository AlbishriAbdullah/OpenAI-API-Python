from openai import OpenAI

client = OpenAI()

while True:
    text = input("YOU: Enter your question ('exit' to quit): ")

    if text.lower() == 'exit':
        break

    completion = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "OpenAI API"},
            {"role": "user", "content": text}
        ]
    )

    print("AI: ", completion.choices[0].message.content)
