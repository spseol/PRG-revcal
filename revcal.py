#!/usr/bin/env python3
# Soubor:  postfix.py
# Datum:   15.02.2018 13:11
# Autor:   Marek Nožka, nozka <@t> spseol <d.t> cz
# Licence: GNU/GPL
# Úloha:   Postfixová kalkulačka
############################################################################
from math import pi
import math
import re


def plus(a, b):
    return a + b


def minus(a, b):
    return a - b


def root(a):
    return a ** (1/2)


def rad2rad(r):
    return r


def deg2rad(d):
    return d * pi / 180


x2rad = deg2rad


def sin(x):
    return math.sin(x2rad(x))


def cos(x):
    return math.cos(x2rad(x))


def tan(x):
    return math.tan(x2rad(x))


FUNCTIONS = {
    '+': (2, plus),
    '-': (2, minus),
    '*': (2, lambda a, b: a * b),
    '/': (2, lambda a, b: a / b),
    '**': (2, lambda a, b: a ** b),
    'root': (1, root),
    'sin': (1, sin),
    'cos': (1, cos),
    'tg': (1, tan),
    'rad': (1, math.radians),
    'deg': (1, math.degrees),
}

stack = []
while True:
    radek = input(str(stack) + ' > ')
    radek = radek.split()
    for token in radek:
        if token == 'kill' or token == 'quit' or token == 'q':
            exit(0)
        elif token == 'switch':
            if len(stack) >= 2:
                a = stack.pop()
                b = stack.pop()
                stack.append(a)
                stack.append(b)
            else:
                print('ERROR "{}": v zásobníku není dost čísel'.format(token))
        elif token == 'R':   # přepnu na počítání v radiánech
            x2rad = rad2rad
        elif token == 'D':   # přepnu na počítáné ve stupních
            x2rad = deg2rad
        elif token == 'pi':   # přidám pi
            stack.append(pi)
        elif token in FUNCTIONS:
            if len(stack) >= FUNCTIONS[token][0]:
                a = stack.pop()
                b = stack.pop()
                stack.append(FUNCTIONS[token][1](a, b))
            else:
                print('ERROR "{}": v zásobníku není dost čísel'.format(token))
        elif re.search(r'[0-9][+-][0-9]j', token):
                stack.append(complex(token))
        elif re.search(r'[0-9][I][0-9]', token):
                ah, uhel = token.split('I')
                ah = float(ah)
                uhel = float(uhel)
                stack.append(complex(ah*cos(uhel), ah*sin(uhel)))
        else:
            try:
                stack.append(float(token))
            except:
                print('ERROR "{}" není ani funkce ani číslo'.format(token))
