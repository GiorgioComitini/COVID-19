# Italian COVID-19 vaccination campaign data

This repository collects the Italian COVID-19 vaccination campaign data in machine-readable form, as extracted from the Government repository https://github.com/italia/covid19-opendata-vaccini. Its contents are structured as follows:
- "dati-regioni" contains the data by region in the CSV format
- "dati-eta" contains the data by age in the CSV format
- "dati-regioni-json" contains the data by region in the JSON format
- "dati-eta-json" contains the data by age in the JSON format
- "graphics" contains the vaccination timeline region by region in graphical form
- "scripts" contains the scripts I use to extract the data from the Government repository

The data are updated every 2 minutes, being stored in a unique file labeled by the current day until a new file is created at the beginning of the next day.

The latest updates are stored as "cse-covid19-ita-[...]-latest.[csv/json]", where [...] is either "regioni" or "eta", in the directories *dati-regioni*, *dati-eta*, *dati-regioni-json* and *dati-eta-json*.

All the last daily data sets are collected in "cse-covid19-ita-[...].csv", where [...] is either "regioni" or "eta". The files get updated every day at 11.59 pm, after the last data have been downloaded.

The plots in the graphics directory are updated at 11.59 pm.

## Scripts

The "scripts" folder contains:

 - "update.sh" downloads the data and then calls *extract.py*. It is a bash script written for Ubuntu Server 18.04 and requires curl and python3.
 - "extract.py" extracts the data into CSV and JSON files. It is a Python3 script and requires the *json*, *cust_time* and *static* modules (read below for the latter two).
 - "static.py" is a Python3 module containing the population data, used by *extract.py*.
 - "cust_time.py" is a Python3 module for time operations, used by *extract.py*.
 - "unique.sh" adds the last daily updates to the summary CSV files *cse-covid19-ita-[...].csv*, where [...] is either "regioni" or "eta", in the directories *dati-regioni* and *dati-eta*. This bash script runs at 11.59 pm.
 - "plots.py" generates the plots in the graphics directory. It is a Python3 script, requires the matplotlib module and runs at 11.59 pm.
 - "etc" contains one unused header for an HTTP POST request. It returns the data organized by category.
 
 # Disclaimer

I take no responsibility for the actual availability and update of the data. Any interested person is advised to download the scripts, modify them if they need to, and run them on their own PC. This repository cannot by any means be considered as an official source (albeit the data are of course extracted from one).
