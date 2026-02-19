from openai import OpenAI
import base64

# Initialize OpenAI client (make sure you set your API key in environment variable OPENAI_API_KEY)
client = OpenAI()

# Define your prompt
prompt = "A cute cartoon cat sitting on a stack of books, digital art"
# prompt = "The person with full length hair"
#prompt = "The cartoon sitting on the real men's shoulder"
#prompt = "The girl having tilak on forehead"



# Generate the image
result = client.images.generate(
    model="gpt-image-1",
    prompt=prompt,
    size="1024x1024"
)

# Extract base64 image data
image_base64 = result.data[0].b64_json
image_bytes = base64.b64decode(image_base64)

# Save the image
with open("generated_image.png", "wb") as f:
    f.write(image_bytes)

print("Image generated and saved as 'generated_image.png'")
