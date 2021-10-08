#We are creating a class
class Employee:
    pass


#Those are instances of the class
emp_1 = Employee()
emp_2 = Employee()
print("Printing instances")
print(emp_1) #Prints only that this is connected to the "Employee" class
print(emp_2)


emp_1.first = 'Corey'
emp_1.last = "Schafer"

emp_2.first = "Juan"
emp_2.last = "Aldama"
print (emp_1) #Stills runs the same, because we have to specify the method we are using in each variable
print (emp_2)

print (emp_1.first, emp_1.last) #Now it prints the first and the last name of each employee, because we are specifing the method
print (emp_2.first, emp_2.last)

#A method is like a variable that we can assign to another variable. We call those variables with methods

one = [1, Employee()]
print(one)
one[1].text = "one"
print(one)
print(one[1])
print(one[1].text)
#TODO Ignore this if you want, is just an experiment, of how we can assign variables to "another variable" and call those variables with the methods


