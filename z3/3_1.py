class Employee:
    def __init__(self, name, lname, wage):
        self.name = "Jan"
        self.lname = "Nowak"
        self.wage = 100

    def regis_time(self, hours):
        self.regis_time += hours

    def pay_salary(self, hours):
        self.regis_time = hours

def licz():
    employee = Employee("Jan", 'Nowak', 100, 0)
    if self.register_time < 8:
        self.salary = self.register_time*100
        self.register_time = 0
        return f'{self.imie}, {self.nazwisko}, zarobił: {self.salary}'
    else:
        self.salary = 800 + (self.register_time-8)*100
        return f'{self.imie}, {self.nazwisko}, zarobił: {self.salary}'


def test_employee():
    employee = Employee("Jan", 'Nowak', 100)
    employee.name == "Jan"
    employee.lname == "Nowak"
    employee.time == 5
    assert employee.wage == 100

def test_employeeNH():
    employee = Employee("Jan", 'Nowak', 100)
    assert employee.name == "Jan"
    assert employee.lname == "Nowak"
    assert employee.wage == 100
    assert employee.pay_salary
