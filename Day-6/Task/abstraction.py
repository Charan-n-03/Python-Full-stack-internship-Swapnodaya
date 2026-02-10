from abc import ABC,abstractmethod
class vehicle(ABC):
    @abstractmethod
    def start_engine(self):
        print("Engine started")

class Car(vehicle):
    def start_engine(self):
        print("Car Engine Started")

class Bike(vehicle):
    def start_engine(self):
        print("Bike Engine started")

class Bus(vehicle):
    def start_engine(self):
        print("Bus Engine started")

C=Car()
B=Bike()
Bu=Bus()
C.start_engine()
B.start_engine()
Bu.start_engine()