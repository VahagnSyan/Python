"""
Electric car class inherited by Car Base class
"""

from car import Car


class ElectricCar(Car):
    """
    Electric car class inherited by Car Base class,
    has its own attributes.
    """

    def __init__(self, details):
        super().__init__(details)
        self.battery_capacity = details.get("battery_capacity", 0)
        self.charge_level = details.get("charge_level", 100)

    def show_details(self):
        """
        Display electric car details.
        """

        print(f"Brand: {self.brand}")
        print(f"Model: {self.model}")
        print(f"Color: {self.color}")
        print(f"Wheels Count: {self.wheels_count}")
        print(f"Doors Count: {self.doors_count}")
        print(f"Motor Type: {self.motor_type}")
        print(f"Battery Capacity: {self.battery_capacity} kWh")
        print(f"Charge Level: {self.charge_level}%")
        print(f"Top Speed: {self.top_speed}")
        print(f"Weight: {self.weight} kg")
        print(f"Seats Count: {self.seats_count}")

    def charge(self, duration):
        """
        Charge the electric car.
        duration: Charging duration in hours.
        """

        # Update charge level based on charging duration
        self.charge_level += duration
        print(f"Car charged. Current charge level: {self.charge_level}%")

    def refuel(self, amount):
        """
        Override the refuel method for ElectricCar.
        This method is empty as electric cars don't use fuel.
        """

        print("Electric cars don't require refueling.")


electric_car = ElectricCar(
    {
        "brand": "Tesla",
        "model": "Model 4",
        "color": "White",
        "wheels_count": 4,
        "doors_count": 6,
        "motor_type": "Electric",
        "fuel_type": "Electric",
        "top_speed": "453km/h",
        "weight": 2070,
        "seats_count": 6,
        "has_sliding_doors": False,
        "battery_capacity": 300,
        "charge_level": 250,
    }
)

electric_car.show_details()
electric_car.accelerate(60)
electric_car.show_speed()
electric_car.decelerate(30)
electric_car.show_status()
electric_car.refuel(2)
electric_car.stop_engine()
