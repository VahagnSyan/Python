class Car:
    '''
        The base class from which all other type car should inherit
    '''


    # Creation of basic attributes belonging to the car
    def __init__(self, brand, carModel, wheelCount, dourCount, seatsCount,
                       maxSpeed, speed, fuel, fuelTank, tug):
        
        self.brand = brand
        self.carModel = carModel
        self.wheelCount = wheelCount
        self.dourCount = dourCount
        self.seatsCount = seatsCount
        self.maxSpeed = maxSpeed
        self.speed = speed
        self.fuelTank = fuelTank
        self.fuel = fuel
        self.tug = tug
    

    def speed_up(self, speed):
        #Increases the speed of the car by the given value
        if 0 < self.fuel <= self.fuelTank:
            if _input_check(speed, "Spead"):
                if self.speed + speed < self.maxSpeed:
                    self.speed += speed
                else:
                    self.speed = self.maxSpeed
                self.fuel -= self.speed * 0.005
            if self.fuel <= 0:
                self.fuel = 0
                self.speed = 0
                print('\033[91mNO Fuel!\033[0m')
    

    def speed_down(self, speed):
        #Decreases the speed of the car by the given value
        if _input_check(speed, "Speed"):
            self.speed -= speed
        if self.speed < 0:
            self.speed = 0


    def refill(self):
        #Makes the current fuel max
        self.fuel = self.fuelTank
        print('\033[94mRefill:\033[0m \033[92mFuel full!\033[0m\n')
    

    def car_info(self):
        #Print all information about car
        print("\033[90m------- Car Info ------\033[0m")
        print(f"\033[90mCar brand:      \033[0m {self.brand}",
              f"\033[90mCar model:      \033[0m {self.carModel}",
              f"\033[90mMax speed:      \033[0m {int(self.maxSpeed)} k/h",
              f"\033[90mPersons count:  \033[0m {int(self.seatsCount)}",
              f"\033[90mFuel tank:      \033[0m {round(self.fuelTank, 2)} L",
              f"\033[90mWheel count:    \033[0m {int(self.wheelCount)}",
              f"\033[90mDour count:     \033[0m {int(self.dourCount)}",
              f"\033[90mTug status:     \033[0m {int(self.tug)}",
              sep='\n')


    def car_status(self):
        #Print all information about car
        print("\033[90m---- Car Status ----\033[0m")
        print(f"Fuel:        \033[92m{round(self.fuel, 2)} L\033[0m",
              f"Speed:       \033[92m{int(self.speed)} k/h\033[0m",
              sep='\n')


def _input_check(number, text):
    #A helper function that checks whether the input data is correct or not
    types = [int, float]
    if type(number) in types and 0 < number:
        return True
    elif type(number) not in types:
        print(f"\033[91mThis value is not a valid number! ({number})\033[0m\n")
        return False
    elif number < 0:
        print(f'\033[91m{text} mast be positive!\033[0m')
        return False