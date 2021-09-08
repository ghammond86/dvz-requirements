import h5py
import numpy as np
import matplotlib.pyplot as plt
plt.rcParams["axes.axisbelow"] = False

filename = "parameters.h5"

def printname(name):
    print(name)

with h5py.File(filename, "r+") as f:
    # f.visit(printname)
    index_string = 'Porosity'
    poroCellID = np.array(f[index_string], '=f8')
    initPress = poroCellID * 1e6 #Pa
    # g1=f.create_group('Pressure')
    f.create_dataset('Pressure',data=initPress,dtype='float32')

    # # datasetname = 'Pressure'
    # # del f[datasetname]
    # g1.attrs['Dimension'] = np.string_('XYZ')
    # g1.attrs['Discretization'] = [1.0, 1.0, 1.0]
    # g1.attrs['Origin'] = [0.0, 0.0, 0.0]
    # g1.attrs['Transient'] = False
    # g1.attrs['Interpolation Method'] = np.string_('STEP')
    # # g1.attrs['Interpolation Method'] = 'STEP'
    # g1.attrs['Cell Centered'] = True
