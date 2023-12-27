"""
    class car
"""

def _positive_number(number, text):
    """
        A helper function that checks whether the input data is correct or not
    """

    types = [int, float]
    if type(number) in types and 0 < number:
        return True
    if type(number) not in types:
        print(f"\033[91mThis value is not a valid number! ({number})\033[0m\n")
        return False
    if number < 0:
        print(f'\033[91m{text} mast be positive!\033[0m')
        return False


class Car:
    '''
        The base class from which all other type car should inherit
    '''

    def __init__(self,
                 brand,
                 car_model,
                 wheel_count,
                 dour_count,
                 seats_count,
                 max_speed,
                 speed,
                 fuel,
                 fuel_tank,
                 tug):
        """
            Creation of basic attributes belonging to the car
        """
        self.brand = brand
        self.car_model = car_model
        self.wheel_count = wheel_count
        self.dour_count = dour_count
        self.seats_count = seats_count
        self.max_speed = max_speed
        self.speed = speed
        self.fuel_tank = fuel_tank
        self.fuel = fuel
        self.tug = tug
    def speed_up(self, speed):
        """
            Increases the speed of the car by the given value
        """

        if 0 < self.fuel <= self.fuel_tank:
            if _positive_number(speed, "Spead"):
                if self.speed + speed < self.max_speed:
                    self.speed += speed
                else:
                    self.speed = self.max_speed
                self.fuel -= self.speed * 0.005
            if self.fuel <= 0:
                self.fuel = 0
                self.speed = 0
                print('\033[91mNO Fuel!\033[0m')
    def speed_down(self, speed):
        """
            Decreases the speed of the car by the given value
        """

        if _positive_number(speed, "Speed"):
            self.speed -= speed
        if self.speed < 0:
            self.speed = 0


    def refill(self):
        """
            Makes the current fuel max
        """

        self.fuel = self.fuel_tank
        print('\033[94mRefill:\033[0m \033[92mFuel full!\033[0m\n')
    def car_info(self):
        """
            Print all information about car
        """

        print("\033[90m------- Car Info ------\033[0m")
        print(f"\033[90mCar brand:      \033[0m {self.brand}",
              f"\033[90mCar model:      \033[0m {self.car_model}",
              f"\033[90mMax speed:      \033[0m {int(self.max_speed)} k/h",
              f"\033[90mPersons count:  \033[0m {int(self.seats_count)}",
              f"\033[90mFuel tank:      \033[0m {round(self.fuel_tank, 2)} L",
              f"\033[90mWheel count:    \033[0m {int(self.wheel_count)}",
              f"\033[90mDour count:     \033[0m {int(self.dour_count)}",
              f"\033[90mTug status:     \033[0m {int(self.tug)}",
              sep='\n')
    def car_status(self):
        """
            Print all information about car
        """

        print("\033[90m---- Car Status ----\033[0m")
        print(f"Fuel:        \033[92m{round(self.fuel, 2)} L\033[0m",
              f"Speed:       \033[92m{int(self.speed)} k/h\033[0m",
              sep='\n')
