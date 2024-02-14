import pytest

from api.engine import Engine

from replay.car_factory import MercedesFactory, BMWFactory


def calculate_startup(x):
    print(f"Value is {x}")

def create_vehicle(factory) -> list:
    car = factory.create_car()
    motorcycle = factory.create_motorcycle()
    return [car, motorcycle]

@pytest.fixture
def pass_gen(request) -> str:
    """
    Fixture to accept the length and number of characters input from the command line.
    :param request: pytest request object

    :return: String of length and number of alpha num characters
    """
    # Taking passed args for length and number of chars
    custom = request.config.getoption("--custom-option")

    yield custom


# Note: fixture function cannot have more than one yield
@pytest.fixture
def setup_data():
    # data = 5  # Set up a sample number
    # print("\nSetting up resources...")
    # yield data  # Provide the data to the test

    engine_type = 'V6'
    print("\nSetting up engine...")

    engine = Engine()
    engine_startup = engine.engneStartUp(engine_type)
    yield engine_startup # Provide the engine_startup to the test

    # Teardown: Clean up resources (if any) after the test
    print("\nTearing down resources...")


'''
@pytest.fixture
def setup_data(request):
    print("\nSetting up resources...")
    data = 5
    
    # Define a finalizer function for teardown
    def finalizer():
        print("\nPerforming teardown...")
        # Clean up any resources if needed

    # Register the finalizer to ensure cleanup
    request.addfinalizer(finalizer)

    return data  # Provide the data to the test
'''


# Test cases
'''
@pytest.mark.env("stage2")
def test_square_positive_number(setup_data):
    result = calculate_square(setup_data)
    assert result == 25
    print("Running test case for positive number")
'''

@pytest.mark.darwin
def test_if_apple_is_evil():
    pass

@pytest.mark.skip(reason="JIRA: Advanced Operations issues - skipping!")
def test_advanced_db_operation():
    pass

# Note: Running with  "pytest -v -s -E staging" the below test will be skipped
@pytest.mark.env("stage1")
def test_basic_db_operation():
    pass


def test_custom_option(request):
    env_value = request.config.getoption("-E")
    print(f"Custom Environment option value: {env_value}")


# Test function
def test_pass_gen(pass_gen) -> None:
    custom_value = pass_gen
    assert custom_value == 'me2'

def test_custom_option(request):
    custom_value = request.config.getoption("--custom-option")
    print(f"Custom option value: {custom_value}")


@pytest.mark.webtest
def test_web_framework(setup_data) -> None:
    # answer = calculate_startup(setup_data)
    # assert answer == False
    # print("*******************************")
    # if answer:
    if setup_data == 'Engine Started':
        response = 200
        assert response == 404
        print("Running test case for web test...")

@pytest.mark.webtest
class TestClass:
    def test_startup(self):
        pass

    def test_startup_and_more(self):
        pass


@pytest.mark.slow
class TestCarSuite:
    """Car test cases."""

    # def setUp(self):
    #     print("setUp initiated")
    #     self.engine = engineStartUp("V6")

    @pytest.mark.database_access
    def test_database_access(self):
        assert True

    @pytest.mark.env('staging')
    @pytest.mark.parametrize("car_brand", [
        "",
        "BMW",
        "Mercedes",
    ])
    def test_car_creation_for_brands(self, car_brand):
        # TODO: is there a better way to check car brand and determine which code path to use?
        if car_brand == 'Mercedes':
            # Using Mercedes Factory
            mercedes_factory = MercedesFactory()
            # create vehicles using different concrete factories for Mercedes
            mercedes_car, mercedes_motorcycle = create_vehicle(mercedes_factory)
            print(mercedes_car.drive()) # Output: Mercedes car is driving
            print(mercedes_motorcycle.ride()) # Output: Mercedes motorcycle is riding.
            assert mercedes_motorcycle.ride() == "Mercedes is riding!"
        elif car_brand == 'BMW':
            # Using BMW Factory
            bmw_factory = BMWFactory()
            # create vehicles using different concrete factories for BMW
            bmw_car, bmw_motorcycle = create_vehicle(bmw_factory)
            print(bmw_car.drive()) # Output: BMW car is driving
            print(bmw_motorcycle.ride()) # Output: BMW motorcycle is riding
            assert bmw_car.drive() == "BMW car is driving"
        else:
            print(f"Invalid car brand {car_brand} was specified!")

    
    # def tearDown(self):
    #     print("Tearing down!!")
