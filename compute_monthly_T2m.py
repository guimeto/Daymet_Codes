# -*- coding: utf-8 -*-
"""
Created on Thu Mar 26 21:05:43 2020
Code to compute month indices
@author: guillaume
"""
import xarray as xr

yi = 1990
yf = 2019
#########################################################
tmin_in = './Daily/tmin/'
tmax_in = './Daily/tmax/'
monthly_out = './Month_Indice/' 

# Compute monthly indices
for year in range(yi,yf+1):     
        data_min = tmin_in + 'daymet_v3_tmin_' + str(year) + '_na.nc4'
        ds_min = xr.open_mfdataset(data_min, chunks = {'time': 12})         
        monthly_min = ds_min.groupby('time.month').mean('time')
       
        data_max = tmax_in + 'daymet_v3_tmax_' + str(year) + '_na.nc4'
        ds_max = xr.open_mfdataset(data_max, chunks = {'time': 12})         
        monthly_max = ds_max.groupby('time.month').mean('time')
        
        for m in monthly_max.month:
            tmp = monthly_max.sel(month=m)
            tmp.to_netcdf(monthly_out + 'tmax/Daymet_v3_Monthly_Mean_Tasmax_'+str(year) +'{:02d}'.format(int(m))+'.nc',  format='NETCDF4')
            
        for m in monthly_min.month:
            tmp = monthly_min.sel(month=m)
            tmp.to_netcdf(monthly_out + 'tmin/Daymet_v3_Monthly_Mean_Tasmin_'+str(year) +'{:02d}'.format(int(m))+'.nc',  format='NETCDF4')
            