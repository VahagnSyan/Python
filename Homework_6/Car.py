class Car:
    '''
    The base class from which all other type car should inherit
    '''


    # Creation of basic attributes belonging to the car
    def __init__(self, model, car_class, max_speed_size, fuel, speed, 
                 door_count, wheel_count, person_count, fuel_tank, tug):
        self.model = model
        self.car_class = car_class
        self.max_speed_size = max_speed_size
        self.fuel = fuel
        self.speed = speed
        self.door_count = door_count
        self.whell_count = wheel_count
        self.person_count = person_count
        self.fuel_tank = fuel_tank
        self.tug = tug


    # A helper function that checks whether the input data is correct or not
    def __inputcheck__(self, value, text):
        if (type(value) == int or type(value) == float) and value > 0:
            return True
        else:
            print(f'\033[91m{text} must be a positive number!\033[0m')
            return False


    # Increases the speed of the car by the given value
    def speed_up(self, speed):
        if 0 < self.fuel <= self.fuel_tank:
            if self.__inputcheck__(speed, 'Speed'):
                if self.speed+speed <= self.max_speed_size:
                    self.speed += speed
                else:
                    self.speed = self.max_speed_size
                
                self.fuel -= self.speed * 0.005

        if self.fuel <= 0:
            self.speed = 0
            self.fuel = 0
            print('\033[91mNO Fuel!\033[0m')


    # Decreases the speed of the car by the given value
    def speed_down(self, speed):
        if self.__inputcheck__(speed, 'Speed'):
            self.speed -= speed
            if self.speed < 0:
                self.speed = 0
    

    # Makes the current fuel max
    def refill(self):
        self.fuel = self.fuel_tank
        print('\033[92mFuel full!\033[0m')


    # Print all information about car
    def car_info(self):
        print(f'Model: {self.model}', f'Class: {self.car_class}', 
              f'Max speed: {self.max_speed_size} k/h', f'Current speed: {self.speed} k/h',
              f'Fuel tank: {self.fuel_tank} l', f'Current fuel: {self.fuel} l', 
              f'Door count: {self.door_count}', f'Wheel count: {self.whell_count}', 
              f'Person count: {self.person_count}', 
              f'Tug: {self.tug}-wheeler', '---------------', sep='\n')