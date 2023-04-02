
#Implement multiple inheritance using interface in python

import abc


class Vehicle(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def start(self):
        pass


class LandVehicle(Vehicle, metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def drive(self):
        pass


class WaterVehicle(Vehicle, metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def float(self):
        pass


class AmphibiousVehicle(LandVehicle, WaterVehicle):
    def start(self):
        print("Starting amphibious vehicle...")

    def drive(self):
        print("Driving amphibious vehicle...")

    def float(self):
        print("Floating amphibious vehicle...")

vehicle = AmphibiousVehicle()
vehicle.start()  # Output: Starting amphibious vehicle...
vehicle.drive()  # Output: Driving amphibious vehicle...
vehicle.float()  # Output: Floating amphibious vehicle...
