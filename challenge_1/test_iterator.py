#!/usr/sbin/env python
#encoding: utf-8

from iterator import GlobalIterator

def test_example():
    x = [ num for num in GlobalIterator(13) ]
    assert x == [13,40,20,10,5,16,8,4,2,1]

def test_input_1_must_return_1():
    x = [ num for num in GlobalIterator(1) ]
    assert x == [1]

def test_input_2_must_return_2_1():
    x = [ num for num in GlobalIterator(2) ]
    assert x == [2,1]

def test_input_4_must_return_4_2_1():
    x = [ num for num in GlobalIterator(4) ]
    assert x == [4,2,1]

def test_input_11():
    x = [ num for num in GlobalIterator(11) ]
    assert x == [11, 34, 17, 52, 26, 13, 40, 20, 10, 5, 16, 8, 4, 2, 1]
