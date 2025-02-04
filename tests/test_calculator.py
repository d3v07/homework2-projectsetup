'''My calculator'''
from calculator import add, subtract, multiply, divide

def test_addition():
    '''asserting'''
    assert add(2,2) == 4

def test_subtraction():
    '''asserting'''
    assert subtract(2,2) == 0

def test_multiply():
    '''asserting'''
    assert multiply(2,2) == 4

def test_divide():
    '''asserting'''
    assert divide(2,2) == 1
