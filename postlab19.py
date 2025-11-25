# # Z-transform of unit step u[n]
# def z_transform_unit_step(z):
#     return 1 / (1 - z**(-1))
# # Stability check
# def check_stability(den_roots):
#     return "Stable" if np.all(np.abs(den_roots) < 1) else "Unstable"
# z = 2
# print("Z-transform of unit step at z=2:", z_transform_unit_step(z))



import numpy as np
num = [0.5, -0.5*(0.7+0.9), 0.5*(0.7*0.9)]
den = [1, -(0.6+0.4), 0.6*0.4]
def check_stability(den_roots):
    return "Stable" if np.all(np.abs(den_roots) < 1) else "Unstable"
zeros = np.roots(num)
poles = np.roots(den)
print("Zeros:", zeros)
print("Poles:", poles)
print("System Stability:", check_stability(poles))
