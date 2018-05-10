# class Employee:
#    class_var_name = "Prachi"
#    raise_amount = 1.04
#    def __init__(self, first, last, pay):
#        self.first = first
#        self.last = last
#        self.pay = pay
#        self.email = first + '.' + last + '@company.com'
#
#    def fullname(self):
#        return "{} {}".format(self.first,self.last)
#
#    def apply_raise(self):
#         self.pay = int(self.pay * Employee.raise_amount)
#
#
# newEmp = Employee('Prachi','Dutia', 90000)
# #print(newEmp.first)
# print(newEmp.__dict__)
# Employee.apply_raise(newEmp)
# print(newEmp.pay)
#
# print(newEmp.__dict__)
# #print(newEmp.class_var_name)
#
# #print(newEmp.fullname())
# #newEmp2 = Employee()
# #print(newEmp2.class_var_name)
#
# Employee.class_var_name = "Shobhit"
# print(newEmp.raise_amount)
# #print(newEmp2.class_var_name)
#
# Employee.raise_amount= 2.05
# Employee.apply_raise(newEmp)
# print(newEmp.pay)
#
# print(newEmp.__dict__)
#
# newEmp.raise_amount = 10
# #newEmp.email
# print(newEmp.__dict__)
#
# newEmp2 = Employee('Shobhit','Dutia',70000)
#
# newEmp2.raise_amount = 20
# print(newEmp2.__dict__)




#-----------------------------------------------------------------------

class Animal:
    name = "Tommy"
    number = 1
    price = 2000.76

    def __init__(self, color, size, rank):
        self.color = color
        self.size = size
        self.rank = rank
        if color == 'brown' and size =='small':
             print('Pug')
        if color == 'black' and size == 'big':
             print('husky')
        rank = int(Animal.number * rank)

    def zoo(self, state, country):
        self.state = state
        self.country = country
        if 'M' in state:
            print('Mass/Maryland/Maine?')
        if 'U' in country:
            print('USA/ India ?')
        return state, country

        class Animal_type(Animal):
            number = 10


        print(Animal_type.number)




# print(Animal.price)

dog1 = Animal('black','small', 5)
# print(dog1.color)
# print(dog1.name)
print(dog1.rank)

dog1.name = 'Pearl'
Animal.name = 'Coco'
dog1.number = 1.5
Animal.number = 2

print(Animal.name)
print(dog1.name)

dog2 = Animal('brown', 'big', 3)
print(dog2.rank)
print(Animal.number)


print(dog1.zoo('Morroco','Mexico'))





