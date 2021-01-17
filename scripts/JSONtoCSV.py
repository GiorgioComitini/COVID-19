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

###--- Demographics ---###
ages={0:["16-19",2322160],1:["20-29",6157183],2:["30-39",6952720],3:["40-49",9039799],4:["50-59",9501180],5:["60-69",7425175],6:["70-79",6006830],7:["80-89",3647476],8:["90+",794572],9:["16+",51847095]}

###--- Data by region ---###
fin=open("../raw-json-regioni/"+argv[1]+".json","r")
resp=json.loads(fin.read()) # JSON data as Python dict
fin.close

time=resp["results"][0]["result"]["data"]["timestamp"][:-5]
ltime=ctime.localtime()
raw_data=resp["results"][0]["result"]["data"]["dsr"]["DS"][0]["PH"][0]["DM0"] # Relevant content in raw (JSON) form
data=[el["C"] for el in raw_data] # Relevant content as Python list
for k in range(len(data)):
    if len(data[k])!=6:
        data[k]=[data[k][0],data[k][1],0,data[k][2],data[k][3],data[k][4]]
arr=["Italia",sum([el[1] for el in data]),sum([el[2] for el in data]),sum([el[3] for el in data]),sum([el[5] for el in data])]
data+=[arr[0:4]+[arr[3]/arr[4]]+[arr[4]]] # Adds Italy row


fout=open("../dati-regioni/"+argv[1]+".csv","w") # Writes data as CSV file
fout.write("data,denominazione_regione,dosi_somministrate_prima,dosi_somministrate_seconda,dosi_somministrate_tot,dosi_consegnate,percentuale_dosi_somministrate_tot_su_consegnate,dosi_somministrate_prima_per_10k_abitanti,dosi_somministrate_seconda_per_10k_abitanti,dosi_consegnate_per_10k_abitanti,data_ultimo_check\n")
for k,el in enumerate(data):
    fout.write(ctime.UTCtoCET(time)+","+el[0]+","+str(el[1])+","+str(el[2])+","+str(el[3])+","+str(el[5])+","+str(round(float(el[3]/el[5])*100,2))+","+str(round(el[1]/regioni[k][1]*10000,2))+","+str(round(el[2]/regioni[k][1]*10000,2))+","+str(round(el[5]/regioni[k][1]*10000,2))+","+ltime+"\n")
fout.close()

###--- Data by age ---###
fin_eta=open("../raw-json-eta/"+argv[2]+".json","r")
resp_eta=json.loads(fin_eta.read()) # JSON data as Python dict
fin_eta.close()

time_eta=resp_eta["results"][0]["result"]["data"]["timestamp"][:-5]
ltime=ctime.localtime()
raw_data_eta=resp_eta["results"][0]["result"]["data"]["dsr"]["DS"][0]["PH"][0]["DM0"] # Relevant content in raw (JSON) form
data_eta=[el["C"] for el in raw_data_eta] # Relevant content as Python list
vacc_16=sum([el[1] for el in data_eta])
data_eta+=[["16+",vacc_16]]

fout_eta=open("../dati-eta/"+argv[2]+".csv","w") # Writes data as CSV file
fout_eta.write("data,fascia_eta,dosi_somministrate,popolazione,dosi_somministrate_per_1k_abitanti,data_ultimo_check\n")
for k,el in enumerate(data_eta):
    fout_eta.write(ctime.UTCtoCET(time_eta)+","+el[0]+","+str(el[1])+","+str(ages[k][1])+","+str(round(el[1]/ages[k][1]*1000,2))+","+ltime+"\n")
fout_eta.close()
