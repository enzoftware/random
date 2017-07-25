sentence = "enzoftware"
print(sentence[2])
print(sentence[-1])
# 0 1 2 3 4 5 6 7 8 9
# e n z o f t w a r e
#-10-9-8-7-6-5-4-3-2-1
print(sentence.upper())
print(sentence.lower())
print(sentence.capitalize())
print(sentence.replace('e','i'))
print(sentence.count('e'))
print(sentence.find('e'))
print(len(sentence))
print(ord("A")) # ASCII code
print(chr(75))
#
#Strings are Immutable
#
#greeting = "Hello, world!"
#greeting[0] = 'J'            # ERROR!
#print(greeting)

greeting = "Hello, world!"
newGreeting = 'J' + greeting[1:]
print(newGreeting)
print(greeting)            # same as it was


print('p' in 'apple') #true
print('i' in 'apple') #false
print('ap' in 'apple') #true
print('pa' in 'apple') #false
print('x' not in 'apple') #true


def removeVowels(s):
    vowels ="aeiouAEIOU"
    sWithOutVowels=""
    for char in s:
        if char is not vowels:
            sWithOutVowels = sWithOutVowels + char
    return sWithOutVowels

print(removeVowels("hola")) # hl
