import unittest
import nose2
from nose2.tools.decorators import with_setup
from nose2.tools.decorators import with_teardown
from nose2.tools import params

from api.engine import Engine

from replay.car_factory import MercedesFactory, BMWFactory


def create_vehicle(factory) -> list:
    car = factory.create_car()
    motorcycle = factory.create_motorcycle()
    return [car, motorcycle]


def setup_func():
    print("set up test fixtures")
    import pdb;pdb.set_trace()
    startup = Engine.engneStartUp()

def teardown_func():
    print("tear down test fixtures")

class CarTestSuite(unittest.TestCase):
    """Car test cases."""

    # def setUp(self):
    #     print("setUp initiated")
    #     self.engine = engineStartUp("V6")

    @with_setup(setup_func)
    def test_absolute_truth_and_meaning(self):
        assert True


    @params('BMW', 'Mercedes')
    def test_car_creation_for_brands(self, car_brand):
        # TODO: is there a better way to check car brand and determine which code path to use?
        if car_brand == 'Mercedes':
            # Using Mercedes Factory
            mercedes_factory = MercedesFactory()
            # create vehicles using different concrete factories for Mercedes
            mercedes_car, mercedes_motorcycle = create_vehicle(mercedes_factory)
            print(mercedes_car.drive()) # Output: Mercedes car is driving
            print(mercedes_motorcycle.ride()) # Output: Mercedes motorcycle is riding.
            self.assertEquals(mercedes_motorcycle.ride(), "Mercedes is riding!")
        elif car_brand == 'BMW':
            # Using BMW Factory
            bmw_factory = BMWFactory()
            # create vehicles using different concrete factories for BMW
            bmw_car, bmw_motorcycle = create_vehicle(bmw_factory)
            print(bmw_car.drive()) # Output: BMW car is driving
            print(bmw_motorcycle.ride()) # Output: BMW motorcycle is riding
            self.assertEquals(bmw_car.drive(), "BMW car is driving")
        else:
            print(f"Invalid car brand {car_brand} was specified!")

    
    # def tearDown(self):
    #     print("Tearing down!!")




if __name__ == '__main__':
    # unittest.main()
    # nose2.main()
    nose2.run(defaultTest=__name__)
