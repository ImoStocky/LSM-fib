#test_fib.py

import pytest
import fib as m
import sys

def test_fib0():
    assert m.fib(0)==0;

def test_fib1():
    assert m.fib(1)==1;

def test_fib10():
    assert m.fib(10)==55;

#@pytest.mark.xfail(raises=ValueError)
def test_fib_raise_val_err():
    with pytest.raises(ValueError):
        m.fib(-1)

def test_file_out():
    mx=3
    stri = "0 1 1 2"

    with open('out.txt','r') as f:
        assert stri == f.readline().rstrip(' ')

def test_fib_is_number():
    if not isinstance(m.fib(0),int):
        raise TypeError('Please check that output of function is number')

