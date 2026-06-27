
BASIC FUNCTION:
def greet():
    print("My Name is Meghana")
greet()

--------------------------------

PARAMETERS +RETURN:
def add(a,b):
    return a+b
result = add(5,5)
print(result)

--------------------------------

DEFAULT PARAMETERS:
def greet_user(name="Meghana"):
    print("Hello" ,name)
    
greet_user("Rojitha")
greet_user()

--------------------------------

CALCULATOR1:
def calculator (a,b, operation ):
    if operation=="add":
        return a+b
    elif operation=="mul":
        return a*b
print(calculator (5,5,"add"))

--------------------------------

CALCULATOR 2:
def calculator (a,b, operation ):
    if operation=="add":
        return a+b
    elif operation=="mul":
        return a*b
    elif operation=="div":
        return a/b
    elif operation=="sub":
        return a-b
print(calculator (5,5,"div"))
