#!/bin/bash
#
# Shell script for downloading the italian vaccination campaign data in CSV format
#

# Downloads the vaccination data from https://raw.githubusercontent.com/italia/covid19-opendata-vaccini/master/dati/
# and saves them in the "ignored directory"
DATE=$(date +%Y%m%d) && \
printf "\n- Downloading regional data...\n" && \
curl -s https://raw.githubusercontent.com/italia/covid19-opendata-vaccini/master/dati/consegne-vaccini-latest.csv > ../ignored/consegne-vaccini-latest.csv && \
curl -s https://raw.githubusercontent.com/italia/covid19-opendata-vaccini/master/dati/somministrazioni-vaccini-latest.csv > ../ignored/somministrazioni-vaccini-latest.csv && \
curl -s https://raw.githubusercontent.com/italia/covid19-opendata-vaccini/master/dati/last-update-dataset.json > ../ignored/last-update-dataset.json && \
#
printf "\n- Extracting data...\n" && \
FILENAME="cse-covid19-ita-regioni-${DATE}" && \
FILENAME2="cse-covid19-ita-eta-${DATE}" && \
./extract.py $FILENAME $FILENAME2 && \
# Updates the "latest" files
printf "\n- Updating latest...\n" && \
cp "../dati-regioni/${FILENAME}.csv" "../dati-regioni/cse-covid19-ita-regioni-latest.csv" && \
cp "../dati-eta/${FILENAME2}.csv" "../dati-eta/cse-covid19-ita-eta-latest.csv" && \
cp "../dati-regioni-json/${FILENAME}.json" "../dati-regioni-json/cse-covid19-ita-regioni-latest.json" && \
cp "../dati-eta-json/${FILENAME2}.json" "../dati-eta-json/cse-covid19-ita-eta-latest.json" && \
printf "\nAll done.\n\n"
