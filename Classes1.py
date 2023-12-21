class Car:
    def __init__(self, tires, fuel, max_speed):
        self.tires = tires
        self.fuel = fuel
        self.max_speed = max_speed

    def drive(self, hours, speed):
        distance = hours * speed
        return f"The car traveled {distance} kilometers."

    def refuel(self, amount):
        self.fuel += amount
        return f"Refueled the car. Current fuel level: {self.fuel} liters."

class PassengerCar(Car):
    def __init__(self, tires, fuel, max_speed, passengers):
        super().__init__(tires, fuel, max_speed)
        self.passengers = passengers

    def play_music(self):
        return "Playing some cool tunes!"

    def passenger_count(self):
        return f"The car has {self.passengers} passengers on board."

    def customize_car(self, color):
        return f"Customizing the car with the color: {color}"

class Truck(Car):
    def __init__(self, tires, fuel, max_speed, cargo_capacity):
        super().__init__(tires, fuel, max_speed)
        self.cargo_capacity = cargo_capacity

    def load_cargo(self):
        return "Loading cargo into the truck."

    def check_cargo_capacity(self):
        return f"The truck has a cargo capacity of {self.cargo_capacity} tons."

    def spray_paint(self, color):
        return f"Spray painting the truck with the color: {color}"

class ElectricCar(PassengerCar):
    def __init__(self, tires, battery_life, passengers):
        super().__init__(tires, 100, 120, passengers)
        self.battery_life = battery_life

    def charge_battery(self, hours):
        self.battery_life += hours
        return f"Charging the electric car's battery. Current battery life: {self.battery_life} hours."

    def change_color(self, color):
        return f"Changing the electric car's color to: {color}"

class SportsCar(PassengerCar):
    def __init__(self, tires, fuel, max_speed, passengers, spoiler):
        super().__init__(tires, fuel, max_speed, passengers)
        self.spoiler = spoiler

    def activate_spoiler(self):
        return "Activating the spoiler for better aerodynamics."

    def high_speed_drive(self):
        return f"The sports car is zooming at {self.max_speed + 20} km/h!"

    def customize_car(self, decal):
        return f"Customizing the sports car with a decal: {decal}"

class Van(Truck):
    def __init__(self, tires, fuel, max_speed, cargo_capacity, passenger_capacity):
        super().__init__(tires, fuel, max_speed, cargo_capacity)
        self.passenger_capacity = passenger_capacity

    def carry_passengers(self):
        return f"The van is carrying {self.passenger_capacity} passengers."

class PickupTruck(Truck):
    def __init__(self, tires, fuel, max_speed, cargo_capacity, towing_capacity):
        super().__init__(tires, fuel, max_speed, cargo_capacity)
        self.towing_capacity = towing_capacity

    def tow_trailer(self):
        return f"The pickup truck is towing a trailer with a capacity of {self.towing_capacity} tons."

# Function to get numeric input
def get_numeric_input(prompt):
    while True:
        try:
            value = float(input(prompt))
            return value
        except ValueError:
            print("Invalid input. Please enter a numeric value.")

# Create instances  PassengerCar, Van, and PickupTruck 
tires_passenger_car = 4
fuel_passenger_car = 50
max_speed_passenger_car = 180
passengers_passenger_car = 4

passenger_car = PassengerCar(tires=tires_passenger_car, fuel=fuel_passenger_car, max_speed=max_speed_passenger_car, passengers=passengers_passenger_car)

# Create instances  Van and PickupTruck
van = Van(tires=4, fuel=60, max_speed=150, cargo_capacity=3, passenger_capacity=8)
pickup_truck = PickupTruck(tires=6, fuel=70, max_speed=120, cargo_capacity=5, towing_capacity=2)

#  PassengerCar
print(passenger_car.drive(hours=2, speed=60))
print(passenger_car.play_music())
print(passenger_car.passenger_count())
print()

# Van
print(van.drive(hours=1, speed=50))
print(van.load_cargo())
print(van.check_cargo_capacity())
print(van.spray_paint(color="blue"))
print(van.carry_passengers())
print()

# PickupTruck
print(pickup_truck.drive(hours=2, speed=80))
print(pickup_truck.load_cargo())
print(pickup_truck.check_cargo_capacity())
print(pickup_truck.spray_paint(color="red"))
print(pickup_truck.tow_trailer())
print()
