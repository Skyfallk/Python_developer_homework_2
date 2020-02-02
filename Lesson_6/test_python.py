import math

test_list = [1,2,3,4,5,6,7,8,9,10,11,12]

def test_filter_0():
    assert list(filter(lambda x: x == 1, test_list))[0] == 1

def test_filter_1():
    for i in list(filter(lambda x: x % 2 == 0, test_list)):
        assert i % 2 == 0

def test_map_0():
    for i,j in enumerate(list(map(lambda x: x - 1, test_list))):
        assert test_list[i] - j == 1

def test_map_1():
    assert sum(list(map(lambda x: x % 5 == 0, test_list))) == 2

def test_sorted():
    res = sorted(test_list)
    for i in range(len(res)-1):
        assert res[i] <= res[i+1]

def test_pi():
    assert math.pi - 3.14 > 0

def test_sqrt_0():
    assert math.sqrt(4) == 2

def test_sqrt_1():
    assert math.sqrt(12.31**2) == 12.31

def test_pow_0():
    assert math.pow(3,4) == 3**4

def test_hypot_0():
    assert math.hypot(1,1) == math.sqrt(2)

