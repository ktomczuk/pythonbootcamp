class Employee:
    def __init__(self, imie, nazwisko, salary, register_time):
        self.imie = "Jan"
        self.nazwisko = "Nowak"
        self.salary = 100
        self.register_time = 0

    def licz(self):
        #employe = Employee("Jan", 'Nowak', 100, 0)
        if self.register_time < 8:
            self.salary = self.register_time*100
            self.register_time = 0
            return f'{self.imie}, {self.nazwisko}, zarobił: {self.salary}'
        else:
            self.salary = 800 + (self.register_time-8)*100
            return f'{self.imie}, {self.nazwisko}, zarobił: {self.salary}'


def test_produkt():
    employee = Employee("Jan", 'Nowak', 100, 500)
    assert employee.imie == "Jan"
    assert employee.nazwisko == "Nowak"
    assert employee.salary == 100
    assert employee.register_time == 0
    assert employee.licz() == 'Jan, Nowak, zarobił: 500'