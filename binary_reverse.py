#!/usr/bin/env python2
# -*- coding: utf-8 -*-
from __future__ import print_function
import fileinput


def binary_reverse(number):
    binary_str = bin(number)[2:]
    reversed_binary_str = ''.join(reversed(binary_str))
    return int(reversed_binary_str, 2)

def as_number(input):
    return int(input.strip())

if __name__ == '__main__':
    for line in fileinput.input():
        print(binary_reverse(as_number(line)))
