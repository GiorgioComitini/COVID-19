#!/usr/bin/python3
# -*- coding: utf-8 -*-

from sys import argv
import json
import cust_time as ctime

###--- Names and population for each region ---###
regioni={0:["Abruzzo"],1:["Basilicata"],2:["Calabria"],3:["Campania"],4:["Emilia-Romagna"],5:["Friuli-Venezia Giulia"],6:["Lazio"],7:["Liguria"],8:["Lombardia"],9:["Marche"],10:["Molise"],11:["P.A. Bolzano"],12:["P.A. Trento"],13:["Piemonte"],14:["Puglia"],15:["Sardegna"],16:["Sicilia"],17:["Toscana"],18:["Umbria"],19:["Valle d'Aosta"],20:["Veneto"],21:["Italia"]}
popolazione=[1305770,556934,1924701,5785861,4467118,1211357,5865544,1543127,10103969,1518400,302265,520891,542214,4341375,4008296,1630474,4968410,3722729,880285,125501,4907704]
popolazione_it=sum(popolazione)
for k in range(21):
    regioni[k]+=[popolazione[k]]
regioni[21]+=[popolazione_it]

fin=open("../raw-json/"+argv[1]+".json","r")
resp=json.loads(fin.read()) # JSON data as Python dict
fin.close

time=resp["results"][0]["result"]["data"]["timestamp"][:-5]
ltime=ctime.localtime()
raw_data=resp["results"][0]["result"]["data"]["dsr"]["DS"][0]["PH"][0]["DM0"] # Relevant content in raw (JSON) form
data=[el["C"] for el in raw_data] # Relevant content as Python list
arr=["Italia",sum([el[1] for el in data]),sum([el[3] for el in data])]
data+=[arr[0:2]+[arr[1]/arr[2]]+[arr[-1]]] # Adds Italy row


fout=open("../dati-regioni/"+argv[1]+".csv","w") # Writes data as CSV file
fout.write("data,denominazione_regione,dosi_somministrate,dosi_consegnate,percentuale_dosi_somministrate_su_consegnate,data_ultimo_check\n")
fout2=open("../dati-regioni-per-10k-abitanti/"+argv[1]+".csv","w") # Writes data as CSV file
fout2.write("data,denominazione_regione,dosi_somministrate_per_10k_abitanti,dosi_consegnate_per_10k_abitanti,data_ultimo_check\n")
for k,el in enumerate(data):
    fout.write(ctime.UTCtoCET(time)+","+el[0]+","+str(el[1])+","+str(el[3])+","+str(round(float(el[2])*100,2))+","+ltime+"\n")
    fout2.write(ctime.UTCtoCET(time)+","+el[0]+","+str(round(el[1]/regioni[k][1]*10000,2))+","+str(round(el[3]/regioni[k][1]*10000,2))+","+ltime+"\n")
fout.close()
fout2.close()
