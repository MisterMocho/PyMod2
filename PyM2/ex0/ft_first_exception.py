def check_temperature(temp_str: str):
    """function that handles inputs and validates them"""
    try:
        temp = int(temp_str)
        if (temp > 40):
            print(f"Error: {temp}°C is too hot for plants (max 40°C)\n")
        elif (temp < 0):
            print(f"Error: {temp}°C is too cold for plants (min 0°C)\n")
        else:
            print(f"Temperature {temp}°C is perfect for plants!\n")
            return (temp)

    except ValueError:
        print(f"Error: '{temp_str}' is not a valid number\n")


def test_temperature_input() -> None:
    """temperature testing function"""
    print("=== Garden Temperature Checker ===\n")
    test_cases: list[str] = ["25", "abc", "100", "-50"]
    for tests in test_cases:
        print(f"Testing temperature: {tests}")
        check_temperature(tests)
    print("All tests completed - program didn't crash!")


if __name__ == "__main__":
    test_temperature_input()
