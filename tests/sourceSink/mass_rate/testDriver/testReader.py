import os
import numpy as np

filename = 'massRate.dat'

f = open(filename)
header_string = f.readline()
f.close()

header = header_string.split(" ")
variables = np.loadtxt(filename, skiprows=1, unpack=True)

print(result[0,:])