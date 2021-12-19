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

"""
Sum operation emulated with boolean bitwise operations.
 
xi - ith 1st argument's bit
yi - ith 2nd argument's bit
zi - ith result's bit

Total number of result bits: N = max(xbits_numer, ybits_numer) + 1

z0 = x0 XOR y0, rest0 = x0 AND y0
z1 = (x1 XOR y1) XOR rest0, rest1 = x1 AND y1
z2 = (x2 XOR y2) XOR rest1, rest2 = x2 AND y2
z3 = (x3 XOR y3) XOR rest2, rest3 = x3 AND y3
...
zN-1 = (xN-1 XOR yN-1) XOR restN-2, restN-1 = xN-1 AND yN-1
The major bit is:
zN = restN-1
"""
def sum(x, y):
    xbits = num_as_binary_list(x)
    ybits = num_as_binary_list(y)
    xbits_numer = len(xbits)
    ybits_numer = len(ybits)
    bit_len = max(xbits_numer, ybits_numer)
    bits_res = []
    rest = 0
    for i in range(bit_len):
        xi = xbits[i] if xbits_numer > i else 0
        yi = ybits[i] if ybits_numer > i else 0
        
        zi = xor_op(xor_op(xi, yi), rest)
        rest = and_op(xi, yi)
        
        bits_res.append(zi)
    
    if rest != 0:    
        bits_res.append(rest)

    return binary_list_as_num(bits_res)

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('arguments', type=int, nargs='+')
    args = parser.parse_args()
    
    if not args.arguments:
        raise("positive integer arguments are not defined")
    
    print("{0} + {1} = {2}".format(
        args.arguments[0], args.arguments[1], sum(args.arguments[0], args.arguments[1])))

if __name__ == "__main__":
    main()