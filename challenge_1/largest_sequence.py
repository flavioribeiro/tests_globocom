#!/usr/sbin/env python
#encoding: utf-8

# Qual inteiro positivo abaixo de 1 milhao produz a sequencia com mais items?

from iterator import GlobalIterator

MAX_NUMBER = 999999

def find_the_largest_sequence():
    global MAX_NUMBER
    largest_seq_size, number = 0, 0

    for x in xrange(1,MAX_NUMBER):
        seq = [n for n in GlobalIterator(x)]
        seq_size = len(seq)
        if seq_size > largest_seq_size:
            largest_seq_size, number = seq_size, x

    print number

if __name__ == "__main__":
    find_the_largest_sequence()

