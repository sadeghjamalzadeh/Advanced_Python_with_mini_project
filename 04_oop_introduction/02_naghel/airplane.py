from flying_vehicle import FlyingVehicle
from ground_vehicle import GroundVehicle


class Airplane(GroundVehicle, FlyingVehicle):

    def __init__(self, airline, number_of_crew, captain, **kwargs):
        super().__init__(**kwargs)
        self.airline = airline
        self.number_of_crew = number_of_crew
        self.captain = captain


class B707(Airplane):
    def __init__(self, **kwargs):
        print(kwargs)
        super().__init__(**kwargs)


x = B707(name="SAliB", price=850000, number_of_seats=850, max_speed=500, number_of_wheels=18,
                 steering_wheel="Manual", fuel="Oil", number_of_fins=2, airline="Quera Air", number_of_crew=65,
                 captain="Bagher")
