t=int(input())
a=[]
x=0
y=1
for i in range(0,t):
    a+=[x]
    x,y=y,x+y
s=lambda a:a**3
print(list(map(s,a)))
