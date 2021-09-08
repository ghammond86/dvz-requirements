import h5py
import numpy as np
import matplotlib.pyplot as plt
# plt.rcParams["axes.axisbelow"] = False

filenamePFLOTRAN = "/Users/deto925/Documents/PFlotran/QA/inactive/active.h5"

def printname(name):
    print(name)

# with h5py.File(filenamePFLOTRAN, "r+") as f:
#     # f.visit(printname)
#     index_string = 'Time:  0.00000E+00 d/Liquid_Pressure [Pa]'
#     presPFLOTRAN = np.array(f[index_string], '=f8')

# dx = 1.0
# dz = 1.0
# nx = 10
# nz = 10

# xCenter = np.linspace(dx/2, nx*dx - dx/2, nx)
# zCenter = np.linspace(dz/2, nz*dz - dz/2, nz)

# gradient = 0.2
# datumInit = 2.0
# rho = 1000 # density kg/m3
# g = 9.8068 # gravity
# pAtm = 101325. #Pa

# presManual = np.zeros((nx, nz))

# for i, x in enumerate(xCenter):
#     datum = datumInit + gradient * x
#     for j, z in enumerate(zCenter):
#         presManual[i,j] = pAtm + rho * g * (datum - z)

# presPFLOTRAN = np.reshape(presPFLOTRAN, (nx, nz))

# # Compare results
# diff = abs(presPFLOTRAN - presManual)/presManual
# # print(diff)
# print(diff.max())

# Steady state condition

with h5py.File(filenamePFLOTRAN, "r+") as f:
    # f.visit(printname)
    index_string = 'Time:  1.00000E+02 d/Liquid_Pressure [Pa]'
    presPFLOTRAN = np.array(f[index_string], '=f8')

dx = 1.0
dz = 1.0
nx = 10
nz = 10

xCenter = np.linspace(dx/2, nx*dx - dx/2, nx)
zCenter = np.linspace(dz/2, nz*dz - dz/2, nz)

gradient = 0.2
datumInit = 10.0
rho = 1000 # density kg/m3
g = 9.8068 # gravity
pAtm = 101325. #Pa

presManual = np.zeros((nx, nz))

for i, x in enumerate(xCenter):
    datum = datumInit + gradient * x
    for j, z in enumerate(zCenter):
        presManual[i,j] = pAtm + rho * g * (datum - z)

presPFLOTRAN = np.reshape(presPFLOTRAN, (nx, nz))

# Compare results
diff = abs(presPFLOTRAN - presManual)/presManual
# print(diff)
print(diff.max())