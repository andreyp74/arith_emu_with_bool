import argparse

def num_as_binary_list(x):
    res = []
    while True:
        res.append(x % 2)
        x = x // 2
        if x == 0:
            break
    return res

def binary_list_as_num(x):
    num = 0
    for i, xi in enumerate(x):
        num += xi * (2 ** i)
    return num

def xor_op(a, b):
    return int(bool(a) != bool(b))

def and_op(a, b):
    return int(bool(a) and bool(b))

def or_op(a, b):
    return int(bool(a) or bool(b))

"""
Sum operation emulated with boolean "bitwise" operations.
 
xi - ith bit of the first argument
yi - ith bit of the second argument
zi - ith bit of the result

Total number of the result's bits: N = max(xbits_numer, ybits_numer) + 1

z0 = x0 XOR y0, rest0 = x0 AND y0
z1 = (x1 XOR y1) XOR rest0, rest1 = (x1 AND y1) OR ((x1 XOR y1) AND rest0)
z2 = (x2 XOR y2) XOR rest1, rest2 = (x2 AND y2) OR ((x2 XOR y2) AND rest1)
z3 = (x3 XOR y3) XOR rest2, rest3 = (x3 AND y3) OR ((x3 XOR y3) AND rest2)
...
zN-1 = (xN-1 XOR yN-1) XOR restN-2, restN-1 = (xN-1 AND yN-1) OR ((xN-1 XOR yN-1) AND restN-2)
The major bit is:
zN = restN-1
"""
def sum(x, y):
    xbits = num_as_binary_list(x)
    ybits = num_as_binary_list(y)
    return binary_list_as_num(sum_impl(xbits, ybits))

def sum_impl(xbits, ybits):
    xbits_numer = len(xbits)
    ybits_numer = len(ybits)
    bit_len = max(xbits_numer, ybits_numer)
    zbits = []
    rest = 0
    for i in range(bit_len):
        xi = xbits[i] if xbits_numer > i else 0
        yi = ybits[i] if ybits_numer > i else 0
        
        t = xor_op(xi, yi)
        zi = xor_op(t, rest)
        rest = or_op(and_op(xi, yi), and_op(t, rest))
        #print("xi=", xi, "yi", yi, "t=", t, "rest=", rest, "zi", zi)
        
        zbits.append(zi)
    
    if rest != 0:    
        zbits.append(rest)

    return zbits

"""
Product operation emulated with boolean "bitwise" operations.

xi - ith bit of the first argument
yi - ith bit of the second argument

N = xbits_numer
M = ybits_numer
i = 0 .. M
j = 0 .. N

pi - i-th intermediate part
pi =
------
i    <------------------------------- j --------------------------------->
p0 = {AND(y0, x0), AND(y0, x1), AND(y0, x2), AND(y0, x3), ..., AND(y0, xN)}
p1 = {0,           AND(y1, x0), AND(y1, x1), AND(y0, x2), ..., AND(y1, xN)}
p2 = {0,           0,           AND(y2, x0), AND(y0, x1), ..., AND(y2, xN)}
...
pM = {0,           0,           0,           AND(yM, x0), AND(yM, x1),... AND(yM, xN)}
      <-------------- M zeros ------------->
result = sum(p0, p1, p2, ..., pM)
"""

def prod(x, y):
    xbits = num_as_binary_list(x)
    ybits = num_as_binary_list(y)
    xbits_numer = len(xbits)
    ybits_numer = len(ybits)
    zbits = []
    for i in range(ybits_numer):
        pi = [0] * i
        for j in range(xbits_numer):
            yi = ybits[i]
            xj = xbits[j]
            tmp = and_op(yi, xj)
            pi.append(tmp)
            
        zbits = sum_impl(zbits, pi)    
        
    return binary_list_as_num(zbits)

"""
Example:
    >python sum_emu.py 2 4 --op sum
    2 + 4 = 6
    >python sum_emu.py 12 43 --op prod
    12 * 43 = 516
"""
def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('arguments', type=int, nargs='+')
    parser.add_argument('--op')
    args = parser.parse_args()
    
    if not args.arguments:
        raise("positive integer arguments are not defined")
    if not args.op:
        raise("operation is not defined")
    
    x = args.arguments[0]
    y = args.arguments[1]
    if args.op == 'sum':
        print("{0} + {1} = {2}".format(x, y, sum(x, y)))
    elif args.op == 'prod':
        print("{0} * {1} = {2}".format(x, y, prod(x, y)))

if __name__ == "__main__":
    main()