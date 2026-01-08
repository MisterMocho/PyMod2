class GardenError(Exception):
    """class that manages all garden related errors"""
    pass


class PlantError(GardenError):
    """class that manages errors related to plants"""
    pass


class WaterError(GardenError):
    """class that manages errors related to watering"""
    pass


class GardenManager:
    """Adds, manages and handles all the plants and inner systems"""
    def __init__(self) -> None:
        self.plants: list[tuple[str, int, int]] = []

    def add_plant(self, name: str, water_level: int, sun: int) -> None:
        """Adds a valid named plant to the garden"""
        try:
            if not name:
                raise ValueError("Plant name cannot be empty!")
            self.plants.append((name, water_level, sun))
            print(f"Added {name} successfully")
        except ValueError as e:
            print(f"Error adding plant: {e}\n")

    def water_plants(self) -> None:
        """Uses finally block to always cleanup if it encounters errors"""
        print("Opening watering system")
        try:
            for name, _, _ in self.plants:
                print(f"Watering {name} - success")
        except Exception as e:
            print(f"Error during watering: {e}")
        finally:
            print("Closing watering system (cleanup)\n")

    def check_plant_health(self) -> None:
        """Checks plant stats and raises invalid data"""
        for name, water, sun in self.plants:
            try:
                if not (1 <= water <= 10):
                    reason = "low (min 1)" if water < 1 else "high (max 10)"
                    raise WaterError(f"Water level {water} is too {reason}")
                if not (2 <= sun <= 12):
                    reason = "low (min 2)" if sun < 2 else "high (max 12)"
                    raise PlantError(f"Sunlight hours {sun} is too {reason}")
                print(f"{name}: healthy (water: {water}, sun: {sun})")
            except GardenError as e:
                print(f"Error checking {name}: {e}")
        print()

    def error_recovery(self) -> None:
        """Function to test unexpected error and system recovery"""
        try:
            raise WaterError("Not enough water in tank")
        except GardenError as e:
            print(f"Caught GardenError: {e}")
        finally:
            print("System recovered and continuing...\n")


def test_garden_system() -> None:
    """Function that tests GM capabilities and error handling"""
    print("=== Garden Management System ===\n")
    man = GardenManager()
    print("Adding plants to garden...")
    man.add_plant("tomato", 5, 8)
    man.add_plant("lettuce", 15, 5)
    man.add_plant("", 5, 5)
    print("Watering plants...")
    man.water_plants()
    print("Checking plant health...")
    man.check_plant_health()
    print("Testing error recovery...")
    man.error_recovery()
    print("Garden management system test complete!")


if __name__ == "__main__":
    test_garden_system()
