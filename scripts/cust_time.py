#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from datetime import datetime

def UTCtoCET(time): # Converts UTC to CET
    hh=time[11:13]
    if hh!='23':
        hh=str(int(hh)+1)
        hh=('0'*(2-len(hh)))+hh
        return time[:11]+hh+time[13:]
    else:
        hh='00'
        dd=time[8:10]
        if dd not in {'28','30','31'}:
            dd=str(int(dd)+1)
            dd=('0'*(2-len(dd)))+dd
            return time[:8]+dd+'T'+hh+time[13:]
        else:
            mm=time[5:7]
            yy=time[:4]
            if (dd=='28' and mm=='02') or (dd=='30' and (mm in {'04','06','09','11'})) or dd=='31':
                dd='01'
                if mm!='12':
                    mm=str(int(mm)+1)
                    mm=('0'*(2-len(mm)))+mm
                else:
                    mm='01'
                    yy=str(int(yy)+1)
            else:
                dd=str(int(dd)+1)
                dd=('0'*(2-len(dd)))+dd
            return yy+'-'+mm+'-'+dd+'T'+hh+time[13:]


def localtime(): # Outputs local time
    time_loc=datetime.now()
    time_loc=[str(time_loc.year),str(time_loc.month),str(time_loc.day),str(time_loc.hour),str(time_loc.minute),str(time_loc.second)]
    for k in range(1,6):
        time_loc[k]='0'*(2-len(time_loc[k]))+time_loc[k]
    return time_loc[0]+'-'+time_loc[1]+'-'+time_loc[2]+'T'+time_loc[3]+':'+time_loc[4]+':'+time_loc[5]
