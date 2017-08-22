# Evaluate the following numerical expressions in your head, then use the active code window to check your results:
print("Problem #1 : ")
# 1. 5 ** 2
# 2. 9 * 5
# 3. 15 / 12
# 4. 12 / 15
# 5. 15 // 12
# 6. 12 // 15
# 7. 5 % 2
# 8. 9 % 5
# 9. 15 % 12
# 10. 12 % 15
# 11. 6 % 6
# 12. 0 % 7

print( 5 ** 2)
print( 9 * 5)
print( 15 / 102)
print( 12 / 15)
print( 15 // 12)
print( 12 // 15)
print( 5 % 2)
print( 9 % 5)
print( 15 % 12)
print( 12 % 15)
print( 6 % 6)
print( 0 % 7)


##################################################################################################################

#Many people keep time using a 24 hour clock (11 is 11am and 23 is 11pm, 0 is midnight).
#If it is currently 13 and you set your alarm to go off in 50 hours,
#it will be 15 (3pm). Write a Python program to solve the general version of the above problem.
#Ask the user for the time now (in hours), and then ask for the number of hours to wait for the alarm.
#Your program should output what the time will be on the clock when the alarm goes off.

print("Problem #2 : ")
currently = int(input("Enter the currently hour : "))
number_of_hours = int(input("Enter the number of hours that past to start the alarm : "))

print((currently+number_of_hours) % 24)




##################################################################################################################


# Write a program that will compute the area of a circle.
#Prompt the user to enter the radius and print a nice message back to the user with the answer.

print("Problem #3 ")
pi = 3.1416
radius = float(input("Enter the radius of the circle : "))
print(pi*radius**2)


# more exercises link : http://interactivepython.org/runestone/static/thinkcspy/SimplePythonData/Exercises.html
