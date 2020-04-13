# -*- coding: utf-8 -*-
"""
Created on Wed Jun 19 10:58:37 2019

@author: guillaume
"""
#for Netcdf manipulation
import xarray as xr

#for array manipulation
import numpy as np
import pandas as pd

#for plotting
import cartopy.crs as ccrs
import cartopy.feature as cfeature
import matplotlib.pylab as plt

#for interpolation
from scipy.spatial import cKDTree

#########################################################
rep1 = 'K:/DATA/DAYMET/Daily/tmax/'
rep2 = 'K:/DATA/DAYMET/Month_Indice/BV/Tmax/'
model = 'daymet_v3'
variable_in = 'tmax'

yeari = 1990
yearf = 1990


########################  OUVERTURE DU CHAMPS A LIRE  ########
#### extraction des données quotidiennes
for year in range(yeari,yearf+1):
    filename= rep1 + model + '_' +variable_in + '_' +str(year) +'_na.nc4'   
    DS = xr.open_mfdataset(filename, decode_cf=True)
        
        
        DS = DS.assign_coords({"lon": (DS.lon, )})
        DS.lon.values
        area = DS.sel(x=slice(*lon_bnd), y=slice(*lat_bnd),)  
        
        area.to_netcdf(outfile),
        
        ds = DS.sel(y=slice(*lat_bnd), x=slice(*lon_bnd))
        DS.x
            tmp = monthly_mean.sel(month=m)
            tmp.to_netcdf(prcp_out + 'MOY/Daymet_v3_Monthly_Mean_Prcp_'+str(year) +'{:02d}'.format(int(m))+'.nc',  format='NETCDF4')
            
    filename= rep1 + variable_in + '/lc/nc4/' + str(year) + '/' + model + '_' + variable_in + '_lc_' + str(year) + '_d.nc4'   
    outfile = rep2 + model + '_lat_' + str(latb[0]) + '-' + str(latb[1]) + '_' + str(lonb[0]).replace('-','') + '-' + str(lonb[1]).replace('-','') + '_' +variable_in + '_' + str(year) + '_day.nc4'
   
    DS = xr.open_mfdataset(outfile)
    area = DS.sel(longitude=slice(*lonb), latitude=slice(*latb),)  
    area.to_netcdf(outfile)
    
endcode = time.time()
print(endcode-startcode)    

