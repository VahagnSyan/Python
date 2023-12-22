from Passenger import Passenger


class Suv(Passenger):
    '''
    SUV class, almost all values are clear and there is a possibility 
    to change tug
    '''


    # Valuation of the main attributes belonging to the Suv car
    def __init__(self, model, car_class, max_speed_size=250, fuel=150, 
                 speed=0, door_count=4, wheel_count=4, person_count=5, 
                 fuel_tank=150, tug=4):
        
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
        
    
    # Tug change function
    def change_tug(self):
        if self.tug == 4:
            self.tug = 2
            print('\033[91mThe car became a 2-wheeler\033[0m')
        else:
            self.tug = 4
            print('\033[91mThe car became a 4-wheeler\033[0m')


car1 = Suv('Porsche', 'Cayenne')
car1.car_info()
car1.speed_up(150)
car1.speed_up(220)
car1.change_tug()
car1.speed_down(50)
car1.car_info()