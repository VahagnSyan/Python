from car import Car

class Pasenger(Car):
    '''
        A class of passenger car where some values are explicit
    '''

    def __init__(self, brand, carModel,
                 speed=0,
                 fuel=100,
                 wheelCount=4,
                 dourCount=4,
                 seatsCount=5,
                 maxSpeed=350,
                 fuelTank=100,
                 tug=2):
        
        """
            Valuation of the main attributes belonging to the passenger car
        """
        
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

