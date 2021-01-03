#!/usr/bin/python3
# -*- coding: utf-8 -*-

from matplotlib import pyplot as plt

###--- Reads from cumulative data ---###
fin=open("../dati-regioni/cse-covid19-ita-regioni-latest.csv","r")
fin.readline()
data=[]
for l in fin:
    line=l.strip().split(',')
    data+=[[line[0][5:10]]+line[2:-2]]
fin.close()
days=len(data)//22
data_regioni=[[data[22*k+j] for k in range(days)] for j in range(22)]

###--- Names and population for each region ---###
regioni={0:["Abruzzo"],1:["Basilicata"],2:["Calabria"],3:["Campania"],4:["Emilia-Romagna"],5:["Friuli-Venezia Giulia"],6:["Lazio"],7:["Liguria"],8:["Lombardia"],9:["Marche"],10:["Molise"],11:["P.A. Bolzano"],12:["P.A. Trento"],13:["Piemonte"],14:["Puglia"],15:["Sardegna"],16:["Sicilia"],17:["Toscana"],18:["Umbria"],19:["Valle d'Aosta"],20:["Veneto"],21:["Italia"]}
popolazione=[1305770,556934,1924701,5785861,4467118,1211357,5865544,1543127,10103969,1518400,302265,520891,542214,4341375,4008296,1630474,4968410,3722729,880285,125501,4907704]
popolazione_it=sum(popolazione)
for k in range(21):
    regioni[k]+=[popolazione[k]]
regioni[21]+=[popolazione_it]

###--- Plots ---###
x=[data_regioni[0][day][0] for day in range(days)]
#y2=[10000 for el in x]
##-- Region by region plots --##
for k in range(22):
    for day in range(days):
        for j in range(1,3):
            data_regioni[k][day][j]=int(data_regioni[k][day][j])
#- Dosi somministrate -#
    y=[data_regioni[k][day][1] for day in range(days)]
    plt.figure(figsize=(9.1,5.12),dpi=200)
    plt.ylim(bottom=0,top=max(y)*1.2)
    plt.plot(x,y,'-o')
    plt.grid(True)
    plt.title("Dosi somministrate - "+regioni[k][0])
    plt.savefig("../graphics/somministrate-"+regioni[k][0].lower().replace(" ","_")+".png")
    plt.close()
#- Percentuale dosi somministrate su consegnate -#
    y=[data_regioni[k][day][1]/data_regioni[k][day][2]*100 for day in range(days)]
    plt.figure(figsize=(9.1,5.12),dpi=200)
    plt.ylim(bottom=0,top=max(y)*1.2)
    plt.plot(x,y,'-o')
    plt.grid(True)
    plt.title("Percentuale dosi somministrate su consegnate (%) - "+regioni[k][0])
    plt.savefig("../graphics/somministrate_su_consegnate-"+regioni[k][0].lower().replace(" ","_")+".png")
    plt.close()
#- Dosi somministrate per 10k abitanti -#
    y=[data_regioni[k][day][1]/regioni[k][1]*10000 for day in range(days)]
    plt.figure(figsize=(9.1,5.12),dpi=200)
    #plt.ylim(bottom=0,top=12000)
    plt.ylim(bottom=0,top=max(y)*1.2)
    #plt.plot(x,y,'-o',x,y2,'--')
    plt.plot(x,y,'-o')
    plt.grid(True)
    plt.title("Dosi somministrate per 10k abitanti - "+regioni[k][0])
    plt.savefig("../graphics/somministrate_per_10k-"+regioni[k][0].lower().replace(" ","_")+".png")
    plt.close()
