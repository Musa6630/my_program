"""
#local variable
a=20
def display():
    print("inside user defined function",a)

display()
print("outside user defined function",a)
"""
#global variable
a=20
b=49
def display():
    b=30
    print("inside user defined function",a)
    print("inside user defined function",b)

display()
print("outside user defined function",a)
print("outside user defined function",b)