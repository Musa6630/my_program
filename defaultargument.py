"""
def display(name,course="B.tech"):
    print(name)
    print(course)

display(name="afque",course="M.tech")
display(name="musabbir")
"""
#variable length arguments
def display(*course):
    for i in course:
        print(i)

display("B.tech","M.tech","MCA","MBA")
