"""
A test of a collection of simple math operations
"""
import simple_math 
from simple_math import simple_add
from simple_math import simple_sub
from simple_math import simple_mult
from simple_math import simple_div
from simple_math import poly_first
from simple_math import poly_second
import pytest

def test_simple_add():
    assert simple_add(1,2) == 1+2

def test_simple_sub():
    assert simple_sub(1,2) == 1-2

def test_simple_mult():
    assert simple_mult(1,2) == 1*2

def test_simple_div():
    assert simple_div(1,2) == 1/2

def test_poly_first():
    assert poly_first(1, 2, 3) == 2 + 3*1

def test_poly_second():
    assert poly_second(1, 2, 3, 4) == 2 + 3*1 + 4*(1**2)