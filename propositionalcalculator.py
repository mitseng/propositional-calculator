# -*- coding: utf-8 -*-
"""
Created on Mon Apr 23 22:35:58 2018

@author: LinlongZeng, XuebingMei
"""

instruction = """
Logical connective standard:
    '&' for conjunction,
    '|' for disjunction,
    '-' for negation,
    '->' for condition,
    '=' for bicondition.
Logical constants are T, and F.
Logical variables could be any upper case except T and F.\
"""


def find_variables(p):  # return all variables in the string.
    temp = [v for v in p if ('A' <= v <= 'Z') and v != 'T' and v != 'F']
    variables = []
    for v in temp:
        if v not in variables:
            variables.append(v)
    variables.sort()
    return tuple(variables)


def formatten(p):  # to make p evaluatable in boolean operation
    p = p.replace('T', ' True ')
    p = p.replace('F', ' False ')
    p = p.replace('&', ' and ')
    p = p.replace('|', ' or ')
    p = p.replace('=', '==')
    p = p.replace('->', '<=')
    p = p.replace('-', ' not ')
    return p


def value(n):  # return the cases of variables for the caculation
    l = [bin(i) for i in range(2 ** n)]
    l = [x[2:] for x in l]
    l = ['0' * (n - len(x)) + x for x in l]
    l = [tuple([bool(eval(y)) for y in x]) for x in l]
    return tuple(l)


def calculate(p, variables, n, varvalue):  # return the truth table
    t = {v: None for v in variables}
    s = {i: None for i in range(2 ** n)}
    for i in range(2 ** n):
        for j in range(n):
            t[variables[j]] = varvalue[i][j]
        q = p
        for x in q:
            if x in variables:
                q = q.replace(x, str(t[x]))
        s[i] = eval(q)
    return s


def show(s):  # to printout
    mi = '∑()'
    ma = 'Π()'
    for key in s:
        if s[key]:
            mi = mi[: -1] + str(key) + ', )'
        else:
            ma = ma[: -1] + str(key) + ', )'
    mi = mi[: -3] + ')'
    ma = ma[: -3] + ')'
    print('result as below: ')
    print(mi)
    print(ma)


def main():
    print(instruction)
    p = input('enter your compound proposition:\n')

    variables = find_variables(p)
    p = formatten(p)
    n = len(variables)
    varvalue = value(n)
    s = calculate(p, variables, n, varvalue)
    show(s)


main()
input('Press <Enter>')
