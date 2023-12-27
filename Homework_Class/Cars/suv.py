from pasenger import Pasenger

class Suv(Pasenger):
    """
        SUV class, almost all values are clear and
        there is a possibility to change tug
    """

    def __init__(self, brand, car_model,
                 speed=0,
                 fuel=50,
                 wheel_count=4,
                 dour_count=4,
                 seats_count=5,
                 max_speed=250,
                 fuel_tank=90,
                 tug=4):
        """
            # Valuation of the main attributes belonging to the Suv car
        """
        
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
    

    def change_tug(self):
        '''
            Tug change function
        '''
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