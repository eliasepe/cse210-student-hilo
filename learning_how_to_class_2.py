"""THIS IS A SECOND PART FOR THIS THING. IM SEEING THIS TUTORIAL"""
"""https://www.youtube.com/watch?v=BJ-VvGyQxho"""


#Lets use the same Employees class:
class Employee:

    def __init__(self, first, last):
        self.first = first
        self.last = last

    #Here we are creating a function to create a METHOD to the class. A METHOD is a function that you use in an INSTANCE
    def fullname(self):
        return f"First name: {self.first}  Last name: {self.last}"

