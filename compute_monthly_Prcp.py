# -*- coding: utf-8 -*-
"""
Created on Thu Mar 26 21:05:43 2020
Code to compute month indices
@author: guillaume
"""
import xarray as xr

yi = 1994
yf = 2019
#########################################################
prcp_in = './Daily/prcp/'
prcp_out = './Month_Indice/' 


# Compute monthly indices
for year in range(yi,yf+1):     
        data_in = prcp_in + 'daymet_v3_prcp_' + str(year) + '_na.nc4'
        ds_in = xr.open_mfdataset(data_in, chunks = {'time': 12})         
        monthly_mean = ds_in.groupby('time.month').mean('time')
        monthly_sum = ds_in.groupby('time.month').sum('time')
        
        for m in monthly_mean.month:
            tmp = monthly_mean.sel(month=m)
            tmp.to_netcdf(prcp_out + 'MOY/Daymet_v3_Monthly_Mean_Prcp_'+str(year) +'{:02d}'.format(int(m))+'.nc',  format='NETCDF4')
            
        for m in monthly_sum.month:
            tmp = monthly_sum.sel(month=m)
            tmp.to_netcdf(prcp_out + 'PrecTOT/Daymet_v3_Monthly_PrecTOT_'+str(year) +'{:02d}'.format(int(m))+'.nc',  format='NETCDF4')
            