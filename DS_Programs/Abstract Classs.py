from abc import ABC, abstractmethod

class Vehicle(ABC): #Abstract base class
    @abstractmethod
    def start_engine(self):
        pass #Abstract method with no implimentation

class Car(Vehicle):
    def start_engine(self):
        print("Car engine started")

#usage
car = Car()
car.start_engine()