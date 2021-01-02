#!/usr/bin/python3
# -*- coding: utf-8 -*-

from sys import argv
import json
import cust_time as ctime

fin=open("../raw-json/"+argv[1]+".json","r")
resp=json.loads(fin.read()) # JSON data as Python dict
fin.close

time=resp["results"][0]["result"]["data"]["timestamp"][:-5]
raw_data=resp["results"][0]["result"]["data"]["dsr"]["DS"][0]["PH"][0]["DM0"] # Relevant content in raw (JSON) form
data=[el["C"] for el in raw_data] # Relevant content as Python list
arr=["Italia",sum([el[1] for el in data]),sum([el[3] for el in data])]
data+=[arr[0:2]+[arr[1]/arr[2]]+[arr[-1]]] # Adds Italy row


fout=open("../dati-regioni/"+argv[1]+".csv","w") # Writes data as CSV file
fout.write("data,denominazione_regione,dosi_somministrate,dosi_consegnate,percentuale_dosi_somministrate_su_consegnate,data_ultimo_check\n")
for el in data:
    fout.write(ctime.UTCtoCET(time)+","+el[0]+","+str(el[1])+","+str(el[3])+","+str(round(float(el[2])*100,2))+","+ctime.localtime()+"\n")
fout.close()
