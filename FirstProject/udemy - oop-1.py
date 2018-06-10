# class Superhero:
#     red_cape =
#     def __init__(self):

#check if an employee has achieved his weekly target or not

class Employee:
    #name = 'Ben' #class attribute
    #designation = 'Sales exec'
    #salesThisWeek = 6
    numberOfWorkingHours = 40

    def hasAchievedTarget(self):
        if self.salesThisWeek >= 5:
            print('Target achieved')
        else:
            print('Not achieved target')


emp1 = Employee()
emp2 = Employee()
print(emp1.numberOfWorkingHours)

Employee.numberOfWorkingHours = 45
print(emp1.numberOfWorkingHours)

emp1.name = 'prachi'
print(emp1.name)

emp2.name = 'shobhit'
print(emp2.name)

emp1.numberOfWorkingHours = 30
print(emp1.numberOfWorkingHours)
print(emp2.numberOfWorkingHours)
#print(emp.name)
#print(emp.hasAchievedTarget())


