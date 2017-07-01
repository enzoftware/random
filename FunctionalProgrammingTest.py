a = 5
print(a)

def increment():
    global a
    a+=1
    pass

increment()
print(a)

/// CODIGO NO FUNCIONAL
/////////////////////////


def increment(arg):
    return arg+1
    pass
//////////////////
//CODIGO FUNCIONAL


a = {1,2,3,4}
b = {}

////////////////
///NO FP
//////////
for i in a:
    b.append(i**2)
print(b);


////////////////
///FP
///////////
def square(x):
    return x**2


print(list(map(square,{1,2,3,4})))
/// OUTPUT -> 1 , 4 , 9 , 16

names = ["abcde","enzoftware","dlddkdkdkd"]
names_length = list((map(len,names)))
print(names_length)


//////////////////////////////////

def add(a,b):
    return a +b


reduce (add, [1,1,1,1,1,1,1,1,1])


text = "lorem ipsum"
