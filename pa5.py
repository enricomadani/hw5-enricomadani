#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May  3 17:30:16 2024

@author: enricoalmadani
"""
import math


def gcd(a, b):
    """Calculate the greatest common divisor of two numbers."""
    if a < b:
        a, b = b, a
    if b == 0:
        return a
    return gcd(b, a % b)


def remove_pairs(path):
    """Remove turnaround pairs from a direction string path."""
    first = path[0]
    if len(path) <= 1:
        return path
    if len(path) == 2:
        if path[0] == 'E' and path[1] == 'W':
            return ''
        if path[0] == 'W' and path[1] == 'E':
            return ''
        if path[0] == 'N' and path[1] == 'S':
            return ''
        if path[0] == 'S' and path[1] == 'N':
            return ''
    if path[0] == 'E' and path[1] == 'W':
        return remove_pairs(path[2:])
    if path[0] == 'W' and path[1] == 'E':
        return remove_pairs(path[2:])
    if path[0] == 'N' and path[1] == 'S':
        return remove_pairs(path[2:])
    if path[0] == 'S' and path[1] == 'N':
        return remove_pairs(path[2:]) 
    return first + remove_pairs(path[1:])


def bisection_root(f, x1, x2):
    """Find the root of a function using the bisection method."""
    bound = 0.0000001
    if f(x1) * f(x2) >= 0:
        raise ValueError("guesses should have different signs")
    mid = (x1 + x2) / 2
    if abs(f(mid)) <= bound:
        return mid
    if f(x1) * f(mid) < 0:
        return bisection_root(f,x1, mid)
    return bisection_root(f,mid, x2)