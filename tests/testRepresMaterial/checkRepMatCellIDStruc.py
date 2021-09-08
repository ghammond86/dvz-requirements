import h5py
import numpy as np
import matplotlib.pyplot as plt
plt.rcParams["axes.axisbelow"] = False

filenamePflotran = "/Users/deto925/Documents/PFlotran/QA/organized/testRepresMaterial/testRepMatCellIDStruc/regions_cellIDs_pflotran.h5"

def printname(name):
    print(name)

with h5py.File(filenamePflotran, "r+") as f:
    # f.visit(printname)
    index_string = 'Time Slice/Time: 0.000e+00 d/Material_ID'
    dataPflotran = np.array(f[index_string], '=f8')

nx = 2
data_manual = np.full((nx, nx, nx), 1)
for i in range(nx):
    for j in range(nx):
        data_manual[i, j , 0] = 2

# Compare regions
diff = abs(data_manual - dataPflotran)
print("Maximum difference: {}".format(diff.max()))
tol = 1e-6

for dif in diff:
    for di in dif:
        if any (d > tol for d in di):
            print("Failed")
            break
print("Passed")