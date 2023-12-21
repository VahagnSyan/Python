class Car:
    def __init__(self, details):
        """
        Initializes car details.
        details: Dictionary containing car details.
        """

        self.brand = details.get("brand", "Unknown Brand")
        self.model = details.get("model", "Unknown Model")
        self.color = details.get("color", "Unknown Color")
        self.wheels_count = details.get("wheels_count", 0)
        self.doors_count = details.get("doors_count", 0)
        self.motor_type = details.get("motor_type", "Unknown Motor Type")
        self.fuel_type = details.get("fuel_type", "Unknown Fuel Type")
        self.fuel_tank = details.get("fuel_tank", "Unknown Fuel Tank")
        self.trunk_capacity = details.get("trunk_capacity", "Unknown Trunk Capacity")
        self.current_fuel_count = details.get(
            "current_fuel_count", "Unknown Current Fuel Count"
        )
        self.top_speed = details.get("top_speed", "Unknown Top Speed")
        self.weight = details.get("weight", 0)
        self.seats_count = details.get("seats_count", "Unknown Seats Count")
        self._status = "Stationary"
        self._speed = 0

    def show_details(self):
        """
        Display car details.
        """

        print(f"Brand: {self.brand}")
        print(f"Model: {self.model}")
        print(f"Color: {self.color}")
        print(f"Wheels Count: {self.wheels_count}")
        print(f"Doors Count: {self.doors_count}")
        print(f"Motor Type: {self.motor_type}")
        print(f"Fuel Type: {self.fuel_type}")
        print(f"Fuel Tunk: {self.fuel_tank} litres")
        print(f"Current Fuel Count: {self.current_fuel_count} litres")
        print(f"Top Speed: {self.top_speed}")
        print(f"Weight: {self.weight} kg")
        print(f"Seats Count: {self.seats_count}")
        print(f"Trunk Capacity: {self.trunk_capacity} cubic meters")

    def set_speed(self, speed):
        if not isinstance(speed, (int, float)):
            # Checks if provided speed value is numerical
            print("Speed must be a numerical value.")
            return

        # Updates speed, status and current fuel count
        # based on provided speed value
        self._speed = speed
        if speed > 0:
            self._status = "Moving"
            self.current_fuel_count -= 1
        elif speed == 0:
            self._status = "Stationary"
        else:
            print("Car speed cannot be a negative value.")

    def show_speed(self):
        """
        Display the current speed of the car.
        """

        print(f"Current speed: {self._speed}km/h")

    def show_status(self):
        """
        Display the current status of the car.
        """

        print(f"Current status: {self._status}")

    def refuel(self, amount):
        """
        Refuel the car.
        amount: Amount of fuel to add.
        """

        if not isinstance(amount, (int, float)) or amount < 0:
            print("Invalid fuel amount.")
            return

        if not isinstance(self.current_fuel_count, (int, float)) or not isinstance(
            self.fuel_tank, (int, float)
        ):
            print("Unknown Current Fuel Count and Fuel Tunk Capacity.")
            return

        if self.current_fuel_count + amount > self.fuel_tank:
            print("Amout of fuel is bigger than fuel tunk capacity.")
        else:
            self.current_fuel_count += amount
            print(f"Car refueled. Current fuel count: {self.current_fuel_count} litres")

    def accelerate(self, acceleration):
        """
        Accelerate the car.
        acceleration: Rate of acceleration.
        """

        if acceleration < 0:
            print("Acceleration must be a non-negative value.")
            return

        self.set_speed(self._speed + acceleration)

    def decelerate(self, deceleration):
        """
        Decelerate the car.
        deceleration: Rate of deceleration.
        """

        if deceleration < 0:
            print("Deceleration must be a non-negative value.")
            return

        self.set_speed(self._speed - deceleration)

    def start_engine(self):
        """Start the car engine."""

        if self._status == "Stationary":
            print("Engine started.")
        else:
            print("Cannot start engine while moving.")

    def stop_engine(self):
        """Stop the car engine."""

        if self._status == "Stationary":
            print("Engine already stopped.")
        else:
            print("Engine stopped.")
            self.set_speed(0)


class Sedan(Car):
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


class Minivan(Car):
    def __init__(self, details):
        """
        Initializes minivan details.
        details: Dictionary containing minivan details.
        """

        super().__init__(details)
        self.has_sliding_doors = details.get("has_sliding_doors", False)
        self.sliding_doors_status = "closed"

    def open_sliding_doors(self):
        """
        Open the sliding doors.
        """

        if self.has_sliding_doors:
            if self.sliding_doors_status == "closed":
                print("Sliding doors opened.")
                self.sliding_doors_status = "opened"
            else:
                print("Sliding doors are already opened.")
        else:
            print("This minivan does not have sliding doors.")

    def close_sliding_doors(self):
        """
        Close the sliding doors.
        """

        if self.has_sliding_doors:
            if self.sliding_doors_status == "opened":
                print("Sliding doors closed.")
                self.sliding_doors_status = "closed"
            else:
                print("Sliding doors are already closed.")
        else:
            print("This minivan does not have sliding doors.")


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


class Truck(Car):
    def __init__(self, details):
        super().__init__(details)
        self.payload_capacity = details.get("payload_capacity", 0)
        self.towing_capacity = details.get("towing_capacity", 0)
        self.bed_size = details.get("bed_size", "Unknown")

    def show_details(self):
        """
        Display truck details.
        """

        print(f"Brand: {self.brand}")
        print(f"Model: {self.model}")
        print(f"Color: {self.color}")
        print(f"Wheels Count: {self.wheels_count}")
        print(f"Doors Count: {self.doors_count}")
        print(f"Motor Type: {self.motor_type}")
        print(f"Payload Capacity: {self.payload_capacity} kg")
        print(f"Towing Capacity: {self.towing_capacity} kg")
        print(f"Bed Size: {self.bed_size}")
        print(f"Top Speed: {self.top_speed}")
        print(f"Weight: {self.weight} kg")
        print(f"Seats Count: {self.seats_count}")


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

minivan = Minivan(
    {
        "brand": "Mercedes",
        "model": "K4",
        "color": "White",
        "wheels_count": 4,
        "doors_count": 6,
        "motor_type": "Fuel engine",
        "fuel_type": "Gasoline",
        "top_speed": "253km/h",
        "weight": 2070,
        "seats_count": 7,
        "has_sliding_doors": True,
    }
)

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

truck = Truck(
    {
        "brand": "Ford",
        "model": "F-150",
        "color": "Blue",
        "wheels_count": 4,
        "doors_count": 4,
        "motor_type": "Fuel engine",
        "fuel_type": "Gasoline",
        "fuel_tank": 80,
        "current_fuel_count": 80,
        "top_speed": "180 km/h",
        "weight": 2500,
        "seats_count": 3,
        "payload_capacity": 1000,
        "towing_capacity": 5000,
        "bed_size": "Short",
    }
)
