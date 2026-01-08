def garden_operations(test: str) -> None:
    """Function that forces different errors depending on input"""
    if (test == "ValueError"):
        int("abc")
    elif (test == "ZeroDivisionError"):
        20 / 0
    elif (test == "FileNotFoundError"):
        open("epstein_files.txt")
    elif (test == "KeyError"):
        my_bible = {}
        my_bible["Missing_Jesus"]


def test_error_types() -> None:
    """Function that catches the errors, explains and prevents them"""
    print("=== Garden Error Types Demo ===\n")
    errors: list[str] = [
        "ValueError",
        "ZeroDivisionError",
        "FileNotFoundError",
        "KeyError"
    ]
    for error in errors:
        try:
            print(f"Testing {error}...")
            garden_operations(error)
        except ValueError:
            print(f"Caught {error}: invalid literal for int()\n")
        except ZeroDivisionError:
            print(f"Caught {error}: division by zero\n")
        except FileNotFoundError as e:
            print(f"Caught {error}: No such file '{e.filename}'\n")
        except KeyError as e:
            print(f"Caught {error}: {e}\n")
    print("Testing multiple errors together...")
    try:
        garden_operations(errors[1])
    except (ValueError, ZeroDivisionError, FileNotFoundError, KeyError):
        print("Caught an error, but program continues!\n")
    print("All error types tested successfully!")


if __name__ == "__main__":
    test_error_types()
