import h5py
import numpy as np
import matplotlib.pyplot as plt
plt.rcParams["axes.axisbelow"] = False

# filenameStomp = "/Users/deto925/Documents/PFlotran/QA/feflow10_13_3/stomp/feflow10_13_3.stomp_stomp.h5"
filenamePflotran = "/Users/deto925/Documents/PFlotran/QA/test_regions/coordinate/regions_coord_pflotran.h5"

def printname(name):
    print(name)

with h5py.File(filenamePflotran, "r+") as f:
    # f.visit(printname)
    index_string = 'Time Slice/Time: 0.000e+00 d/Material_ID'
    dataPflotran = np.array(f[index_string], '=f8')
    # x_h5Pflotran = np.array(f['Coordinates/X [m]'])
    # z_h5Pflotran = np.array(f['Coordinates/Z [m]'])


data_manual = np.full((2, 2, 2), 1)
data_manual[0, 0 , 0] = 2

# Compare regions
diff = abs(data_manual - dataPflotran)
print("Maximum difference: {}".format(diff.max()))

