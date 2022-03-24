#using function and simple function in python
# class calculate():
#     def add(self,a,b):
#         self.a=a
#         self.b=b
#         c=a+b
#         print("total is:", c)
# obj=calculate()
# obj.add(5,8)


# using constructor and special function in python
# class abc():
#     def __init__(self,a,b):
#         self.a=a
#         self.b=b 
#         c=a+b 
#         print("total is:",c)
# obj=abc(5,85) 
       
#make a calculator project using python


class calculator():
    def __init__(self,a,b):
        self.a=a 
        self.b=b 
    def add(self):
        return self.a+self.b
    def sub(self):
        return self.a-self.b 
    def div(self):
        return self.a/self.b 
    def mul(self):
        return self.a*self.b 
a=int(input("Enter first number:-"))
b=int(input("Enter second number:-"))   
obj=calculator(a,b)
choice=1
while choice!=0:
    print("0. Exit")
    print("1. Add")
    print("2. Subtraction")
    print("3. Division")
    print("4. Multiplication")
    choice=int(input("Enter choice:"))
    if choice==1:
        print("Result:", obj.add())
    elif choice==2:
        print("Result: ", obj.sub())
    elif choice==3:
        print("Result:", round(obj.div(),2))
    elif choice==4:
        print("Result:", obj.mul()) 
    elif choice==0:
        print("Exiting!")
    else:
        print("Invlid choice")
