# Some arithmetic operations emulated with bitwise logic gates
Usage example:
```
>python sum_emu.py 2 4 --op sum
2 + 4 = 6
>python sum_emu.py 12 43 --op prod
12 * 43 = 516
```
## Sum operation
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
## Prod operation
```
xi - ith bit of the first argument
yi - ith bit of the second argument

N = xbits_numer
M = ybits_numer
i = 0 .. M
j = 0 .. N

pi - i-th intermediate part
pi =
i    <------------------------------- j --------------------------------->
p0 = {AND(y0, x0), AND(y0, x1), AND(y0, x2), AND(y0, x3), ..., AND(y0, xN)}
p1 = {0,           AND(y1, x0), AND(y1, x1), AND(y0, x2), ..., AND(y1, xN)}
p2 = {0,           0,           AND(y2, x0), AND(y0, x1), ..., AND(y2, xN)}
...
pM = {0,           0,           0,           AND(yM, x0), AND(yM, x1),... AND(yM, xN)}
      <-------------- M zeros ------------->
result = sum(p0, p1, p2, ..., pM)
```

