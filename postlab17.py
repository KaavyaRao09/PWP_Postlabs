# import sympy as sp
# n, z = sp.symbols('n z')
# x_n = 3**n
# X_z = sp.summation(x_n * z**(-n), (n, 0, sp.oo))
# print("Z-transform of x[n] = 3^n u[n]:")
# sp.pprint(X_z.simplify(), use_unicode=True)


import sympy as sp
n, z, omega = sp.symbols('n z omega')
x_n = sp.cos(omega * n)
X_z = sp.summation(x_n * z**(-n), (n, 0, sp.oo))
print("Z-transform of x[n] = cos(ω n) u[n]:")
sp.pprint(X_z.simplify(), use_unicode=True)

