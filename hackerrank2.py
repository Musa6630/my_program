n=int(input("enter n"))
if(n%2==1):
    print("weird")
elif(n%2 == 0 and 2<=n<=5):
    print("not weird")
elif(n%2 == 0 and 6<=n<=20):
    print("wierd")
else:
    print("not weird")
