# -*- coding: utf-8 -*-
"""
Created on Thu Apr 11 13:06:25 2019

@author: guillaume
"""
import datetime
import pandas as pd 
import numpy as np
from datetime import date, timedelta
from dateutil.relativedelta import relativedelta
import time 

from cdo import *
cdo = Cdo()
startcode =  time.time()
#########################################################
latb = [ 48 , 53 ]
lonb = [ -119 , -112 ]
#########################################################
rep1 = '/bgdisque1/guillaume_dueymes/DATA/DONNEES_AMERIQUE_DU_NORD/DAYMET/'
rep2 = '/bgdisque1/guillaume_dueymes/PLATEFORME/codes_python/output_netcdf/'
model = 'DAYMET_1km'
variable_in = 'prcp'

yeari=1980
yearf = 2018

########################  OUVERTURE DU CHAMPS A LIRE  ########
#### extraction des données quotidiennes
for year in range(yeari,yearf+1):
    filename= rep1 + variable_in + '/lc/nc4/' + str(year) + '/' + model + '_' + variable_in + '_lc_' + str(year) + '_d.nc4'   
    outfile = rep2 + model + '_lat_' + str(latb[0]) + '-' + str(latb[1]) + '_' + str(lonb[0]).replace('-','') + '-' + str(lonb[1]).replace('-','') + '_' +variable_in + '_' + str(year) + '_day.nc4'
    # cdo.timmean(input = filename, output = outfile, options = '-f nc' )
    cdo.sellonlatbox(lonb[0], lonb[1], latb[0], latb[1], input = filename, output = outfile, options = '-f nc' )       
    
endcode = time.time()
print(endcode-startcode)

