import cmath
import math

z = 188 + 8333j

print(f"Phase of {z} = {cmath.phase(z):.3f} radians")
print(f"Phase of {z} = {math.degrees(cmath.phase(z)):.3f}°")

mod = (z.real**2 + z.imag**2) ** 0.5
print(f"Modulas of {z} = {mod:.3f}")
print(f"Modulas of {z} = {abs(z):.3f}")
