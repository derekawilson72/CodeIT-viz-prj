


def country(*abc):  ##abc=[slice(2,None)]
    if len(abc)==1:
        item=abc[0]
        def f(obj):
            return obj[item]

    else:
        def f(obj):
            return tuple(obj[item] for item in abc)

    return f


selection = []
selection = country(slice(2,None))('AUSTRALIA')
print selection



##slicing object
s1 = slice(2,None)
L1 = range(20)     ##make 20 elements from 0 to 19
L1[0:10:1]         ##slicing start, stop, step
L1[slice(0,10,1)]  ##slicing function does the same thing
s1 = slice(2,None) ##start=2, stop=None, step defaults to 1
'AUSTRALIA'[s1]    ## = 'STRALIA'

item=s1
def f(obj):
    return obj[item]

f('AUSTRALIA')


