"""
Car base class to derive default attributes to derived classes
"""
import dataclasses


@dataclasses.dataclass
class ExternalDetails:
    """
    ExternalDetails class to initialize external details in Car class
    """

    brand: str
    model: str
    color: str
    wheels_count: int
    doors_count: int
    seats_count: int


@dataclasses.dataclass
class InternalDetails:
    """
    InternalDetails class to initialize internal details in Car class
    """

    motor_type: str
    trunk_capacity: int
    weight: int


@dataclasses.dataclass
class Fuel:
    """
    Fuel class to initialize fuel details in Car class
    """

    type: str
    tank: int
    current_fuel_count: int


class Car:
    """
    Base class of instances Car
    """

    def __init__(self, details):
        """
        Initializes car details.
        details: Dictionary containing car details.
        """

        self.external_details = ExternalDetails(
            brand=details.get("brand", "Unknown Brand"),
            model=details.get("model", "Unknown Model"),
            color=details.get("color", "Unknown Color"),
            wheels_count=details.get("wheels_count", 0),
            doors_count=details.get("doors_count", 0),
            seats_count=details.get("seats_count", "Unknown Seats Count"),
        )
        self.fuel = Fuel(
            type=details.get("fuel_type", "Unknown Fuel Type"),
            tank=details.get("fuel_tank", "Unknown Fuel Tank"),
            current_fuel_count=details.get("current_fuel_count", 0),
        )
        self.internal_details = InternalDetails(
            motor_type=details.get("motor_type", "Unknown Motor Type"),
            trunk_capacity=details.get("trunk_capacity", "Unknown Trunk Capacity"),
            weight=details.get("weight", 0),
        )

        self.top_speed = details.get("top_speed", "Unknown Top Speed")
        self._status = "Stationary"
        self._speed = 0

    def show_details(self):
        """
        Display car details.
        """

        print(f"Brand: {self.external_details.brand}")
        print(f"Model: {self.external_details.model}")
        print(f"Color: {self.external_details.color}")
        print(f"Wheels Count: {self.external_details.wheels_count}")
        print(f"Doors Count: {self.external_details.doors_count}")
        print(f"Motor Type: {self.internal_details.motor_type}")
        print(f"Fuel Type: {self.fuel.type}")
        print(f"Fuel Tunk: {self.fuel.tank} litres")
        print(f"Current Fuel Count: {self.fuel.current_fuel_count} litres")
        print(f"Top Speed: {self.top_speed}")
        print(f"Weight: {self.internal_details.weight} kg")
        print(f"Seats Count: {self.external_details.seats_count}")
        print(f"Trunk Capacity: {self.internal_details.trunk_capacity} cubic meters")

    def set_speed(self, speed):
        """
        Change speed of car
        """

        if not isinstance(speed, (int, float)):
            # Checks if provided speed value is numerical
            print("Speed must be a numerical value.")
            return

        # Updates speed, status and current fuel count
        # based on provided speed value
        self._speed = speed
        if speed > 0:
            self._status = "Moving"
            self.fuel.current_fuel_count -= 1
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

        if not isinstance(self.fuel.current_fuel_count, (int, float)) or not isinstance(
            self.fuel.tank, (int, float)
        ):
            print("Unknown Current Fuel Count and Fuel Tunk Capacity.")
            return

        if self.fuel.current_fuel_count + amount > self.fuel.tank:
            print("Amout of fuel is bigger than fuel tunk capacity.")
        else:
            self.fuel.current_fuel_count += amount
            print(
                f"Car refueled. Current fuel count: {self.fuel.current_fuel_count} litres"
            )

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
