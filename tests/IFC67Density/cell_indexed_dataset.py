import sys
import math
from h5py import *
import numpy

filename = 'pres_temp.h5'
h5file = File(filename,mode='w')

n = 25

# create integer array for cell ids
iarray = numpy.arange(n,dtype='i4')
# convert to 1-based
iarray[:] += 1
dataset_name = 'Cell Ids'
h5dset = h5file.create_dataset(dataset_name, data=iarray)

# create double array for pressure
pressure = [0.101325e6, 0.5e6, 1.0e6, 2.0e6, 5.0e6]
# create double array for temperature
temperature = [10.0, 15.0, 25.0, 35.0, 55.0]

rarray = numpy.array(numpy.meshgrid(pressure, temperature)).T.reshape(-1,2)

dataset_name = 'pressure'
h5dset = h5file.create_dataset(dataset_name, data=rarray[:,0])

dataset_name = 'temperature'
h5dset = h5file.create_dataset(dataset_name, data=rarray[:,1])

h5file.close()
