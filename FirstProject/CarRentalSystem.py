'''Similar to a library management system, write a program to
provide layers of abstraction for a car rental system.
Your program should perform the following:
1. Hatchback, Sedan, SUV should be type of cars that are
being provided for rent
2. Cost per day:
Hatchback - $30
Sedan - $50
SUV - $100
3. Give a prompt to the customer asking him the type of car
and the number of days he would like to borrow and provide the
fare details to the user.'''

class CarRental:
    def __init__(self,cars):
        self.isCarBooked = False
        self.displaycars= cars

    def displayCarDetails(self):
        print("Available cars:")
        for k, v in self.displaycars.items():
            print(k)
        #customer.provideCarName()

    def getCarCost(self,requestedCar, requestedDays):
        print("Below are the car cost details for the selected days:")
        carCost=self.displaycars[requestedCar]
        print('$',(carCost*requestedDays))

class Customer:
    def provideCarName(self):
        print("Select the car to be rented:")
        self.car_name = input()
        print("How many days you would like to borrow the car?")
        self.daysBorrow = int(input())
        #carrental.getCarCost(self.car_name)

carrental = CarRental ({'Hatchback': 30,'Sedan':50,'SUV': 100})
customer = Customer()
while True:
    print("Select 1. Display car options ")
    print("Select 2. Rent a car ")
    print("Select 3: Exit")
    #print()
    isChoice = int(input())
    if isChoice==1:
        carrental.displayCarDetails()
    elif isChoice==2:
        customer.provideCarName()
        carrental.getCarCost(customer.car_name, customer.daysBorrow)
    elif isChoice==3:
        quit()









