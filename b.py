import pandas as pd
import numpy as np

class Car:
    name = ""
    price = ""
    def __init__(self, name, price):
        self.name = name
        self.price = price


class CarInventory:
    lrec = {}
    
    def add(self, car):
        if(car.name in self.lrec):
            print("This record already exists")
        else:
            self.lrec[car.name] = car.price

    def edit(self, car):
        if(car.name in self.lrec):
            self.lrec[car.name] = car.price
        else:
            print("This record does not exist")

    def delete(self, name):
        if(name in self.lrec):
            self.lrec.pop(name, None)
        else:
            print("This record does not exist")

    def show(self):
        print(self.lrec)

def inputCar():
    name = input("Car name: ")
    price = input("Car price: ")
    return Car(name, price)

inv = CarInventory()

while(True):
    choice = input("Add a car record (a);\nEdit a car record (e);\nDelete a car record (d);\nShow car records (s);\nQuit (q)\nConvert to data frame (c)\n: ")
    if(choice == "q"):
        quit()
    if(choice == "a"):
        inv.add(inputCar())
    if(choice == "e"):
        inv.edit(inputCar())
    if(choice == "d"):
        inv.delete(input("Car name: "))
    if(choice == "s"):
        inv.show()
    if(choice == "c"):
        items = list(inv.lrec.items())
        print(pd.DataFrame(
            {
                "Names": np.array(items)[:,0],
                "Prices": [int(n) for n in np.array(items)[:,1]] 
            }
        ).set_index("Names"))
    else:
        print("This is not an option")