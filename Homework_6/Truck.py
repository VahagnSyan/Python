from Car import Car


class Truck(Car):
    '''
    A class of trucks where certain values are clear and 
    there is an opportunity to load and unload cargo
    '''


    # Valuation of the main attributes belonging to the truck car
    def __init__(self, model, car_class, max_speed_size=120, fuel=200, speed=0, 
                 door_count=2, wheel_count=6, person_count=3, fuel_tank=200,
                 tug=2, max_load_weight=20000, load_weight=0):
        
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

        self.max_load_weight = max_load_weight
        self.load_weight = load_weight


    # Loading a truck at a given value
    def upload(self, weight):
        if self.__inputcheck__(weight, 'Weight'):
            if self.load_weight + weight > self.max_load_weight:
                print('\033[91mYou cannot load '
                      f'{self.load_weight+weight - self.max_load_weight} 
                      kg\033[0m')
                self.load_weight = self.max_load_weight
            else:
                self.load_weight += weight
        
    
    # Unloading a truck at a given value
    def unload(self, weight):
        if self.__inputcheck__(weight, 'Weight'):
            self.load_weight -= weight
            if self.load_weight < 0:
                self.load_weight = 0


    # Print all information about truck
    def car_info(self):
        super().car_info()
        print(f'Max load weight: {self.max_load_weight} kg', 
              f'Current load weight: {self.load_weight} kg', sep='\n')