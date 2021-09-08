import h5py
import numpy as np
import matplotlib.pyplot as plt
plt.rcParams["axes.axisbelow"] = False

#Choose file to verify
filenamePflotran = "/Users/deto925/Documents/PFlotran/QA/organized/testRepresIC/testRepICCellIDUnstruc/regions_cellIDs.h5"
# filenamePflotran = "/Users/deto925/Documents/PFlotran/QA/organized/testRepresIC/testRepICRegUnstruc/regions_cellIDs.h5"

def printname(name):
    print(name)

with h5py.File(filenamePflotran, "r+") as f:
    # f.visit(printname)
    index_string = '   0 Time  0.00000E+00 d/Material ID'
    dataPflotran = np.array(f[index_string], '=f8')

nx = 2
data_manual = np.full((nx*nx*nx,), 1)
for i in range(nx*nx):
    data_manual[i] = 2

# Compare regions
diff = abs(data_manual - dataPflotran)
print("Maximum difference: {}".format(diff.max()))
tol = 1e-6


if any (d > tol for d in diff):
    print("Failed")
else:
    print("Passed")