# -*- coding: utf-8 -*-
"""
Created on Tue Jun 28 10:06:43 2016

@author: alysha.reinard
"""

import sys
sys.path.append('../common/')
from scipy.io.idl import readsav
import os
#from datetime import datetime, timezone
#from sunpy_time import parse_time

def read_DSCOVR_mag():

    if os.sep=="/":
        osdir=os.sep+os.path.join("Users", "alyshareinard")
    else:
        osdir=os.path.join("C:"+os.sep+"Users", "alysha.reinard.SWPC")

    rootdir=os.path.join(osdir, "Dropbox", "Work", "IDL_code", "analysis", "DSCOVR")+os.sep
    print("fulldir", rootdir)
    data=readsav(rootdir+"dsc_mag1.sav")
    print("dsc_mag1", data['results'][0:8])
    print(len(data['results']))
    dsc_mag_timetag1=[]
    dsc_mag_gsm_bx=[]
    dsc_mag_gsm_by=[]
    dsc_mag_gsm_bz=[]
    dsc_mag_qual=[]
    
    for line in data['results']:
        vals=line.split()
#        print("line", vals)

        if len(vals)==6:
            date=(vals[0].decode()+' '+ vals[1].decode())
#            print("date", date)
#            print((type(vals[1])))
            dsc_mag_timetag1.append(date)
            dsc_mag_gsm_bx.append(vals[2])
            dsc_mag_gsm_by.append(vals[3])
            dsc_mag_gsm_bz.append(vals[4])
            dsc_mag_qual.append(vals[5])


    data=readsav(rootdir+"dsc_mag2.sav")
    print("dsc_mag2", data['results'][0:8])
    dsc_mag_timetag2=[]
    dsc_mag_bt=[]
    dsc_mag_theta_gsm=[]
    dsc_mag_phi_gsm=[]
    dsc_mag_sample_size=[]
    
    for line in data['results']:
        vals=line.split()
#        print("line", vals)

        if len(vals)==6:
            date=(vals[0].decode()+' '+ vals[1].decode())
#            print("date", date)
#            print((type(vals[1])))
            dsc_mag_timetag1.append(date)
            dsc_mag_bt.append(vals[2])
            dsc_mag_theta_gsm.append(vals[3])
            dsc_mag_phi_gsm.append(vals[4])
            dsc_mag_sample_size.append(vals[5])    
    
    data=readsav(rootdir+"dsc_plasma1.sav")
    print("dsc_plasma1", data['results'][0:8])
#    
#    data=readsav(rootdir+"dsc_plasma2.sav")
#    print("dsc_plasma2", data['results'][0:8])
#    
#    data=readsav(rootdir+"ace_mag1.sav")
#    print("ace_mag1", data['results'][0:8])
#    
#    data=readsav(rootdir+"ace_mag2.sav")
#    print("ace_mag2", data['results'][0:8])
#    
#    data=readsav(rootdir+"ace_plasma.sav")
#    print("ace_plasma", data['results'][0:8])


#    current_a=data["current_a"]
#    current_b=data["current_b"]
#    current_c=data["current_c"]
#    fc_date=data["fc_date"]
#    fc_time=data["fc_time"]
#    mod_val=data["mod_value"]
#    print(mod_val)
    
read_DSCOVR_mag()