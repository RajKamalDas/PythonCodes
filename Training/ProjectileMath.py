import math

# Details
G = 9.8
iniVel = 100
theta = 45

# Convert to Radian
thetaRad = math.radians(theta)

# Calculations
durationOfFlight = (2 * iniVel * math.sin(thetaRad)) / G
maxHeight = (iniVel**2 * math.sin(thetaRad**2)) / (G * 2)
distance = (iniVel**2 * math.sin(thetaRad * 2)) / G

# Output
print(
    f"""-----Projectile Travel Details-----
Time of Flight: {durationOfFlight}
Maximum Height Reached: {maxHeight}
Horizontal Distance Traveled: {distance}"""
)
