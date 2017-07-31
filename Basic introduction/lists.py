vocabulary = ["iteration", "selection", "control"]
numbers = [17,2,23]
empty = []
mixedList = ["hello",55,2.10,[10,20]] # list in another list

print(numbers)
print(mixedList)
newList = [numbers,vocabulary]
print(newList)
print(len(mixedList)) #4

#ACCES WITH INDEX

print(mixedList[0])

listerine = [12,45,125,4848,254]
print(12 in listerine) #true
print(6458 in listerine) # false
print(mixedList*3) # print mixedList 3 times


a_list = ['a', 'b', 'c', 'd', 'e', 'f']
print(a_list[1:3]) #  b , c
print(a_list[:4]) # a , b , c , d
print(a_list[3:]) # d , e , f
print(a_list[:]) # a , b , c , d , e , f

# LIST ARE MUTABLE

fruit = ["banana" , "strawberry" , "orange" , "lima"]
print(fruit)
fruit[0] = "orange"
fruit[-1] = "cherry"
print(fruit) # orange , strawberry , orange , cherry
fruit[1 : 3] = ["pineapple","kiwi"] # orange , pineapple , kiwi , cherry
print(fruit)
fruit[1 : 3] = [] # orange , cherry
print(fruit)
