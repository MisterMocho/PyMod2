def water_plants(plant_list: list[object]) -> None:
    """System that closes the water even if errors occurr"""
    print("Opening watering system")
    has_error = False
    try:
        for plant in plant_list:
            if not isinstance(plant, str):
                raise TypeError(f"Cannot water {plant} - invalid plant!")
            print(f"Watering {plant}")
    except TypeError as e:
        print(f"Error: {e}")
        has_error = True
    finally:
        print("Closing watering system (cleanup)")
    if has_error:
        print("")
    else:
        print("Watering completed successfully!\n")


def test_watering_system() -> None:
    print("=== Garden Watering System ===\n")
    good_garden: list[object] = [
        "tomato",
        "lettuce",
        "carrots"
    ]
    bad_garden: list[object] = [
        "tomato",
        123,
        "carrots"
    ]
    print("Testing normal watering...")
    water_plants(good_garden)
    print("Testing with error...")
    water_plants(bad_garden)
    print("Cleanup always happens, even with errors!")


if __name__ == "__main__":
    test_watering_system()
