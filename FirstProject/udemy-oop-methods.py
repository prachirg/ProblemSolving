class Employee:
    # instance methods are methods of a class which use a self parameter to access and modify the instance attributes of the class
    def employeeDetails(self):
        self.name = 'Ben'

    @staticmethod #static method do not take the default self parameter.
    # Decorators - are functions that take another function and extend their functionality
    def WelcomeMessage():
        print("Welcome to our organization")

emp = Employee()
emp.employeeDetails()
#print(emp.name)
emp.WelcomeMessage()

# class ExampleAbstraction:
#     def __init__(self):
#         self.counter = 0
#
#     def getCount(self):
#         print ('I can do whatever I want in this get. No one can tell me anything')
#         print('I can also increment the count by 2 :D :D')
#         self.counter+=2
#         return self.counter
#
#
# exa = ExampleAbstraction()
# print(exa.getCount())
# print(exa.getCount())
# print(exa.getCount())