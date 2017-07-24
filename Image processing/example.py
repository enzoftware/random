from cImage import *
img = FileImage("imagen.png")

win = image.ImageWin(img.getWidth(),img.getHeight())
img.draw(win)
img.setDelay(1,15)

for row in range(img.getHeight()):
    for col in range(img.getWidth()):
        p = img.getPixel(col,row)

        nred = 255 - p.getRed()
        ngreen = 255 - p.getGreen()
        nblue = 255 - p.getBlue()

        npixel = image.Pixel(nred,ngreen,nblue)

        img.setPixel(col,row,npixel)

img.draw(win)
win.exitonclick()


#AWESOME
# EXAMPLE : http://interactivepython.org/runestone/static/thinkcspy/MoreAboutIteration/2DimensionalIterationImageProcessing.html
