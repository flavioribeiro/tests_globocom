#!/usr/sbin/env python
#encoding: utf-8

def find_seq_size(n):
    cont = 1
    while n > 1:
        n = n/2 if n % 2 == 0 else 3*n+1
        cont+=1
    return cont

max_seq_size = 0
n_max_seq_size = 0

for num in xrange(1, 999999):
    seq_size = find_seq_size(num)
    if seq_size > max_seq_size:
        max_seq_size = seq_size
        n_max_seq_size = num

print n_max_seq_size
