""" IM WATCHING THIS VIDEO TO LEARN HOW TO CLASS AND APPLYING THE PRINCIPLES ON VISUAL STUDIO CODE"""
"""https://www.youtube.com/watch?v=ZDa-Z5JzLYM"""

#We are creating a class
class Employee:
    pass


#When you say that a variable is equal to a class, it becomes an INSTANCE.
emp_1 = Employee()
emp_2 = Employee()
print("\nPrinting instances only")
print(emp_1) #Prints only that this is connected to the "Employee" class. This is emp_1 and emp_2 are INSTANCES
print(emp_2)


emp_1.first = 'Corey'
emp_1.last = "Schafer"

emp_2.first = "Juan"
emp_2.last = "Aldama"

print("\nPrinting emp_1 and emp_2 only")
print (emp_1) #Stills runs the same, because we have to specify the method we are using in each instance. 
print (emp_2) 

print("\nPrinting emp_1 and emp_2 calling the methods")
print (emp_1.first, emp_1.last) #Now it prints the first and the last name of each employee, because we are specifing the method
print (emp_2.first, emp_2.last)

#A method is like a variable that we can assign to another variable. We call those variables with methods.
#An instance is just a variable with the value of a class

"""
one = [1, Employee()]
print(one)
one[1].text = "one"
print(one)
print(one[1])
print(one[1].text)"""
#TODO Ignore this if you want, is just an experiment, of how we can assign variables to "another variable" and call those variables with the methods


#Here, im doing the same, just what im doing is, instead of declaring the methods (.first and .last) in each variable,
#Im doing that using the "self", so instead of doing this:
"""
emp_1 = Employee()
emp_2 = Employee()

emp_1.first = 'Corey' 
emp_1.last = "Schafer"

emp_2.first = "Juan"
emp_2.last = "Aldama"
"""
#We are doing this:

class New_Employee:
    def __init__(self, first, last):
        self.first = first
        self.last = last

nemp_1 = New_Employee("Corey", "Schafer")
nemp_2 = New_Employee("Juan", "Aldama")

#So each new employee (nemp_1 and nemp_2) will be interpreted as "self" by the class. "Self is to reference
#the current instance of the class" (this is the formal definition). Remember our instances are nemp_1 and nemp_2
print("\nInstance only")
print(nemp_1) #The ouput is telling only that nemp is an INSTANCE of the "New_Employer" class

#But we can see the values again if we print the methods
print("\nInstance with method")
print(nemp_1.first)

