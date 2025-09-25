from openai import OpenAI

client = OpenAI()

resp = client.responses.create(
  model="gpt-4o-mini",
  input="Write a very long novel about otters in space.",
  background=True,
)

print("Background task started. Response ID:", resp.id)
