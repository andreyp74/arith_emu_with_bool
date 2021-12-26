# Sum operation emulated with boolean "bitwise" operations
``` 
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
```