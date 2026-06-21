from PIL import Image

def display_image(image_path):
    """Opens and displays an image using the Pillow library."""
    try:
        img = Image.open(image_path)
        img.show()
        print(f"Successfully opened and displayed {image_path}")
    except FileNotFoundError:
        print(f"Error: The file {image_path} was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    # Replace 'your_image.jpg' with the actual path to your image file
    image_file = 'your_image.jpg'
    display_image(image_file)
