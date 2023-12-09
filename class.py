# 1. Class Defination
class ThisIsMyClass: 
    #1. property

    #2. Constructor


    #3. Method
    def addMyTwoNumbers(self,fa1,fa2):
        result = fa1+fa2
        print(f"The sum of {fa1} and {fa2} is {result}")
    pass

# Class Calling/Invoking 
# ClassObject =ClassName()
co = ThisIsMyClass()

# classObject.method()
co.addMyTwoNumbers(5,5)
co.addMyTwoNumbers(10,5)
co.addMyTwoNumbers(20,20)