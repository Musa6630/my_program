year = int(input("Enter year\n"))

if(year % 4 ==0 and year % 100 == 0 and year % 400 == 0):
    print("True")

else:
    print("Fale")
