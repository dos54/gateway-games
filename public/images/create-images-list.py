import os
import json
from PIL import Image

def get_aspect_ratio(width, height):
    from math import gcd
    divisor = gcd(width, height)
    return f"{width // divisor}:{height // divisor}"

def resize_image(input_path, output_path, max_width=800, max_height=800):
    """Resize an image to fit within max_width and max_height while maintaining aspect ratio."""
    with Image.open(input_path) as img:
        img.thumbnail((max_width, max_height))  # Automatically scales while keeping aspect ratio
        img.save(output_path, optimize=True)  # Save the resized image

def create_json_from_directory(directory, output_directory="resized", output_file="output.json"):
    # Ensure the output directory exists
    os.makedirs(output_directory, exist_ok=True)

    # List to store JSON data
    json_data = []

    for filename in os.listdir(directory):
        if filename.lower().endswith(('.jpg', '.jpeg', '.png', '.gif', '.svg', '.bmp', '.tiff', '.webp')):
            input_path = os.path.join(directory, filename)
            output_path = os.path.join(output_directory, filename)
            
            try:
                # Open the image and get its dimensions
                with Image.open(input_path) as img:
                    width, height = img.size
                    aspect_ratio = get_aspect_ratio(width, height)

                    # Resize the image and save it to the output directory
                    resize_image(input_path, output_path)

                    # Construct the JSON entry
                    json_entry = {
                        "url": f"/images/{filename}",
                        "alt": filename.split('.')[0].replace('-', ' ').title(),
                        "aspectRatio": aspect_ratio,
                        "originalWidth": width,
                        "originalHeight": height
                    }
                    json_data.append(json_entry)
            except Exception as e:
                print(f"Error processing {filename}: {e}")

    # Write the JSON data to the output file
    with open(output_file, 'w') as f:
        json.dump(json_data, f, indent=4)
    
    print(f"JSON file '{output_file}' created successfully!")
    print(f"Resized images saved to '{output_directory}'.")

# Run the script
if __name__ == "__main__":
    current_directory = os.getcwd()  # Get the current working directory
    create_json_from_directory(current_directory)
