#!/bin/bash
#
# This script adds the last daily update to the file cse-covid19-ita-regioni.csv
#
# WARNING! It adds the data in append mode, so it will result in redundant behavior
# if used more than once a day

cat "../dati-regioni/cse-covid19-ita-regioni-$(date +%Y%m%d).csv" | tail -n +2 >> "../dati-regioni/cse-covid19-ita-regioni.csv"
