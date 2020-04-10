# -*- coding: utf-8 -*-
"""
Created on Fri Apr 10 08:51:04 2020

@author: guillaume
"""

    multi_file = [f'{file}{year}{month}.nc' for year in range(1990,2020,1)]
    
    ds_clim = xr.concat([xr.open_dataset(f) for f in multi_file], 'time')
    
    data_clim = ds_clim.variables['t2m'][:].mean("time")
    data_std = ds_clim.variables['t2m'][:].std("time")
    
    stand_anomalies = xr.apply_ufunc(
        lambda x, m, s: (x - m) / s,
        ds_all.groupby("time"),
        data_clim,
        data_std,
    )
    
    stand_anomalies.to_netcdf('J:/REANALYSES/ERA5/Anomaly_stand/ERA5_T2m_Anomaly_Stand_1979-2019_vs_1990-2019_'+month+'.nc')