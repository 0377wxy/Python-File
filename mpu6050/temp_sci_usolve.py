from sympy import *
# 二元一次方程
x = Symbol('x')
y = Symbol('y')
z = Symbol('z')
k1 = Symbol('k1')
k2 = Symbol('k2')
k3 = Symbol('k3')
print("start...")
solved_value = nsolve(
    [
        (x + 0.013741629464285714*k1)**2 +
        (y - 0.05656328852872671*k2)**2 +
        (z + 0.9020389533190993*k3)**2-0.97936**2,

        (x - 0.9624402685072816*k1)**2 +
        (y - 0.057875549908980584*k2)**2 +
        (z - 0.2956590374696602*k3)**2-0.97936**2,

        (x - 0.008429491370292887*k1)**2 +
        (y + 0.9816741304916318*k2)**2 +
        (z - 0.008675675013075314 * k3)**2-0.97936**2,

        (x + 1.015511607671801*k1)**2 +
        (y - 0.033140643513033176*k2)**2 +
        (z - 0.07795375444312796*k3)**2-0.97936**2,

        (x + 0.01949897378177966*k1)**2 +
        (y - 1.0090141684322034*k2)**2 +
        (z + 0.005959514036016949*k3)**2-0.97936**2,

        (x - 0.043886931046195655*k1)**2 +
        (y + 0.10544752038043478*k2)**2 +
        (z - 1.130653713060462*k3)**2-0.97936**2,
    ],
    [x, y, z, k1, k2, k3],
    [0, 0, 0.1, 1, 1, 1]
)
print(solved_value)