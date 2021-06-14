import cmath
import math
s=complex(input())
sq=(s.real**2)+(s.imag**2)
print(math.sqrt(sq))
print(cmath.phase(complex(s.real,s.imag)))