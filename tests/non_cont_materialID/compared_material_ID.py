import h5py
import numpy as np
import matplotlib.pyplot as plt
plt.rcParams["axes.axisbelow"] = False

filenameNonCont = "/Users/deto925/Documents/PFlotran/QA/organized/non_cont_materialID/non-contiguous/feflow10_13_3_non_cont.h5"
filenameCont = "/Users/deto925/Documents/PFlotran/QA/organized/non_cont_materialID/contiguous/feflow10_13_3_cont.h5"

def printname(name):
    print(name)

with h5py.File(filenameCont, "r+") as f:
    # f.visit(printname)
    index_string = 'Time:  5.00000E+00 d/Liquid_Pressure [Pa]'
    presCont = np.array(f[index_string], '=f8')

with h5py.File(filenameNonCont, "r+") as f:
    # f.visit(printname)
    index_string = 'Time:  5.00000E+00 d/Liquid_Pressure [Pa]'
    presNonCont = np.array(f[index_string], '=f8')

# Compare results
diff = abs(presCont - presNonCont)
print(diff.max())
tol = 1e-6

for dif in diff:
    for di in dif:
        if any (d > tol for d in di):
            print("Failed")
            break
print("Passed")