"""
    class truc inherit from car
"""

import car

class Truck(car.Car):
    '''
        A class of trucks where certain values are clear and 
        there is an opportunity to load and unload cargo
    '''

    def __init__(self,
                 brand,
                 car_model,
                 speed=0,
                 fuel=50,
                 wheel_count=6,
                 dour_count=2,
                 seats_count=3,
                 max_speed=120,
                 fuel_tank=200,
                 max_load_weight = 20,
                 load_weight = 0,
                 tug = 6):
        """
            Valuation of the main attributes belonging to the truck car
        """
        self.max_load_weight = max_load_weight
        self.load_weight = load_weight
        super().__init__(brand=brand,
                         car_model=car_model,
                         speed=speed,
                         fuel=fuel,
                         wheel_count=wheel_count,
                         dour_count=dour_count,
                         seats_count=seats_count,
                         max_speed=max_speed,
                         fuel_tank=fuel_tank,
                         tug=tug)
    def upload(self, weight):
        """
            Loading a truck at a given value
        """

        if car._positive_number(weight, "Weight"):
            self.load_weight += weight
            if self.load_weight > self.max_load_weight:
                self.load_weight = self.max_load_weight
                print("\033[94mInput weight should not be more than",
                      f"{self.max_load_weight} Tons!\033[0m\n", sep='')
    def unload(self, weight):
        """
            Unloading a truck at a given value
        """

        if car._positive_number(weight, "Weight"):
            self.load_weight = max(self.load_weight, 0)
    def car_info(self):
        """
            Print all information about truck
        """

        super().car_info()
        print(f"\033[90mMax load weight:\033[0m {self.max_load_weight} Tons\n",
              sep='\n')


    def car_status(self):
        super().car_status()
        print(f"Load weight: \033[92m{self.load_weight} Tons\033[0m\n",
              sep='\n')


type1 = Truck("Volvo", "Volvo-FH", fuel_tank=100)
type1.car_info()
type1.car_status()
type1.upload(20)
type1.upload("sfgfgsfg")
for i in range(1, 20):
    type1.speed_up(120)
type1.car_status()
type1.refill()
type1.car_status()
