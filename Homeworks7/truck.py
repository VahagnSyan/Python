"""Truck class inherited by Car class"""

from car import Car


class Truck(Car):
    """
    Truck class inherited by Car class attributes,
    has its own attributes.
    """

    def __init__(self, details):
        super().__init__(details)
        self.payload_capacity = details.get("payload_capacity", 0)
        self.current_payload_capacity = details.get("current_payload_capacity", 0)
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

    def load_payload(self, payload):
        """
        Load payload into the car.
        payload: Amount of payload to add.
        """

        if not isinstance(payload, (int, float)) or payload < 0:
            print("Invalid payload amount.")
            return

        if self.current_payload_capacity + payload > self.payload_capacity:
            print("Payload exceeds the available capacity.")
        else:
            self.current_payload_capacity += payload
            print(
                f"Payload loaded. Current payload capacity: {self.current_payload_capacity} kg"
            )

    def unload_payload(self, payload):
        """
        Unload payload from the car.
        payload: Amount of payload to remove.
        """

        if not isinstance(payload, (int, float)) or payload < 0:
            print("Invalid payload amount.")
            return

        if self.current_payload_capacity - payload < 0:
            print("Payload cannot be unloaded beyond current capacity.")
        else:
            self.current_payload_capacity -= payload
            print(
                f"Payload unloaded. Current payload capacity: {self.current_payload_capacity} kg"
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


truck.show_details()
truck.accelerate(60)
truck.show_speed()
truck.decelerate(30)
truck.show_status()
truck.load_payload(900)
truck.show_details()
truck.unload_payload(800)
truck.stop_engine()
