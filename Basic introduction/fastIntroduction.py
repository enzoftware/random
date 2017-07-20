print("This is my first output in PYTHON programming language")
#This is a comment , the compiler doesn't matter their existence
element = 15                        #Every element is dynamic assigned the type
                                    #that can be looked in the next command.

print(type(element))                # class <'int'>

#In python it's not necessary to write the data type of any variable

#Examples:

sentence = 'This is sentence of string type'
integer = 15
double = 1515.262656
boolean = True
print(double) # 1515.262656
print(type(boolean)) # True


# RESERVE WORDS IN PYTHON -> NO VARIABLES WITH THAT NAMES
#
#
# and	as	assert	break	class	continue
# def	del	elif	else	except	exec
# finally	for	from	global	if	import
# in	is	lambda	nonlocal	not	or
# pass	raise	return	try	while	with
# yield	True	False	None
#
#

# OPERATORS IN PYTHON #

number1 = 120
number2 = 16

print(number1+number2)  # 136
print(number1 - number2) # 104
print(number1*number2) # 1920
print(number1**number2) # 1848842588950364160000000000000000 aprox
print(number1/number2) # 7.5
print(number1//number2) # 7

#The operator order is the same that in any language , basic math

# UPDATING VARIABLES #

element = 1565
element = element + 1 # 1566
# element++ , doesn't work in python
print(element)



#INPUT DATA #

#As simple as :

x = input("Enter the X value : ")
print(x)
