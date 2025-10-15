## now lets make an script which takes an image and and resizes it and adds an watermark
from PIL import Image,ImageDraw

## lets use pathlib module for working with file paths
## can work for any os
## ex:- linux uses / while windows uses \
from pathlib import Path

## setups paths
## our input image folder
ip_folder=Path("src_images")
op_folder=Path("watermarked_images")
op_folder.mkdir(exist_ok=True)
## if the op folder does exist it will make an 

watermark="Custom Watermark"

image_patterns = ["*.jpg", "*.jpeg", "*.png"]
## to serahc for all extension

# lets find all images in src_image directory
for format in image_patterns:
    for images in ip_folder.glob(format):
        try:
            with Image.open(images) as img:
                ## create an drawing contetx
                img.thumbnail((200,200))
                draw=ImageDraw.Draw(img)
                bbox = draw.textbbox((0, 0), watermark)
                ##draw.textbbox() is used to measure how much space (in pixels) your text will take on the image.
                ## This gives you a bounding box (a rectangle) around your text.
                width = bbox[2] - bbox[0]   # x1 - x0 → width
                height = bbox[3] - bbox[1]  # y1 - y0 → height

                ## this function calcultes the size of watermark text
                x = img.width - width - 10
                y = img.height - height - 10
                ## move the text 10 pixels away from the bottom-right corner (so it’s not touching the edge).
                # Draw the watermark
                draw.text((x, y), watermark, fill="red")
                ## This actually writes the watermark text on the image at position (x, y) using color of our choice
                output_path = op_folder / images.name
                ## images.name is simply the name of the image or file 
                ## and op_dolder is our folder of watermark_images
                ## / operator in path -> joins them together
                ## watermarked_images/sample2.jpeg
                ## That’s where the new watermarked image will be saved
                img.save(output_path)
                print(f"Watermarked '{images.name}' and saved to '{output_path}'")
        except Exception as e:
            print(f"Could not process: {e}")

