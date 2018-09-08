class ElectricCar():
    def __init__(self, max_range):
        self.max_range = max_range
        self.distance = 0

    def drive(self, distance):
        if distance + self.distance > self.max_range:
            to_travel = self.max_range - self.distance
            self.distance = self.max_range
            return to_travel
        else:
            self.distance += distance
            return to_travel
        #return self.max_range


    def charge(self):
        self.max_range = 100


def test_car_below():
    car = ElectricCar(100)
    assert car.drive(70) == 70

def test_car_below():
    car = ElectricCar(100)
    assert car.drive(130) == 100

def test_car_below():
    car = ElectricCar(100)
    assert car.drive(70) == 70
    assert car.drive(50) == 30
    assert car.drive(50) == 0
    car.charge()
    assert car.drive(50) == 50
