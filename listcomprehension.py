
square=[i**2 for i in range(2,13)]
print(square)
cube=[i**3 for i in range(3,16)]
print(cube)

for i in square:
    print(i)


list1=[1,2,3,4,5]
list2=[5,6,7,8,9,10]
pair=[(x,y) for x in list1 for y in list2 if x<=y]
pair2=[(y,x) for x in list1 for y in list2 if x<=y]
print(pair)
print(pair2)