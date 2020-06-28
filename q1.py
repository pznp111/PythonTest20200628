from scipy.integrate import dblquad
import numpy as np

def f(x, y):
   return np.exp(-x-y)

area = dblquad(lambda x, y: np.exp(-x-y), 0, np.inf, lambda x: x, lambda x: np.inf)
print(area[0])


