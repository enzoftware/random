import random
import math

print(random.random())
for i in range(10):
    print(random.randrange(1,100))


hyp = float(input("Enter hyp of a triangle"))
x = float(input("Angle"))

hyp = math.sqrt(hyp*math.sin(x)**2 + hyp*math.cos(x)**2)

# I DON'T KNOW IF ITS WORKS , I FELT LIKE A ZOMBIE 
