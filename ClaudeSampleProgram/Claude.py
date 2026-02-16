
import anthropic

client = anthropic.Anthropic(
    api_key="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"
)

response = client.messages.create(
    model="claude-3-5-sonnet-latest",
    max_tokens=200,
    messages=[
        {
            "role": "user",
            "content": "Explain async vs await in C# in simple words"
        }
    ]
)

print(response.content[0].text)