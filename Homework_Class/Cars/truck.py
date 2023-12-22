import car

class Truck(car.Car):
    '''
        A class of trucks where certain values are clear and 
        there is an opportunity to load and unload cargo
    '''


    #Valuation of the main attributes belonging to the truck car
    def __init__(self, brand, carModel,
                 speed=0,
                 fuel=50,
                 wheelCount=6,
                 dourCount=2,
                 seatsCount=3,
                 maxSpeed=120,
                 fuelTank=200,
                 maxLoadWeight = 20,
                 loadWeight = 0,
                 tug = 6,
                 ):
        
        self.maxLoadWeight = maxLoadWeight
        self.loadWeight = loadWeight
        
        super().__init__(brand=brand,
                         carModel=carModel,
                         speed=speed,
                         fuel=fuel,
                         wheelCount=wheelCount,
                         dourCount=dourCount,
                         seatsCount=seatsCount,
                         maxSpeed=maxSpeed,
                         fuelTank=fuelTank,
                         tug=tug)
        
    
    def upload(self, weight):
        #Loading a truck at a given value
        if car._input_check(weight, "Weight"):
            self.loadWeight += weight
            if self.loadWeight > self.maxLoadWeight:
                self.loadWeight = self.maxLoadWeight
                print(f"\033[94mInput weight should not be more than {self.maxLoadWeight} Tons!\033[0m\n")
    

    def unload(self, weight):
        #Unloading a truck at a given value
        if car._input_check(weight, "Weight"):
            self.loadWeight -= weight
            if self.loadWeight < 0:
                self.loadWeight = 0
    

    #Print all information about truck
    def car_info(self):
        super().car_info()
        print(f"\033[90mMax load weight:\033[0m {self.maxLoadWeight} Tons\n",
              sep='\n')


    def car_status(self):
        super().car_status()
        print(f"Load weight: \033[92m{self.loadWeight} Tons\033[0m\n",
              sep='\n')


type1 = Truck("Volvo", "Volvo-FH", fuelTank=100)
type1.car_info()
type1.car_status()
type1.upload(20)
type1.upload("sfgfgsfg")
for i in range(1, 20):
    type1.speed_up(120)
type1.car_status()
type1.refill()
type1.car_status()