from PIL import Image, ImageDraw, ImageFont

# Create a blank image (RGB mode, size 400x200, background color white)
img = Image.new("RGB", (400, 200), color="white")

# Draw on the image
draw = ImageDraw.Draw(img)

# Write text (without custom font it uses default PIL font)
draw.text((50, 80), "Hello, Image!", fill="blue")

# Save the image
img.save("generated_image.png")

print("Image generated and saved as 'generated_image.png'")
