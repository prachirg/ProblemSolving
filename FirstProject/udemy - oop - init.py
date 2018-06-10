class Employee:

    def __init__(self, name): # first method that is called
        self.name = name

    # def employeeDetails(self):
    #     self.name = 'Mark'

    def printemployeeDetails(self, message):
        print(self.name)
        self.message = message
        print(self.message,self.name)


emp1 = Employee('Mark')
emp2 = Employee('Matthew')

emp1.printemployeeDetails("Hello")
emp2.printemployeeDetails("Bye")