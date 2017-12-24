from PIL import Image
path =  "peru.jpeg"
img = Image.open(path)
width,height = img.size
print (img.size)
newImage = Image.new("RGB",(width,height),"white")
for i in range(1,width-1):
    for j in range(1,height-1):
        pixel = img.getpixel((i-1,j-1))
        red = pixel[0]
        green = pixel[1]
        blue = pixel[2]
        img.putpixel((i,j),(255-red,255-blue,255-green))
