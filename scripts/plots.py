#!/usr/bin/python3
# -*- coding: utf-8 -*-

from datetime import datetime
from matplotlib import pyplot as plt
from matplotlib import dates as mdates

###--- Reads from cumulative data ---###
fin=open("../dati-regioni/cse-covid19-ita-regioni.csv","r")
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
x=[datetime(2021,int(data_regioni[0][day][0][:2]),int(data_regioni[0][day][0][3:])) for day in range(days)]
locator=mdates.AutoDateLocator(minticks=1,maxticks=10)
formatter=mdates.ConciseDateFormatter(locator)
#y2=[10000 for el in x]
##-- Region by region plots --##
for k in range(22):
    for day in range(days):
        for j in range(1,8):
            data_regioni[k][day][j]=float(data_regioni[k][day][j])
#- Dosi somministrate - prima -#
    y=[data_regioni[k][day][1] for day in range(days)]
    fig,ax=plt.subplots(figsize=(9.1,5.12),dpi=200)
    ax.set_ylim(bottom=0,top=max(y)*1.2)
    ax.xaxis.set_major_locator(locator)
    ax.xaxis.set_major_formatter(formatter)
    ax.plot(x,y,'-o')
    plt.grid(True)
    plt.title("Dosi somministrate (prima dose) - "+regioni[k][0])
    plt.savefig("../graphics/somministrate_prima-"+regioni[k][0].lower().replace(" ","_")+".png")
    plt.close()
#- Dosi somministrate - seconda -#
    y=[data_regioni[k][day][2] for day in range(days)]
    fig,ax=plt.subplots(figsize=(9.1,5.12),dpi=200)
    ax.set_ylim(bottom=0,top=max(y)*1.2)
    ax.xaxis.set_major_locator(locator)
    ax.xaxis.set_major_formatter(formatter)
    ax.plot(x,y,'-o')
    plt.grid(True)
    plt.title("Dosi somministrate (seconda dose) - "+regioni[k][0])
    plt.savefig("../graphics/somministrate_seconda-"+regioni[k][0].lower().replace(" ","_")+".png")
    plt.close()
#- Dosi somministrate - totale -#
    y=[data_regioni[k][day][3] for day in range(days)]
    fig,ax=plt.subplots(figsize=(9.1,5.12),dpi=200)
    ax.set_ylim(bottom=0,top=max(y)*1.2)
    ax.xaxis.set_major_locator(locator)
    ax.xaxis.set_major_formatter(formatter)
    ax.plot(x,y,'-o')
    plt.grid(True)
    plt.title("Dosi somministrate (totale) - "+regioni[k][0])
    plt.savefig("../graphics/somministrate-"+regioni[k][0].lower().replace(" ","_")+".png")
    plt.close()
#- Percentuale dosi somministrate su consegnate -#
    y=[data_regioni[k][day][5] for day in range(days)]
    fig,ax=plt.subplots(figsize=(9.1,5.12),dpi=200)
    ax.set_ylim(bottom=0,top=max(y)*1.2)
    ax.xaxis.set_major_locator(locator)
    ax.xaxis.set_major_formatter(formatter)
    ax.plot(x,y,'-o')
    plt.grid(True)
    plt.title("Percentuale dosi somministrate su consegnate (%) - "+regioni[k][0])
    plt.savefig("../graphics/somministrate_su_consegnate-"+regioni[k][0].lower().replace(" ","_")+".png")
    plt.close()
#- Dosi somministrate per 10k abitanti - prima -#
    y=[data_regioni[k][day][6] for day in range(days)]
    fig,ax=plt.subplots(figsize=(9.1,5.12),dpi=200)
    ax.set_ylim(bottom=0,top=max(y)*1.2)
    ax.xaxis.set_major_locator(locator)
    ax.xaxis.set_major_formatter(formatter)
    #ax.set_ylim(bottom=0,top=12000)
    #ax.plot(x,y,'-o',x,y2,'--')
    ax.plot(x,y,'-o')
    plt.grid(True)
    plt.title("Dosi somministrate per 10k abitanti (prima dose) - "+regioni[k][0])
    plt.savefig("../graphics/somministrate_prima_per_10k-"+regioni[k][0].lower().replace(" ","_")+".png")
    plt.close()
#- Dosi somministrate per 10k abitanti -seconda -#
    y=[data_regioni[k][day][7] for day in range(days)]
    fig,ax=plt.subplots(figsize=(9.1,5.12),dpi=200)
    ax.set_ylim(bottom=0,top=max(y)*1.2)
    ax.xaxis.set_major_locator(locator)
    ax.xaxis.set_major_formatter(formatter)
    #ax.set_ylim(bottom=0,top=12000)
    #ax.plot(x,y,'-o',x,y2,'--')
    ax.plot(x,y,'-o')
    plt.grid(True)
    plt.title("Dosi somministrate per 10k abitanti (seconda dose) - "+regioni[k][0])
    plt.savefig("../graphics/somministrate_seconda_per_10k-"+regioni[k][0].lower().replace(" ","_")+".png")
    plt.close()
