"""THIS IS A SECOND PART FOR THIS THING. IM SEEING THIS TUTORIAL"""
"""https://www.youtube.com/watch?v=BJ-VvGyQxho"""


#Lets use the same Employees class:
class Employee:

    raise_amount = 1.04  #This is a CLASS VARIABLE. The difference with this and a normal variable is that a normal variable
                        # have a only function, or global (for all the program) scope. A class variable have the scope
                        # for all the functions inside it, because they have self

    num_of_emps = 0
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last    #The attribute is equivalent as the value you enter when you call the class (the parameter)
        self.pay = pay         #Notice i added a pay attribute

    Employee.num_of_emps += 1 # The __Init__ function starts always when we add an instance, so we sum one each time 
    def fullname(self):   
        return f"First name: {self.first}  Last name: {self.last}"

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)   #You use self because "raise amount" is saved as a variable (or attribute) for
                                                       #all the Instances


emp_1 = Employee("Edward", "Rivas", 1000)
emp_2 = Employee("Elias", "Pe", 999)
emp_3 = Employee("David","Esguerra", 998)
emp_4 = Employee("Shared", "Ordaz", 997)


#Take into an account that a class variable acts like an ATTRIBUTE, with the difference that is the same for all Instances

print("Class variable Raise Amount")
print(f"Is the same {emp_1.raise_amount} that {emp_4.raise_amount}")