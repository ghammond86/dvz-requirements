import h5py
import numpy as np
import matplotlib.pyplot as plt

# filenamePflotran = "/Users/deto925/Documents/PFlotran/QA/organized/struct_irregular/struct_irregular.h5"
# filenameManual = "/Users/deto925/Documents/PFlotran/QA/organized/struct_irregular/manual_coords_struct_irregular.dat"

filenamePflotran = "/Users/deto925/Documents/PFlotran/QA/organized/struct_irregular/struct_irregular_origin.h5"
filenameManual = "/Users/deto925/Documents/PFlotran/QA/organized/struct_irregular/manual_coords_struct_irregular_origin.dat"

def printname(name):
    print(name)

with h5py.File(filenamePflotran, "r+") as f:
    # f.visit(printname)
    index_string = 'Coordinates/X [m]'
    XPflotran = np.array(f[index_string], '=f8')
    XPflotran = np.reshape(XPflotran, (-1,1))
    index_string = 'Coordinates/Y [m]'
    YPflotran = np.array(f[index_string], '=f8')
    YPflotran = np.reshape(YPflotran, (-1,1))
    index_string = 'Coordinates/Z [m]'
    ZPflotran = np.array(f[index_string], '=f8')
    ZPflotran = np.reshape(ZPflotran, (-1,1))

coordPflotran = np.concatenate((XPflotran,YPflotran, ZPflotran), axis = 1)

coordManual = np.loadtxt(filenameManual, skiprows=1, delimiter = " ")
# Compare results
diff = abs(coordPflotran - coordManual)

print(diff.max())
tol = 1e-6

for dif in diff:
    if any (d > tol for d in dif):
        print("Failed")
        break
print("Passed")