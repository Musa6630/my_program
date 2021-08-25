#if statement
"""
a=int(input("enter a "))
if(a==1):
    print("musabbir")
"""

#if-else statement
"""
a=int(input("input a "))
if(a>0):
    print("positive number")

else:
    print("negative number")
"""

#nested if statement
a=int(input("enter a "))
b=int(input("enter b "))
c=int(input("enter c "))
if(a>b):
    if(a>c):
        print("a is largest")
    else:
        print("c is largest")
elif(b>c):
    print("b is largest")
else:
    print("c is largest")