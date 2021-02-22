#!/usr/bin/python3
# -*- coding_ utf-8 -*-
#

###--- Modules ---###
import os
import cust_time as ctime
from sys import argv
import json

###--- Import static data ---###
from static import hr, ha
dati_regioni = hr
dati_eta = ha

###--- Format updates ---###
for key in dati_regioni.keys():
    dati_regioni[key]["dosi_somministrate_prima"] = 0
    dati_regioni[key]["dosi_somministrate_seconda"] = 0
    dati_regioni[key]["dosi_somministrate_tot"] = 0
    dati_regioni[key]["dosi_consegnate"] = 0
for key in dati_eta.keys():
    dati_eta[key]["dosi_somministrate_prima"] = 0
    dati_eta[key]["dosi_somministrate_seconda"] = 0
    dati_eta[key]["dosi_somministrate_tot"] = 0

fin = open("../ignored/last-update-dataset.json","r")
fin.readline()
last_update = fin.readline().strip().split(": \"")[1].strip("\"")[:19]
fin.close()

fin = open("../ignored/somministrazioni-vaccini-latest.csv", "r")
l=fin.readline().strip().split(",")
ar_ind=l.index("area")
fa_ind=l.index("fascia_anagrafica")
pr_ind=l.index("prima_dose")
se_ind=l.index("seconda_dose")
for line in fin:
    l=line.strip().split(",")
    dati_regioni[l[ar_ind]]["dosi_somministrate_prima"] += int(l[pr_ind])
    dati_regioni[l[ar_ind]]["dosi_somministrate_seconda"] += int(l[se_ind])
    dati_regioni[l[ar_ind]]["dosi_somministrate_tot"] += int(l[pr_ind]) + int(l[se_ind])
    dati_eta[l[fa_ind]]["dosi_somministrate_prima"] += int(l[pr_ind])
    dati_eta[l[fa_ind]]["dosi_somministrate_seconda"] += int(l[se_ind])
    dati_eta[l[fa_ind]]["dosi_somministrate_tot"] += int(l[pr_ind]) + int(l[se_ind])
fin.close()
dati_regioni["ITA"]["dosi_somministrate_prima"] = sum([dati_regioni[key]["dosi_somministrate_prima"] for key in dati_regioni.keys()])
dati_regioni["ITA"]["dosi_somministrate_seconda"] = sum([dati_regioni[key]["dosi_somministrate_seconda"] for key in dati_regioni.keys()])
dati_regioni["ITA"]["dosi_somministrate_tot"] = sum([dati_regioni[key]["dosi_somministrate_tot"] for key in dati_regioni.keys()])
dati_eta["16+"]["dosi_somministrate_prima"] = sum([dati_eta[key]["dosi_somministrate_prima"] for key in dati_eta.keys()])
dati_eta["16+"]["dosi_somministrate_seconda"] = sum([dati_eta[key]["dosi_somministrate_seconda"] for key in dati_eta.keys()])
dati_eta["16+"]["dosi_somministrate_tot"] = sum([dati_eta[key]["dosi_somministrate_tot"] for key in dati_eta.keys()])

fin = open("../ignored/consegne-vaccini-latest.csv", "r")
l=fin.readline().strip().split(",")
ar_ind=l.index("area")
nd_ind=l.index("numero_dosi")
for line in fin:
    l=line.strip().split(",")
    dati_regioni[l[ar_ind]]["dosi_consegnate"] += int(l[nd_ind])
fin.close()
dati_regioni["ITA"]["dosi_consegnate"] = sum([dati_regioni[key]["dosi_consegnate"] for key in dati_regioni.keys()])

###--- Add fields ---###
for key in dati_regioni.keys():
    dati_regioni[key]["data"] = last_update
    dati_regioni[key]["percentuale_dosi_somministrate_tot_su_consegnate"] = round(dati_regioni[key]["dosi_somministrate_tot"]/dati_regioni[key]["dosi_consegnate"]*100,2)
    dati_regioni[key]["dosi_somministrate_prima_per_10k_abitanti"] = round(dati_regioni[key]["dosi_somministrate_prima"]/dati_regioni[key]["popolazione"]*10000,2)
    dati_regioni[key]["dosi_somministrate_seconda_per_10k_abitanti"] = round(dati_regioni[key]["dosi_somministrate_seconda"]/dati_regioni[key]["popolazione"]*10000,2)
    dati_regioni[key]["dosi_consegnate_per_10k_abitanti"] = round(dati_regioni[key]["dosi_consegnate"]/dati_regioni[key]["popolazione"]*10000,2)
    dati_regioni[key]["data_ultimo_check"] = ctime.localtime()

for key in dati_eta.keys():
    dati_eta[key]["data"] = last_update
    dati_eta[key]["dosi_somministrate_prima_per_1k_abitanti"] = round(dati_eta[key]["dosi_somministrate_prima"]/dati_eta[key]["popolazione"]*1000,2)
    dati_eta[key]["dosi_somministrate_seconda_per_1k_abitanti"] = round(dati_eta[key]["dosi_somministrate_seconda"]/dati_eta[key]["popolazione"]*1000,2)
    dati_eta[key]["data_ultimo_check"] = ctime.localtime()

###--- Export files ---###
fout = open("../dati-regioni/"+argv[1]+".csv","w")
fout.write("data,denominazione_regione,dosi_somministrate_prima,dosi_somministrate_seconda,dosi_somministrate_tot,dosi_consegnate,percentuale_dosi_somministrate_tot_su_consegnate,dosi_somministrate_prima_per_10k_abitanti,dosi_somministrate_seconda_per_10k_abitanti,dosi_consegnate_per_10k_abitanti,data_ultimo_check\n")
for key in dati_regioni.keys():
    fields=dati_regioni[key]
    fout.write(fields["data"]+","+fields["denominazione_regione"]+","+str(fields["dosi_somministrate_prima"])+","+str(fields["dosi_somministrate_seconda"])+","+str(fields["dosi_somministrate_tot"])+","+str(fields["dosi_consegnate"])+","+str(fields["percentuale_dosi_somministrate_tot_su_consegnate"])+","+str(fields["dosi_somministrate_prima_per_10k_abitanti"])+","+str(fields["dosi_somministrate_seconda_per_10k_abitanti"])+","+str(fields["dosi_consegnate_per_10k_abitanti"])+","+fields["data_ultimo_check"]+"\n")
fout.close()

fout = open("../dati-eta/"+argv[2]+".csv","w")
fout.write("data,fascia_eta,dosi_somministrate_prima,dosi_somministrate_seconda,dosi_somministrate_tot,dosi_somministrate_prima_per_1k_abitanti,dosi_somministrate_seconda_per_1k_abitanti,data_ultimo_check\n")
for key in dati_eta.keys():
    fields=dati_eta[key]
    fout.write(fields["data"]+","+key+","+str(fields["dosi_somministrate_prima"])+","+str(fields["dosi_somministrate_seconda"])+","+str(fields["dosi_somministrate_tot"])+","+str(fields["dosi_somministrate_prima_per_1k_abitanti"])+","+str(fields["dosi_somministrate_seconda_per_1k_abitanti"])+","+fields["data_ultimo_check"]+"\n")
fout.close()

fout = open("../dati-regioni-json/"+argv[1]+".json","w")
fout.write(json.dumps(dati_regioni,indent = 4))
fout.close()

fout = open("../dati-eta-json/"+argv[2]+".json","w")
fout.write(json.dumps(dati_eta,indent = 4))
fout.close()

os.system("rm -drf __pycache__")
