class GardenError(Exception):
    """class that manages all garden related errors"""
    pass


class PlantError(GardenError):
    """class that manages errors related to plants"""
    pass


class WaterError(GardenError):
    """class that manages errors related to watering"""
    pass


def plant_error() -> None:
    """Raises PlantError"""
    raise PlantError("The tomato plant is wilting!")


def water_error() -> None:
    """Raises a WaterError"""
    raise WaterError("Not enough water in the tank")


def test_errors() -> None:
    """Tests all the custom created errors"""
    print("=== Custom Garden Errors Demo ===\n")
    errors = [plant_error, water_error]
    print("Testing PlantError...")
    try:
        plant_error()
    except PlantError as e:
        print(f"Caught PlantError: {e}\n")
    print("Testing WaterError...")
    try:
        water_error()
    except WaterError as e:
        print(f"Caught WaterError: {e}\n")
    print("Testing catching all garden errors...")
    for test in errors:
        try:
            test()
        except GardenError as e:
            print(f"Caught a garden error: {e}")
    print("\nAll custom error types work correctly!")


if __name__ == "__main__":
    test_errors()
