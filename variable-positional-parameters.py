#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""https://docs.python.org/3/glossary.html#term-parameter
"""
def adder(x, y, *args):
    sum = x + y
    
    arglen = len(args)
    for i in range(0, arglen):
        sum = sum + args[i]
    
    return sum

if __name__ == '__main__':
    print(adder(1, 2))
    print(adder(1, 2, 3, 4, 5.5))
