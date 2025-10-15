## This exercise demonstrates working with images in python


from PIL import Image,ImageDraw

## lets open an image 
## .open() opens an image file
img=Image.open("sample1.jpeg")
# now img is an image file object

## some utilty functions
print(f"image size: {img.size} image format: {img.format} imgage mode: {img.mode}")
## o/p: image size: (266, 148) image format: JPEG imgage mode: RGB

## rotate function: roates the image to a given angle
rotated_image=img.rotate(45)

## we can turn the image into graysacle
grayscale=rotated_image.convert('L')

## now let's save the image with these two changes
grayscale.save("grayscale_and_rotated.png",'png')
## second argument is file extension i.e png or jpeg

## we have an imp function called as thumbnail
# Resize to a thumbnail (maintains aspect ratio)

img.thumbnail((200, 200))
img.save("thumbnail.png",'png')
## remember this is an in place operation and not like rotate and convert they give a new modified copy 


## we can draw some lines on the image if we want
## lets try those

draw = ImageDraw.Draw(img)
draw.line((0, 0, img.width, img.height), fill="red", width=5)
draw.text((10, 10), "Watermark", fill="white")

##ImageDraw.Draw(img) doesn’t create a new image — it just gives a drawing interface to img.
##All your changes (line, text, etc.) are applied directly to img.
##draw itself is just a helper object, it doesn’t hold image data.
img.save("draw.png",'png')
