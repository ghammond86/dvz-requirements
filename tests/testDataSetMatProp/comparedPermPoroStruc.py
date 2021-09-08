import h5py
import numpy as np
import matplotlib.pyplot as plt
plt.rcParams["axes.axisbelow"] = False

filenameGridded = "/Users/deto925/Documents/PFlotran/QA/organized/testDataSetMatProp/griddedStruct/pflotran/heterogeneous.h5"
filenameIndexed = "/Users/deto925/Documents/PFlotran/QA/organized/testDataSetMatProp/cellIDStruct/pflotran/heterogeneous.h5"

def printname(name):
    print(name)

with h5py.File(filenameGridded, "r+") as f:
    # f.visit(printname)
    index_string = 'Time:  0.00000E+00 d/Permeability_X [m^2]'
    permGridded = np.array(f[index_string], '=f8')
    index_string = 'Time:  0.00000E+00 d/Porosity'
    poroGridded = np.array(f[index_string], '=f8')

with h5py.File(filenameIndexed, "r+") as f:
    # f.visit(printname)
    index_string = 'Time:  0.00000E+00 d/Permeability_X [m^2]'
    permInd = np.array(f[index_string], '=f8')
    index_string = 'Time:  0.00000E+00 d/Porosity'
    poroInd = np.array(f[index_string], '=f8')

# Compare permeabilities
diffPerm = abs(permGridded - permInd)
print(diffPerm.max())
diffPoro = abs(poroGridded - poroInd)
print(diffPoro.max())
tol = 1e-6

for dif in diffPerm:
    for di in dif:
        if any (d > tol for d in di):
            print("Failed")
            break
print("Passed")

for dif in diffPoro:
    for di in dif:
        if any (d > tol for d in di):
            print("Failed")
            break
print("Passed")