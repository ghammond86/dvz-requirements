import h5py
import numpy as np
import matplotlib.pyplot as plt
plt.rcParams["axes.axisbelow"] = False

filenameActive = "/Users/deto925/Documents/PFlotran/QA/organized/inactive/active.h5"
filenameInactive = "/Users/deto925/Documents/PFlotran/QA/organized/inactive/inactive.h5"

def printname(name):
    print(name)

with h5py.File(filenameActive, "r+") as f:
    # f.visit(printname)
    index_string = 'Time:  1.00000E+02 d/Liquid_Pressure [Pa]'
    presActive = np.array(f[index_string], '=f8')

with h5py.File(filenameInactive, "r+") as f:
    # f.visit(printname)
    index_string = 'Time:  1.00000E+02 d/Liquid_Pressure [Pa]'
    presInactive = np.array(f[index_string], '=f8')

presInactive = np.delete(presInactive, [0,-1], axis=2)
presInactive = np.delete(presInactive, [0,-1], axis=0)

# Compare results
diff = abs(presActive - presInactive)
diffRel = abs(presActive - presInactive)/presActive
# print(presActive)
# print(presInactive)

print(diff.max())
print(diffRel.max())
tol = 1e-6

for dif in diff:
    for di in dif:
        if any (d > tol for d in di):
            print("Failed")
            break
print("Passed")