'''
Car class is a binary class
'''

class Car:
    '''
    Car class is a binary class
    '''

    def __init__(self, tires, fuel, gas_tank_size, speed, max_speed, brand):
        self.tires = tires
        self.fuel = fuel
        self.max_speed = max_speed
        self.speed = speed
        self.in_progress = speed > 0
        self.brand = brand
        self.gas_tank_size = gas_tank_size

    def reduce_speed(self, speed_to_reduce):
        '''
        Reduce speed if speed is > 0
        '''
        try:
            if self.in_progress and self.speed > 0:
                if self.speed - speed_to_reduce > 0:
                    self.speed -= speed_to_reduce
                    return (self.in_progress, self.speed)
                self.in_progress = False
                self.speed = 0
                raise OverflowError
            raise ValueError
        except ValueError:
            print('Speed is 0; you can\'t reduce speed')
        except OverflowError:
            print('Car stopped. Speed = 0')
            return (self.in_progress, self.speed)
        return self.in_progress, self.speed

    def add_speed(self, additional_speed):
        '''
        Add speed if fuel is available
        '''
        if self.speed + additional_speed < self.max_speed and self.speed != self.max_speed:
            try:
                if self.fuel - 10 > 0:
                    self.speed += additional_speed
                    self.fuel -= 10
                else:
                    raise ValueError
            except ValueError:
                print('Your fuel is 0')
        return self.speed

    def break_(self):
        '''
        Apply the brakes
        '''
        self.speed = 0
        self.in_progress = False
        return self.speed, self.in_progress

    def refuel(self, fuel):
        '''
        Refuel the car
        '''
        if self.fuel + fuel <= self.gas_tank_size:
            self.fuel += fuel
        else:
            self.fuel = self.gas_tank_size
        return self.fuel

    @property
    def tires(self):
        '''
        Return tires
        '''
        return self.tires

    @property
    def fuel(self):
        '''
        Return fuel
        '''
        return self.fuel

    @property
    def max_speed(self):
        '''
        Return max_speed
        '''
        return self.max_speed

    @property
    def speed(self):
        '''
        Return speed
        '''
        return self.speed

    @property
    def brand(self):
        '''
        Return brand
        '''
        return self.brand

    @max_speed.setter
    def max_speed(self, new_max_speed):
        '''
        Set value max_speed
        '''
        self.max_speed = new_max_speed


class PassengerCar(Car):
    '''
    PassengerCar is a class to inherit from Car class
    '''

    def __init__(self, tires, fuel, gas_tank_size, speed, max_speed, brand, passengers_count, passengers_count_now):
        super().__init__(tires, fuel, gas_tank_size, speed, max_speed, brand)
        self.passengers_count = passengers_count
        self.passengers_count_now = passengers_count_now

    def sit_passenger(self, count):
        '''
        Allow passengers to sit if there is enough space
        '''
        if self.passengers_count_now + count <= self.passengers_count:
            self.passengers_count_now += count
        else:
            self.passengers_count_now = self.passengers_count
        return self.passengers_count_now

    @property
    def passengers_count(self):
        '''
        Return passengers_count
        '''
        return self.passengers_count


class Truck(Car):
    '''
    Truck is a class to inherit from Car class
    '''

    def __init__(self, tires, fuel, gas_tank_size, speed, cargo_capacity, max_cargo_capacity):
        super().__init__(tires, fuel, gas_tank_size, speed, max_speed=120, brand="Truck")
        self.cargo_capacity = cargo_capacity
        self.max_cargo_capacity = max_cargo_capacity

    def load_cargo(self, cargo_to_load):
        '''
        Load cargo if not full
        '''
        if self.max_cargo_capacity != self.cargo_capacity:
            if self.cargo_capacity + cargo_to_load <= self.max_cargo_capacity:
                self.cargo_capacity += cargo_to_load
        return self.cargo_capacity

    @property
    def cargo_capacity(self):
        '''
        Return cargo capacity
        '''
        return self.cargo_capacity
class SportCar(PassengerCar):
    def __init__(self, tires, fuel, gas_tank_size, speed, max_speed, brand, passengers_count, passengers_count_now):
        super().__init__(tires, fuel, gas_tank_size, speed, max_speed, brand, passengers_count, passengers_count_now)
