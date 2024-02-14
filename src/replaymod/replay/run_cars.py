from car_factory import MercedesFactory, BMWFactory

def create_vehicle(factory) -> list:
    car = factory.create_car()
    motorcycle = factory.create_motorcycle()
    return [car, motorcycle]

# Note: 
'''
The Abstract Factory pattern enables us to switch
between brands seamlessly without modifying the client code
'''

def run():
    # Using Mercedes Factory
    mercedes_factory = MercedesFactory()
    # create vehicles using different concrete factories for Mercedes
    mercedes_car, mercedes_motorcycle = create_vehicle(mercedes_factory)
    print(mercedes_car.drive()) # Output: Mercedes car is driving
    print(mercedes_motorcycle.ride()) # Output: Mercedes motorcycle is riding.

    # Using BMW Factory
    bmw_factory = BMWFactory()
    # create vehicles using different concrete factories for BMW
    bmw_car, bmw_motorcycle = create_vehicle(bmw_factory)
    print(bmw_car.drive()) # Output: BMW car is driving
    print(bmw_motorcycle.ride()) # Output: BMW motorcycle is riding


if __name__ == '__main__':
    run()