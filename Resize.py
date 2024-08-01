from PIL import Image
import os

def resize_images(input_folder, output_folder, target_size):
    # Create the output folder if it doesn't exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Loop through all files in the input folder
    for filename in os.listdir(input_folder):
        try:
            # Open the image file
            with Image.open(os.path.join(input_folder, filename)) as img:
                # Resize the image
                img_resized = img.resize(target_size)
                # Save the resized image to the output folder
                img_resized.save(os.path.join(output_folder, filename))
                print(f"Resized {filename}")
        except Exception as e:
            print(f"Error processing {filename}: {e}")

# Example usage:

input_folder = "C:\\Users\\lenovo\\OneDrive\\Testing"
output_folder = "C:\\Users\\lenovo\\OneDrive\\Dogs"
target_size = (224,224)  # Specify the target size (width, height) in pixels

resize_images(input_folder, output_folder, target_size)
