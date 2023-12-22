from Car import Car


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
