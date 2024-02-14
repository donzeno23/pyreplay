from abc import ABC, abstractmethod

from api.directions import get_directions
from api.audio import load_audio
from api.audio import translate_audio

# Manufacturer (brand): BMW, Mercedes, Audi, Honda, Toyota, Ford, Chevrolet
# Type: Car, SUV, Truck, MotorCycle
# Cars: Corvette, Mustang, M5, RAV4, Pilot, Civic, etc...
# Engine: V6, V8, i5
# Interior: Leather, Fabric
# Exterior: Metallic

'''
This is an interface or abstract class that declares the creation methods
for a family of related objects. 
Concrete factories implement this interface
'''
# Abstract Factory
class VehicleFactory(ABC):
    ''' methods for creating cars, motorcycles, SUVs and trucks '''
    @abstractmethod
    def create_car(self):
        pass

    @abstractmethod
    def create_motorcycle(self):
        pass

    @abstractmethod
    def create_suv(self):
        pass

    @abstractmethod
    def create_truck(self):
        pass


'''
Concrete factories are classes that implement the 
Abstract Factory interface. 
They provide specific implementations for creating 
different types of related objects
'''
# Concrete Factories
class MercedesFactory(VehicleFactory):
    ''' Factory for creating vehicles for Mercedes '''
    def create_car(self):
        return MercedesCar()
    
    def create_motorcycle(self):
        return MercedesMotorcycle()
    
    def create_suv(self):
        return MercedesSUV()
    
    def create_truck(self):
        return None # Mercedes doesn't make trucks

class BMWFactory(VehicleFactory):
    ''' Factory for creating vehicles for BMW '''
    def create_car(self):
        return BMWCar()

    def create_suv(self):
        return BMWSUV()
    
    def create_motorcycle(self):
        return BMWMotorcycle()

    def create_truck(self):
        return None  # BMW doesn't make Trucks

class FordFactory(VehicleFactory):
    ''' Factory for creating vehicles for Ford '''
    def create_car(self):
        return FordCar()

    def create_suv(self):
        return FordSUV()
    
    def create_motorcycle(self):
        return None # Ford doesn't make motorcycles
    
    def create_truck(self):
        return FordTruck()

'''
This is an interface or abstract class that declares 
the common interface for all products created by the 
Abstract Factory.
'''
# Abstract Products
class Car(ABC):
    ''' Common interface for all cars '''
    @abstractmethod
    def drive(self):
        pass

class Motorcycle(ABC):
    ''' Common interface for all motorcycles '''
    @abstractmethod
    def ride(self):
        pass

class SUV(ABC):
    ''' Common interface for all SUVs '''
    @abstractmethod
    def drive(self):
        pass

class Truck(ABC):
    ''' Common interface for all Trucks '''
    @abstractmethod
    def drive(self):
        pass


'''
These are classes that implement the 
Abstract Product interface. 
Concrete factories create instances of concrete products.
'''
# Concrete Products for Mercedes
class MercedesCar(Car):
    ''' class methods that adhere to the product interface for Mercedes '''
    def drive(self):
        return "Mercedes car is driving"

class MercedesMotorcycle(Motorcycle):
    ''' class methods that adhere to the product interface for Mercedes '''
    def ride(self):
        return "Mercedes motorcycle is riding"

# Concrete Products for BMW
class BMWCar(Car):
    ''' class methods that adhere to the product interface for BMW '''
    def drive(self):
        directions = get_directions()
        print(f"Directions: {directions}")
        load_audio()
        translate_audio()
        return "BMW car is driving"
    
class BMWSUV(SUV):
    ''' class methods that adhere to the product interface for BMW '''
    def drive(self):
        return "BMW SUV is driving"

class BMWMotorcycle(Motorcycle):
    ''' class methods that adhere to the product interface for BMW '''
    def ride(self):
        return "BMW motorcycle is riding"

class FordCar(Car):
    print("This was instantiated??")
    def drive(self):
        return "Ford car is driving"