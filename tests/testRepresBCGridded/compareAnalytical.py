def flow_steady_2D_BC1st2ndkind(path,input_prefix,remove,screen_on,pf_exe,
				                             mpi_exe,num_tries):
#==============================================================================#
# Based on:
# Kolditz, et al. (2015) Thermo-Hydro-Mechanical-Chemical Processes in 
# Fractured Porous Media: Modelling and Benchmarking, Closed Form Solutions,
# Springer International Publishing, Switzerland.
# Section 2.2.4, pg.29
# "A 2D Steady-State Pressure Distribution, Boundary Conditions of 1st and
# 2nd Kind"
#
# Author: Jenn Frederick
# Date: 07/25/2017
# ******************************************************************************
  nxyz = np.zeros(3) + 1
  dxyz = np.zeros(3) + 1.
  lxyz = np.zeros(3) + 1.
  error_analysis = np.zeros(num_tries)
  dxyz_record = np.zeros((num_tries,3))
  nxyz_record = np.zeros((num_tries,3))
  test_pass = False
  try_count = 0

  # initial discretization values
  lxyz[0] = 2.       # [m] lx 
  lxyz[1] = 1.       # [m] ly 
  nxyz[0] = 20       # [m] nx
  nxyz[1] = 10       # [m] ny
  dxyz = lxyz/nxyz   # [m]
  p0 = 1.            # [MPa]
  p_offset = 1.0     # [MPa]
  ierr = 0

  while (not test_pass) and (try_count < num_tries): 
    print_discretization(lxyz,nxyz,dxyz)
    nx = int(nxyz[0]); ny = int(nxyz[1]); nz = int(nxyz[2])
    dx = dxyz[0]; dy = dxyz[1]; dz = dxyz[2]
    Lx = lxyz[0]; Ly = lxyz[1]; Lz = lxyz[2]
    try_count = try_count + 1

    p_soln = np.zeros((nx,ny))                         # [MPa]
    p_pflotran = np.zeros((nx,ny))                     # [Pa]
    x_soln = np.linspace(0.+(dx/2.),(Lx)-(dx/2.),nx)   # [m]
    y_soln = np.linspace(0.+(dy/2.),Ly-(dy/2.),ny)     # [m]

    # create the analytical solution
    i = -1
    for x in x_soln:
      i = i + 1
      j = -1
      for y in y_soln:
	j = j + 1
	p_soln[i,j] = (p0/Ly)*(x+(2*y)) + p_offset

    # run PFLOTRAN simulation
    run_pflotran(input_prefix,nxyz,dxyz,lxyz,remove,screen_on,pf_exe,mpi_exe)

    # load data from hdf5
    index_string = 'Time:  1.00000E+00 y/Liquid_Pressure [Pa]'
    p_pflotran[:,:] = read_pflotran_output_2D(path+
	           '/2D_steady_pressure_BC_1st_2nd_kind.h5',index_string,remove)
    ierr = check(p_pflotran)
  
    # Convert pressure units [Pa -> MPa]
    p_pflotran = p_pflotran/1.e6   # [MPa]
    
    max_percent_error = calc_relative_error(p_soln,p_pflotran,ierr)
    record_error(error_analysis,nxyz_record,dxyz_record,max_percent_error,
                 nxyz,dxyz,try_count)
    test_pass = does_pass(max_percent_error,try_count,num_tries)
    nxyz[0] = nxyz[0]*2.
    nxyz[1] = nxyz[1]*2.
    dxyz = lxyz/nxyz

  # Plot the PFLOTRAN and analytical solutions
  plot_2D_steady(path,x_soln,y_soln,p_soln,p_pflotran,'Distance [m]',
                 'Pressure [MPa]',"{0:.2f}".format(max_percent_error))
  
  # Plot error analysis
  plot_error(error_analysis,nxyz_record,dxyz_record,path,try_count,2)
  
  # Add test result to report card
  add_to_report(path,test_pass,max_percent_error,ierr)

  return;