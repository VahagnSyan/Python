from pasenger import Pasenger

class Suv(Pasenger):
    """
        SUV class, almost all values are clear and
        there is a possibility to change tug
    """


    #Valuation of the main attributes belonging to the Suv car
    def __init__(self, brand, carModel,
                 speed=0,
                 fuel=50,
                 wheelCount=4,
                 dourCount=4,
                 seatsCount=5,
                 maxSpeed=250,
                 fuelTank=90,
                 tug=4):
        
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
    

    #Tug change function
    def change_tug(self):
        if self.tug == 2:
            self.tug=4
            print("\033[94m\n4x4 ON!\033[0m\n")
        else: 
            self.tug=2
            print("\033[94m\n4x4 OFF!\033[0m\n")
    


type1 = Suv("BMW", "X5")
type1.car_info()
type1.car_status()
type1.change_tug()
type1.car_status()
type1.change_tug()