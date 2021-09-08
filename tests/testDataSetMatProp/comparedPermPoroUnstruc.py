import h5py
import numpy as np
import matplotlib.pyplot as plt
plt.rcParams["axes.axisbelow"] = False

filenameGridded = "/Users/deto925/Documents/PFlotran/QA/organized/testDataSetMatProp/griddedUnstruct/heterogeneous.h5"
filenameIndexed = "/Users/deto925/Documents/PFlotran/QA/organized/testDataSetMatProp/cellIDUnstruct/heterogeneous.h5"

def printname(name):
    print(name)

with h5py.File(filenameGridded, "r+") as f:
    # f.visit(printname)
    index_string = '   0 Time  0.00000E+00 d/Permeability X [m^2]'
    permGridded = np.array(f[index_string], '=f8')
    index_string = '   0 Time  0.00000E+00 d/Porosity'
    poroGridded = np.array(f[index_string], '=f8')

with h5py.File(filenameIndexed, "r+") as f:
    # f.visit(printname)
    index_string = '   0 Time  0.00000E+00 d/Permeability X [m^2]'
    permInd = np.array(f[index_string], '=f8')
    index_string = '   0 Time  0.00000E+00 d/Porosity'
    poroInd = np.array(f[index_string], '=f8')

# Compare permeabilities
diffPerm = abs(permGridded - permInd)
print(diffPerm.max())
diffPoro = abs(poroGridded - poroInd)
print(diffPoro.max())
tol = 1e-6

if any (d > tol for d in diffPerm):
    print("Failed")
else:
    print("Passed")

if any (d > tol for d in diffPoro):
    print("Failed")
else:
    print("Passed")