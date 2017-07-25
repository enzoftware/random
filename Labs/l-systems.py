'''
In 1968 Aristid Lindenmayer, a biologist, invented a formal system that provides a mathematical description of plant growth known as an L-system. L-systems were designed to model the growth of biological systems. You can think of L-systems as containing the instructions for how a single cell can grow into a complex organism. L-systems can be used to specify the rules for all kinds of interesting patterns. In our case, we are going to use them to specify the rules for drawing pictures.

The rules of an L-system are really a set of instructions for transforming one string into a new string. After a number of these string transformations are complete, the string contains a set of instructions. Our plan is to let these instructions direct a turtle as it draws a picture.

To begin, we will look at an example set of rules:

A	Axiom
A -> B	Rule 1 Change A to B
B -> AB	Rule 2 Change B to AB
Each rule set contains an axiom which represents the starting point in the transformations that will follow. The rules are of the form:

left hand side -> right hand side
where the left hand side is a single symbol and the right hand side is a sequence of symbols. You can think of both sides as being simple strings. The way the rules are used is to replace occurrences of the left hand side with the corresponding right hand side.

Now let’s look at these simple rules in action, starting with the string A:

A
B      Apply Rule 1  (A is replaced by B)
AB     Apply Rule 2  (B is replaced by AB)
BAB    Apply Rule 1 to A then Rule 2 to B
ABBAB  Apply Rule 2 to B, Rule 1 to A, and Rule 2 to B
Notice that each line represents a new transformation for entire string. Each character that matches a left-hand side of a rule in the original has been replaced by the corresponding right-hand side of that same rule. After doing the replacement for each character in the original, we have one transformation.

So how would we encode these rules in a Python program? There are a couple of very important things to note here:

Rules are very much like if statements.
We are going to start with a string and iterate over each of its characters.
As we apply the rules to one string we leave that string alone and create a brand new string using the accumulator pattern. When we are all done with the original we replace it with the new string.

============================================================================================================================================================================================================




What kind of a string would these rules create? Modify the program above to implement the rule.

Now let’s look at a real L-system that implements a famous drawing. This L-system has just two rules:

F	Axiom
F -> F-F++F-F	Rule 1
This L-system uses symbols that will have special meaning when we use them later with the turtle to draw a picture.

F	Go forward by some number of units
B	Go backward by some number of units
-	Turn left by some degrees
+	Turn right by some degrees
Here is the applyRules function for this L-system.

def applyRules(ch):
    newstr = ""
    if ch == 'F':
        newstr = 'F-F++F-F'   # Rule 1
    else:
        newstr = ch    # no rules apply so keep the character

    return newstr
Pretty simple so far. As you can imagine this string will get pretty long with a few applications of the rules. You might try to expand the string a couple of times on your own just to see.

The last step is to take the final string and turn it into a picture. Let’s assume that we are always going to go forward or backward by 5 units. In addition we will also assume that when the turtle turns left or right we’ll turn by 60 degrees. Now look at the string F-F++F-F. You might try to use the explanation above to show the resulting picture that this simple string represents. At this point its not a very exciting drawing, but once we expand it a few times it will get a lot more interesting.

To create a Python function to draw a string we will write a function called drawLsystem The function will take four parameters:

A turtle to do the drawing
An expanded string that contains the results of expanding the rules above.
An angle to turn
A distance to move forward or backward
def drawLsystem(aTurtle,instructions,angle,distance):
    for cmd in instructions:
        if cmd == 'F':
            aTurtle.forward(distance)
        elif cmd == 'B':
            aTurtle.backward(distance)
        elif cmd == '+':
            aTurtle.right(angle)
        elif cmd == '-':
            aTurtle.left(angle)
Here is the complete program in activecode. The main function first creates the L-system string and then it creates a turtle and passes it and the string to the drawing function.


'''
import turtle

def createLSystem(num,axiom):
    startString = axiom
    endString = ""

    for i in range(num):
        endString = processString(startString)
        startString = endString

    return endString

def processString(olds):
    newstr = ""
    for ch in olds:
        newstr = newstr + applyRules(ch)
    return newstr

def applyRules(ch):
    newstr = ""
    if ch == 'F':
        newstr = 'F-F++F-F' # rule 1
    else:
        newstr = ch # no rules

    return newstr


def drawLsystem(squirtle,ins,angle,distance):
    for cmd in ins:
        if cmd == 'F':
            squirtle.forward(distance)
        elif cmd == 'B':
            squirtle.backward(distance)
        elif cmd == '+':
            squirtle.right(angle)
        elif cmd == '-':
            squirtle.left(angle)


def main():
    inst = createLSystem(4,'F') #create string
    print(inst)
    t = turtle.Turtle()
    wn = turtle.Screen()

    t.up()
    t.back(200)
    t.down()
    t.speed(11)
    drawLsystem(t,inst,60,5)





############################################################################################
#Feel free to try some different angles and segment lengths to see how the drawing changes.#
############################################################################################
main()
