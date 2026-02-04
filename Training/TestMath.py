import math

# Constants
PI = math.pi
E = math.e

# Input
a = 77
b = 6.9
x = 22
y = 88
angle = 90

# Functions:
# GCD/LCM
print(f"GCD of {x} & {y} = {math.gcd(x, y)}")
print(f"LCM of {x} & {y} = {math.lcm(x, y)}")

# Trigonometry
radAngle = math.radians(angle)  # ←All Trig functions need Radions instead of Degrees

print(f"Sin {angle}° = {math.sin(radAngle)}")
print(f"Cos {angle}° = {math.cos(radAngle):.5}")
print(f"Tan {angle}° = {math.tan(radAngle):.5}")

# Distance
print(f"Is 0.1 + 0.3 close to 0.3? A:{math.isclose(0.1 + 0.2, 0.3)}")

# Rounding
print(f"Rounding {b} to the Ceiling: {math.ceil(b)}")
print(f"Rounding {b} to the Floor: {math.floor(b)}")
print(f"Rounding {b} using Truncate: {math.trunc(b)}")

# Factorial
print(f"Factorial of 5: {math.factorial(5)}")

# Absolute value
print(f"The Absolute value of -420: {math.fabs(-420)}")

# Powers
print(f"Square root of 25: {math.sqrt(25)}")
print(f"2 to the 3rd power: {math.pow(2, 3)}")
print(f"8 to the 1/3rd power: {math.pow(8, 1/3)}")

# Logs
print(f"Natural Log of 100: {math.log(100)}")
print(f"Log Base 10 of 100: {math.log10(100)}")
print(f"Log Base 2 of 100: {math.log2(100)}")