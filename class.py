class Vehicle:
    '''
    Vehicle class is a generic class representing a mode of transportation.
    '''
    def __init__(self, tires, fuel, fuel_tank_size, speed, max_speed, brand):
        self.tires = tires
        self.fuel = fuel
        self.max_speed = max_speed
        self.speed = speed
        self.is_moving = speed > 0
        self.brand = brand
        self.fuel_tank_size = fuel_tank_size

    def decrease_speed(self, speed_to_reduce):
        '''
        Decrease speed if the vehicle is in motion.
        '''
        try:
            if self.is_moving and self.speed > 0:
                if self.speed - speed_to_reduce > 0:
                    self.speed -= speed_to_reduce
                else:
                    self.speed = 0
                    self.is_moving = False
                    raise OverflowError("Vehicle stopped.")
        except OverflowError as e:
            print(str(e))
        except ValueError:
            print("Speed is already 0; you can't reduce it further.")
        return self.is_moving, self.speed

    def increase_speed(self, additional_speed):
        '''
        Increase speed if there is enough fuel.
        '''
        if self.speed + additional_speed < self.max_speed and self.speed != self.max_speed:
            try:
                if self.fuel - 10 > 0:
                    self.speed += additional_speed
                    self.fuel -= 10
                else:
                    raise ValueError("Out of fuel.")
            except ValueError as e:
                print(str(e))
        return self.speed

    def apply_brakes(self):
        '''
        Apply the brakes and bring the vehicle to a stop.
        '''
        self.speed = 0
        self.is_moving = False
        return self.speed, self.is_moving

    def refuel(self, fuel):
        '''
        Refuel the vehicle.
        '''
        if self.fuel + fuel <= self.fuel_tank_size:
            self.fuel += fuel
        else:
            self.fuel = self.fuel_tank_size
        return self.fuel

class PassengerVehicle(Vehicle):
    '''
    PassengerVehicle is a class that inherits from the Vehicle class.
    '''
    def __init__(self, tires, fuel, fuel_tank_size, speed, max_speed, brand, passenger_capacity, current_passenger_count):
        super().__init__(tires, fuel, fuel_tank_size, speed, max_speed, brand)
        self.passenger_capacity = passenger_capacity
        self.current_passenger_count = current_passenger_count

    def board_passengers(self, count):
        '''
        Allow passengers to board if there is enough space.
        '''
        if self.current_passenger_count + count <= self.passenger_capacity:
            self.current_passenger_count += count
        else:
            self.current_passenger_count = self.passenger_capacity
        return self.current_passenger_count

class DeliveryTruck(Vehicle):
    '''
    DeliveryTruck is a class that inherits from the Vehicle class.
    '''
    def __init__(self, tires, fuel, fuel_tank_size, speed, cargo_capacity, max_cargo_capacity):
        super().__init__(tires, fuel, fuel_tank_size, speed, max_speed=120, brand="Truck")
        self.cargo_capacity = cargo_capacity
        self.max_cargo_capacity = max_cargo_capacity

    def load_cargo(self, cargo_to_load):
        '''
        Load cargo if there is available space.
        '''
        if self.cargo_capacity + cargo_to_load <= self.max_cargo_capacity:
            self.cargo_capacity += cargo_to_load
        return self.cargo_capacity