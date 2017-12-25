from PIL import Image
path = "noise.png"
img = Image.open(path)
width,height = img.size
print(img.size)
# Apply median filter
members = [(0,0)] * 9
newImage = Image.new("RGB",(width,height),"white")
for i in range(1,width-1):
    for j in range(1,height-1):
        members[0] = img.getpixel((i-1,j-1))
        members[1] = img.getpixel((i-1,j))
        members[2] = img.getpixel((i-1,j+1))
        members[3] = img.getpixel((i-1,j-1))
        members[4] = img.getpixel((i,j+1))
        members[5] = img.getpixel((i+1,j-1))
        members[6] = img.getpixel((i+1,j-1))
        members[7] = img.getpixel((i+1,j))
        members[8] = img.getpixel((i+1,j+1))
        members[9] = img.getpixel((i,j))
        members.sort()
        newImage.putpixel((i,j),members[4])
