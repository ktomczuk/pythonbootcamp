from z3.z3_2.z7_2 import Employee
#from z7_2 import Employee

class PremiumEmployee(Employee):
    classmethod

    def __init__(self, name="", lastname="", wage=0, bonus=0):
        super().__init__(name, lastname, wage)
        self.bonus = bonus

    def give_bonus(self, bonus):
        self.bonus += bonus

    def pay_salary(self):
        sel = super(PremiumEmployee, self).pay_salary()
        sel += self.bonus
        self.bonus = 0
        return sel
#metoda klasowa nie sel a cls bo sluzy do rozszerzenia klasy
    @classmethod
    def create_hero(cls, lista):
        lista = lista.split(':')
        return PremiumEmployee(lista(0), lista(1), float(lista(2)), float(lista(3)))


    @staticmethod
    def przywitaj_sie():
        return "Hello"


def test_register_time():
    emp = PremiumEmployee("Jan", "Nowak", 100)
    emp.register_time(5)
    #assert emp.give_bonus == 0
    assert emp.registered_time == 5
    assert emp.lastname == "Nowak"
    assert emp.name == "Jan"
    assert emp.wage == 100
    assert emp.pay_salary() == 500



def test_register_time2():
    emp = PremiumEmployee("Jan", "Nowak", 100)
    emp.register_time(0)
    emp.give_bonus(500)
    emp.give_bonus(1000)
    assert emp.registered_time == 0
    assert emp.wage == 100
    assert emp.pay_salary() == 1500

def test_emp_of_the_month():
    emp = PremiumEmployee.create_hero()
    assert emp.pay_salary() == 0


def import_from_text():
    param = "henryk":"kania":50
    emp = PremiumEmployee.create_hero()
    assert emp.pay_salary() == 0