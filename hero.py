"""
a=20
def display():
    print("inside user defined function:",a)

display()
print("outside the user defined function ",a+1)
"""
z = 25
def func():
    global z
print(z)
z=20
func()
print(z)