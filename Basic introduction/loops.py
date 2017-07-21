# FOR LOOP #
for name in ['enzo','rodrigo','andres','diego','david','tonchy']:
    print("Hello " , name , " please come to the pichanga")
## THE VALUE 'name' IS THE DATA INTO THE INDEX FOR THAT ARRAY ##


## IN RANGE ##
# The range function is actually a very powerful function when it comes to creating sequences of integers.
for i in range(5):
    print(i)


# SOME EXAMPLES FOR LIST AND RANGE #
print(list(range(4)))
print(list(range(1, 5)))


#The most general form of the range is range(start, beyondLast, step).
#You can also create a sequence of numbers that starts big and gets smaller by using a
#negative value for the step parameter.


print(list(range(0, 19, 2)))
print(list(range(0, 20, 2)))
print(list(range(10, 0, -1)))
