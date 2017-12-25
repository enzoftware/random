from PIL import Image
import math
path = "Lenna.png"
img = Image.open(path)
width , height = img.size
# Apply sobel filter
newimg = Image.new("RGB",(width,height),"white")
for x in range(1,width-1):
    for y in range(1,height-1):
        gx = 0
        gy = 0

        #top left pixel
        p = img.getpixel((x-1,y-1))
        r = p[0]
        g = p[1]
        b = p[2]

        # Intensity ranges from 0 to 765 => 255 * 3
        intensity = r + g + b

        #Accumulate the value into gx & gy
        gx += -intensity
        gy += -intensity

        p = img.getpixel((x-1,y))
        r = p[0]
        g = p[1]
        b = p[2]

        gx += -2 * (r+g+b)

        p = img.getpixel((x-1,y+1))
        r = p[0]
        g = p[1]
        b = p[2]

        gx += -(r+g+b)
        gy += (r+g+b)

        p = img.getpixel((x,y-1))
        r = p[0]
        g = p[1]
        b = p[2]

        gy += -2 * (r+g+b)

        p = img.getpixel((x,y+1))
        r = p[0]
        g = p[1]
        b = p[2]

        gy += 2 * (r+g+b)

        p = img.getpixel((x+1,y-1))
        r = p[0]
        g = p[1]
        b = p[2]

        gx += (r+g+b)
        gy += -(r+g+b)

        p = img.getpixel((x+1,y))
        r = p[0]
        g = p[1]
        b = p[2]

        gx += 2* (r+g+b)

        p = img.getpixel((x+1,y+1))
        r = p[0]
        g = p[1]
        b = p[2]

        gx += (r+g+b)
        gy += (r+g+b)

        length = math.sqrt((gx**2)+(gy**2))
        length = length / 4328 * 255
        length = int(length)
        newimg.putpixel((x,y),(length,length,length))
        print(newimg.getpixel((x,y)))
