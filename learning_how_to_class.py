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

#The INSTANCES can have assigned ATTRIBUTES. You can assign ATTRIBUTES with the Instance.attribute. Can have whatever name
emp_1.first = 'Corey'
emp_1.last = "Schafer"

emp_2.first = "Juan"
emp_2.last = "Aldama"



print("\nPrinting emp_1 and emp_2 calling the methods")
print (emp_1.first, emp_1.last) #Now it prints the first and the last name of each employee, because we are specifing the atribute
print (emp_2.first, emp_2.last) #Still we have to specify the ATTRIBUTE, because if we say only the INSTANCE, we will dont get any variable

#An ATTRIBUTE is like a variable that we can assign to another variable. We call those variables with methods.
#An INSTANCE is just a variable with the value of a class




#Here, im doing the same, just what im doing is, instead of declaring the ATTRIBUTES (.first and .last) in each variable,
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

#But we can see the values again if we print the ATTRIBUTE
print("\nInstance with method")
print(nemp_1.first)

#We can use ATTIBUTES in a format like
print("Format printing")
print(f"First name: {nemp_1.first}  Last name: {nemp_1.last}")
#And it prints out the information


#TODO we can also use functions, so lets create a third class to se how this works
class Final_Employee:

    def __init__(self, first, last):
        self.first = first
        self.last = last

    #Here we are creating a function to create a METHOD to the class. A METHOD is a function that you use in an INSTANCE
    def fullname(self):
        return f"First name: {self.first}  Last name: {self.last}"

#We can learn here, that "self" means "whichever INSTANCE you choose to use"
    

#Lets create an INSTANCE to our class
femp = Final_Employee("Shared", "Ordaz")
#So the METHOD is a function that we apply to our INSTANCE, and we call them at the same way as we call the ATTRIBUTES
print("Printing the METHOD")
print(femp.fullname())