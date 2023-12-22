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
        self.current_fuel_count = details.get("current_fuel_count", 0)
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

        if self._speed - deceleration < 0:
            self._speed = 0
        else:
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
