class ElectricCar():
    def __init__(self, range):
        self.range = range

    def drive(self, drive):
        zasieg = self.range
        if self.range >= drive:
            self.range = drive
            zasieg = self.range - drive
            return self.range
        elif self.range <= drive:
            a = drive - self.range
            zasieg = 0
            self.range = 0
            return a
        elif self.range == 0:
            return 0

    def charge(self):
        self.range = 100


def test_car():
    car = ElectricCar(100)
    assert car.drive(70) == 70
    assert car.drive(50) == 30
    assert car.drive(50) == 0
    car.charge()
    assert car.drive(50) == 50
