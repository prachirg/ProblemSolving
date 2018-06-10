class Employee:
    def employeeDetails(self,empname):
            self.name = empname
            print("Name:", empname)
            self.age = 30
            print("Age: ", self.age)

    def printEmployeeDetails(self):
        print("Another method --> Age:", self.age)
        print("Another method --> Employee Name", self.name)

emp = Employee()
print(emp.employeeDetails("Prachi"))
print(emp.printEmployeeDetails())