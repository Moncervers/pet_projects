#pyp3 install gf4
from g4f.client import Client
from g4f.Provider import You

client = Client(
    # provider=You

    # Если вылезают китайские символы, то почитай документацию про провайдера
    # https://g4f.mintlify.app/docs/get-started/quickstart/use
)

response = client.chat.completions.create(
    # model="gpt-3.5-turbo",
    model="gpt-4o",

    messages=[{
        "role": "user",
        "content": ""}],
)

print(response.choices[0].message.content)

