"""
    Sedan class inherited by Car class
"""

from car import Car


class Sedan(Car):
    """
    Sedan class inherited by Car class attributes,
    has its own attributes.
    """

    def __init__(self, details):
        """
        Initializes sedan details.

        details: Dictionary containing sedan details.
        """

        super().__init__(details)
        self.trunk_capacity = details.get("trunk_capacity", 0)
        self.trunk_status = "closed"

    def open_trunk(self):
        """
        Open the trunk.
        """

        if self.trunk_status == "closed":
            print("Trunk opened.")
            self.trunk_status = "opened"
        else:
            print("Trunk is already opened.")

    def close_trunk(self):
        """
        Close the trunk.
        """

        if self.trunk_status == "opened":
            print("Trunk closed.")
            self.trunk_status = "closed"
        else:
            print("Trunk is already closed.")


sedan = Sedan(
    {
        "brand": "BMW",
        "model": "M3",
        "color": "Black",
        "wheels_count": 4,
        "doors_count": 4,
        "motor_type": "Fuel engine",
        "fuel_type": "Gasoline",
        "fuel_tank": 63,
        "current_fuel_count": 63,
        "top_speed": "302km/h",
        "weight": 1570,
        "seats_count": 5,
        "trunk_capacity": 0.5,
    }
)

sedan.show_details()
sedan.accelerate(60)
sedan.show_speed()
sedan.decelerate(30)
sedan.show_status()
sedan.refuel(30)
sedan.stop_engine()
