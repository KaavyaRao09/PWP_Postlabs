#1. 
# # Define symbols
# n, z, a = sp.symbols('n z 3')
# # Define the signal x[n] = a^n * u[n]
# x_n = 2**n
# # Compute the Z-transform
# X_z = sp.summation(x_n * z**(-n), (n, 0, sp.oo))
# # Print the result
# print("Z-transform of x[n] = 3^n u[n]:")
# sp.pprint(X_z, use_unicode=True)

#2.
# n, z, omega = sp.symbols('n z omega')
# # Define the sinusoidal sequence x[n] = sin(omega * n) * u[n]
# x_n = sp.cos(omega * n)
# # Compute the Z-transform
# X_z = sp.summation(x_n * z**(-n), (n, 0, sp.oo))
# # Print the result
# print("Z-transform of x[n] = cos(omega * n) u[n]:")
# sp.pprint(X_z, use_unicode=True)

