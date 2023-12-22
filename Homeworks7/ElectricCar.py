from Car import Car


class ElectricCar(Car):
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
