# -*- coding: utf-8 -*-
"""
Created on Mon Jul 15 10:31:05 2019

@author: guillaume
"""
import xarray as xr

model='DAYMET_1km_subset_BV'


yi = 1980
yf = 2017
#########################################################
rep_data='K:/DATA/DONNEES_AMERIQUE_DU_NORD/DAYMET/DATA/'

for year in range(yi,yf+1):
    for month in range(1,13):
        data = rep_data + model + '_tmax_'+str(year) +'_'+ '{:02d}'.format(month) +'.nc4'
        tmax = xr.open_mfdataset(data)
        data = rep_data + model + '_tmin_'+str(year) +'_'+ '{:02d}'.format(month) +'.nc4'
        tmin = xr.open_mfdataset(data)
        data = rep_data + model + '_vp_'+str(year) +'_'+ '{:02d}'.format(month) +'.nc4'
        vp = xr.open_mfdataset(data)
        
        DS = xr.merge([tmax,tmin,vp])
        
        # La formule est basée sur les travaux de J.M. Masterton et F.A. Richardson (1979)
        # humidex = (température de l'air) + h
        # h = (0,5555)*(e - 10,0) e = pression de vapeur en hPa
        # https://web.archive.org/web/20121230081513/http://www.cchst.ca/oshanswers/phys_agents/humidex.html
        
        DS['humidex'] = ((DS.tmin + DS.tmax) / 2) + (0.5555 * ((DS.vp*0.01) -10 )) 
        humidex = ((DS.tmin + DS.tmax) / 2) + (0.5555 * ((DS.vp*0.01) -10 ))  
        
        DS.humidex.attrs['long_name'] = 'humidex index'
        DS.humidex.attrs['units'] = 'nb'
        DS.humidex.attrs['description'] = 'Humidex index calculated from Richardson formula'
        
        
        DS = DS.drop('tmax')
        DS = DS.drop('tmin')
        DS = DS.drop('vp')
   
        DS.to_netcdf(rep_data + model + '_humidex_'+str(year) +'_'+ '{:02d}'.format(month) +'.nc4')
       
       