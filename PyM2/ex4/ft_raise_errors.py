def check_plant_health(plant_name: str, water_level: int,
                       sunlight_hours: int) -> None:
    """Value checker and error handling in case values are bad"""
    if plant_name == "":
        raise ValueError("Error: Plant name cannot be empty!")
    elif not (1 <= water_level <= 10):
        if (water_level < 1):
            raise ValueError(
                f"Error: Water level {water_level} is too low (min 1)"
                )
        elif (water_level > 10):
            raise ValueError(
                f"Error: Water level {water_level} is too high (max 10)"
                )
    elif not (2 <= sunlight_hours <= 12):
        if (sunlight_hours < 2):
            raise ValueError(
                f"Error: Sunlight hours {sunlight_hours} is too low (min 2)"
                )
        elif (sunlight_hours > 12):
            raise ValueError(
                f"Error: Sunlight hours {sunlight_hours} is too high (max 12)"
                )
    else:
        print(f"Plant '{plant_name}' is healthy!\n")


def test_plant_checks() -> None:
    """Function to test the plant health function with good and bad input"""
    print("=== Garden Plant Health Checker ===\n")
    print("Testing good values...")
    try:
        check_plant_health("tomato", 5, 5)
    except ValueError as e:
        print(f"{e}\n")
    print("Testing empty plant name...")
    try:
        check_plant_health("", 5, 5)
    except ValueError as e:
        print(f"{e}\n")
    print("Testing bad water level...")
    try:
        check_plant_health("tomato", 15, 5)
    except ValueError as e:
        print(f"{e}\n")
    print("Testing bad sunlight hours...")
    try:
        check_plant_health("tomato", 5, 0)
    except ValueError as e:
        print(f"{e}\n")
    print("All error raising tests completed!")


if __name__ == "__main__":
    test_plant_checks()
