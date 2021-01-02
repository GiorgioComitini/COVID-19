# Italian COVID-19 vaccination campaign data

This repository collects the Italian COVID-19 vaccination campaign data by region in machine-readable form, as extracted from the Government website http://www.governo.it/it/cscovid19. Its contents are structured as follows:
- **"dati-regioni"** contains the data in the CSV format
- "raw-json" contains the the data in the JSON format
- "scripts" contains the scripts I use to extract the data from the website

The data are updated every 2 minutes, being stored in a unique file labeled by the current day until a new file is created at the beginning of the next day. The latest update is stored as "cse-covid19-ita-regioni-latest.csv".

## Scripts

The "scripts" folder contains:

 - "update.sh" downloads and decompresses the data and then calls JSONtoCSV.py. It is a bash script written for Ubuntu Server 18.04 and requires curl, gzip and python3.
 - "JSONtoCSV.py" converts the JSON response into a CSV file. It is a Python3 script and requires the json module.
 - "cust_time.py" is a Python module for time operations, used by JSONtoCSV.py.
 - "unique.sh" adds the last daily update to the summary CSV file /dati-regioni/cse-covid19-ita-regioni.csv. This bash script runs at 23.59.
 - "etc" contains two unused headers for HTTP POST requests. They return the data organized by age and by category.
 
 # Disclaimer

I take no responsibility for the actual availability and update of the data. Any interested person is advised to download the scripts, modify them if they need to, and run them on their own PC. This repository cannot by any means be considered as an official source (albeit the data are of course extracted from one).
