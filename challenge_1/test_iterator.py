#!/usr/sbin/env python
#encoding: utf-8

from iterator import GlobalIterator

def test_example():
    x = [ num for num in GlobalIterator() ]
    assert x == [13,40,20,10,5,16,8,4,2,1]
