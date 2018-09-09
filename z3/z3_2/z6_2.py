import math
class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        v_ret = Vector(self.x + other.x, self.y + other.y)
        return v_ret

    def __mul__(self, other):
        v_ret = Vector(self.x * other, self.y * other)
        return v_ret

    @property
    def length(self):
        return ((self.x**2 + self.y**2)**(1/2))

    def __sub__(self, other):
        v_ret = Vector(self.x - other.x, self.y - other.y)
        return v_ret

    def __eq__(self, other):
        return self.length == other.length

    def __gt__(self, other):
        return self.length > other.length

    def __ge__(self, other):
        return self.length >= other.length

    def __le__(self, other):
        return self.length <= other.length

    def __lt__(self, other):
        return self.length < other.length

    def __ne__(self, other):
        return self.length != other.length

    def __str__(self):
        return f'Vx{self.x}, Vy{self.y}: {self.length}'




def test_create_vector():
    v1 = Vector(1, 2)
    v2 = Vector(3, 4)
    assert v1.x == 1
    assert v1.y == 2
    assert v2.x == 3
    assert v2.y == 4

def test_vector_add():
    v1 = Vector(1, 2)
    v2 = Vector(3, 4)
    #v3 = (4, 6)
    v3 = v1 + v2
    assert v3.x == 4
    assert v3.y == 6

#def test_vector_add_not_vector():
#    v1 = Vector(1, 2)
#    v2 = Vector(3, 4)
#    v3 = v1 +
#    assert v3.x == 4
#    assert v3.y == 6

def test_vector_minus():
    v1 = Vector(1, 2)
    v2 = Vector(3, 4)
    v3 = v1 - v2
    assert v3.x == -2
    assert v3.y == -2

def test_vector_multi():
    v1 = Vector(1, 2)
    v2 = Vector(3, 4)
    v3 = v1 * 4
    assert v3.x == 4
    assert v3.y == 8

def test_vector_dod_vectorw():
    v1 = Vector(3, 4)
    v2 = Vector(3, 4)
    assert v1.length == 5
    assert v2.length == 5

#def test_vector_dod_vectorw():
#    v1 = Vector(3, 4)
#    v2 = Vector(3, 4)
#    len(v3) = len(v1) + len(v2)
#    assert v3.x == 5
#    assert v3.y == 5

def test_vector_equal():
    v1 = Vector(1, 2)
    v2 = Vector(1, 2)
    assert v1 == v2

def test_vector_equa2():
    v1 = Vector(1, 2)
    v2 = Vector(-1, -2)
    assert v1 == v2

def test_vector_equa3():
    v1 = Vector(3, 4)
    v2 = Vector(0, 5)
    assert v1 == v2

def test_vector_greater():
    v1 = Vector(5, 4)
    v2 = Vector(0, 5)
    assert v1 > v2

def test_vector_greater_equi():
    v1 = Vector(5, 4)
    v2 = Vector(4, 5)
    assert v1 >= v2

def test_vector_less_equi():
    v1 = Vector(5, 4)
    v2 = Vector(4, 5)
    assert v1 <= v2
    v1 = Vector(4, 5)
    v2 = Vector(4, 5)
    assert v1 <= v2
    v1 = Vector(8, 2)
    v2 = Vector(4, 5)
    assert not v1 <= v2

def test_vector_less_than():
    v1 = Vector(1, 4)
    v2 = Vector(4, 5)
    assert v1 < v2
    v1 = Vector(8, 4)
    v2 = Vector(4, 5)
    assert not v1 < v2

def test_vector_less_than():
    v1 = Vector(1, 4)
    v2 = Vector(4, 5)
    assert v1 != v2
    v1 = Vector(1, 4)
    v2 = Vector(1, 4)
    assert not v1 != v2

def test_sorted():
    v1 = Vector(1, 4)
    v2 = Vector(4, 5)
    v3 = Vector(0, 2)
    list = [v1, v2, v3]
    for a in list:
        print(str(a))
    print(list)
    #list = sorted(list)
    assert sorted(list) == [v2, v1, v3]
    print(str(list))