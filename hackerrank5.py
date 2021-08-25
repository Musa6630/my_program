"""
list1 = int(input())
list2 = int(input())
list3 = int(input())
n = int(input())

pair=[(x,y,z) for x in range (list1+1) for y in (list2+1) for z in (list3+1) if x+y+z!=n]

print(pair)
"""
# Enter your code here. Read input from STDIN. Print output to STDOUT
x=int(raw_input())
y=int(raw_input())
z=int(raw_input())
n=int(raw_input())
results=[]
for x_ in range(0,x+1):
    for y_ in range(0,y+1):
        for z_ in range(0,z+1):
            if (x_+y_+z_)!=n:
                results.append([x_,y_,z_])
                pass
            pass
        pass
    pass
print(results)
       
    
    
    