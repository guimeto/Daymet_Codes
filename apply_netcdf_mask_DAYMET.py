import xarray as xr
from netCDF4 import Dataset
import netCDF4 as nc


def create_file_from_source(src_file, trg_file):
    src = nc.Dataset(src_file)
    trg = nc.Dataset(trg_file, mode='w')

    # Create the dimensions of the file
    for name, dim in src.dimensions.items():
        trg.createDimension(name, len(dim) if not dim.isunlimited() else None)

    # Copy the global attributes
   # trg.setncatts({a:src.getncattr(a) for a in src.ncattrs()})

    # Create the variables in the file
    for name, var in src.variables.items():
        trg.createVariable(name, var.dtype, var.dimensions)

        # Copy the variable attributes
        trg.variables[name].setncatts({a:var.getncattr(a) for a in var.ncattrs()})

        # Copy the variables values (as 'f4' eventually)
        if name not in tomask:
            trg.variables[name][:] = src.variables[name][:]
            
        else:    
            trg.variables[name][:] = data

    # Save the file
    trg.close()

#create 2d grid mask http://meteo.unican.es/work/xarray_seminar/xArray_seminar.html
tomask = ['tmax']
#m_f=xr.open_dataset('K:/DATA/DONNEES_AMERIQUE_DU_NORD/DAYMET/Ottawa_River_watershed_DaymetRes5.nc')
m_f=xr.open_dataset('K:/DATA/DAYMET/bv_mask_buffer/bv_mask_buffer/mask_buff_1km.nc')
lat2d=m_f.variables['lat'][:]
lon2d=m_f.variables['lon'][:]
mask = m_f['mask'][0, :, :].values

lat_bnd = [50, 43]
#lon_bnd = [270, 300]
lon_bnd = [-90, -60]

variables=['tmax']
for variable in variables:
    for year in range(1990,2019):
        for month in range(1,13):
            infile = 'K:/DATA/DAYMET/Month_Indice/tmax/Daymet_v3_Monthly_Mean_Tasmax_'+str(year) +'{:02d}'.format(int(month))+'.nc'           
            outfile = 'K:/DATA/DAYMET/Month_Indice/BV/Tmax/Daymet_v3_Monthly_Mean_Tasmax_BV_Outaouais_'+str(year)+'_'+"{0:02d}".format(month)+'.nc4'
           

            nc_Modc=xr.open_dataset(infile)
            area = nc_Modc.sel(lon=slice(*lon_bnd), lat=slice(*lat_bnd),)  
            nc_Modc.lon.values
            nc_Modf=Dataset(infile,'r')
            data = nc_Modc['tmax'].where(mask==1)
            create_file_from_source(infile, outfile)


  
  
  
  
