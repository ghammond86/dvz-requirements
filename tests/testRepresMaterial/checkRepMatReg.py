import h5py
import numpy as np
import matplotlib.pyplot as plt
plt.rcParams["axes.axisbelow"] = False

# Choose file to test
filenamePflotran = "/Users/deto925/Documents/PFlotran/QA/testRepresMaterial/testRepMatIJKStruc/regions_IJK.h5"
# filenamePflotran = "/Users/deto925/Documents/PFlotran/QA/testRepresMaterial/testRepMatRegStruc/regions_coords.h5"

def printname(name):
    print(name)

with h5py.File(filenamePflotran, "r+") as f:
    # f.visit(printname)
    index_string = 'Time:  0.00000E+00 d/Material_ID'
    dataPflotran = np.array(f[index_string], '=f8')

data_manual = np.zeros((80,65))

Lx = 8.
Lz = 6.5

Nx = 80
dx = Lx/Nx
Nz = 65
dz = Lz/Nz

x, y = np.mgrid[slice(0, Lx+dx, dx),
                slice(0, Lz+dz, dz)]

coord_x = np.linspace(dx/2., Lx-dx/2, Nx)
coord_z = np.linspace(dz/2., Lz-dz/2, Nz)

for i in range(Nx):
    for j in range(Nz):
        if coord_z[j] < 4:
            data_manual[i, j] = 3
        elif coord_z[j] < 5:
            if coord_x[i] < 1 or coord_x[i] > 3:
                data_manual[i, j] = 3
            else:
                data_manual[i, j] = 4
        elif coord_z[j] < 5.6:
            data_manual[i, j] = 3
        elif coord_z[j] < 6.1:
            data_manual[i, j] = 2
        elif coord_z[j] < 6.5:
            data_manual[i, j] = 1

dataPflotran = dataPflotran.reshape((80,65))
# Compare regions
diff = abs(data_manual - dataPflotran)
print(diff.max())
if diff.any() < 1e-3:
    print("Passed")
else:
    print("Failed")
    
fig, ax = plt.subplots(1, 1)
ax.grid(True, alpha = 1.0, linestyle='-', color='grey')
ax.plot([0, 8], [4, 4], color='grey', linestyle='-', linewidth=2)
ax.plot([0, 8], [5, 5], color='grey', linestyle='-', linewidth=2)
ax.plot([1, 1], [0, 6.5], color='grey', linestyle='-', linewidth=2)
ax.plot([3, 3], [0, 6.5], color='grey', linestyle='-', linewidth=2)
ax.plot([0, 8], [6.1, 6.1], color='grey', linestyle='-', linewidth=2)
ax.plot([0, 8], [5.6, 5.6], color='grey', linestyle='-', linewidth=2)
plt.pcolormesh(x, y, diff)
plt.colorbar()
plt.show()

# fig2, ax2 = plt.subplots(1, 1)
# ax2.grid(True, alpha = 1.0, linestyle='-', color='grey')
# ax2.plot([0, 8], [4, 4], color='grey', linestyle='-', linewidth=2)
# ax2.plot([0, 8], [5, 5], color='grey', linestyle='-', linewidth=2)
# ax2.plot([1, 1], [0, 6.5], color='grey', linestyle='-', linewidth=2)
# ax2.plot([3, 3], [0, 6.5], color='grey', linestyle='-', linewidth=2)
# ax2.plot([0, 8], [6.1, 6.1], color='grey', linestyle='-', linewidth=2)
# ax2.plot([0, 8], [5.6, 5.6], color='grey', linestyle='-', linewidth=2)
# plt.pcolormesh(x, y, data_plot)
# plt.show()

# data_manual = data_manual.reshape((80,1,65))
# diff = abs(data - data_manual)
# print(diff.max())

