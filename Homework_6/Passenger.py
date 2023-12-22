from Car import Car


class Passenger(Car):
    '''
    A class of passenger car where some values are explicit
    '''


    # Valuation of the main attributes belonging to the passenger car
    def __init__(self, model, car_class, max_speed_size=300, fuel=100, speed=0, 
                 door_count=4, wheel_count=4, person_count=5, fuel_tank=100, 
                 tug=2):
        
        super().__init__(model=model, 
                         car_class=car_class, 
                         max_speed_size=max_speed_size, 
                         fuel=fuel, 
                         speed=speed, 
                         door_count=door_count, 
                         wheel_count=wheel_count, 
                         person_count=person_count, 
                         fuel_tank=fuel_tank,
                         tug=tug)