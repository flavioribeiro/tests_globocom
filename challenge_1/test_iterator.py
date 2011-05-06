#!/usr/sbin/env python
#encoding: utf-8

from iterator import GlobalIterator

def test_example():
    x = [ num for num in GlobalIterator(13) ]
    assert x == [13,40,20,10,5,16,8,4,2,1]

def test_input_1():
    x = [ num for num in GlobalIterator(1) ]
    print x
    assert x == [1]
