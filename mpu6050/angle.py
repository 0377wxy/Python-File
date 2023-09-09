import math

x = 0.008916853265108004
y = -0.024172373571437165
z = 0.9759152672367309


an1 = math.acos(math.sqrt(x**2+z**2)/math.sqrt(x**2+y**2+z**2))
an2 = math.acos(math.sqrt(y**2+z**2)/math.sqrt(x**2+y**2+z**2))
an3 = math.acos(math.sqrt(x**2+y**2)/math.sqrt(x**2+y**2+z**2))
#an4 = math.acos(z/math.sqrt(y**2+z**2))
an4 = math.acos(math.sqrt(2-(x**2+y**2+2*z**2)/(x**2+y**2+z**2)))
print(an1, an2, an3, an4)
