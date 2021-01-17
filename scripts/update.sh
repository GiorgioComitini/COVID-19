#!/bin/bash
#
# Shell script for downloading the italian vaccination campaign data in CSV format
#

# Downloads the gzipped vaccination data and saves them as resp_tmp and resp_age_timp.
# POST request headers are taken straight from my browser's developer tools.
DATE=$(date +%Y%m%d) && \
# The following is for the regional data
printf "\n- Downloading regional data...\n\n" && \
curl -i \
-H "Host: wabi-europe-north-b-api.analysis.windows.net" \
-H "Connection: keep-alive" \
-H "Content-Length: 3072" \
-H "Accept: application/json, text/plain, */*" \
-H "RequestId: 2fe09f8c-ba6e-0461-0d01-9d427028aba7" \
-H "X-PowerBI-ResourceKey: 388bb944-d39d-4e22-817c-90d1c8152a84" \
-H "Content-Type: application/json;charset=UTF-8" \
-H "ActivityId: 6bf4dd37-d0cb-a91b-5d29-4ccbb557a95d" \
-H "Origin: https://app.powerbi.com" \
-H "Sec-Fetch-Site: cross-site" \
-H "Sec-Fetch-Mode: cors" \
-H "Sec-Fetch-Dest: empty" \
-H "Referer: https://app.powerbi.com/" \
-H "Accept-Encoding: gzip, deflate, br" \
-H "Accept-Language: it-IT,it;q=0.9,en-US;q=0.8,en;q=0.7" \
-d '{"version":"1.0.0","queries":[{"Query":{"Commands":[{"SemanticQueryDataShapeCommand":{"Query":{"Version":2,"From":[{"Name":"t2","Entity":"TAB_REGIONI","Type":0},{"Name":"t","Entity":"TAB_MASTER","Type":0}],"Select":[{"Column":{"Expression":{"SourceRef":{"Source":"t2"}},"Property":"AREA"},"Name":"TAB_REGIONI.AREA"},{"Aggregation":{"Expression":{"Column":{"Expression":{"SourceRef":{"Source":"t"}},"Property":"TML_DOSE_1"}},"Function":0},"Name":"Sum(TAB_MASTER.TML_DOSE_1)"},{"Aggregation":{"Expression":{"Column":{"Expression":{"SourceRef":{"Source":"t"}},"Property":"TML_DOSE_2"}},"Function":0},"Name":"Sum(TAB_MASTER.TML_DOSE_2)"},{"Aggregation":{"Expression":{"Column":{"Expression":{"SourceRef":{"Source":"t"}},"Property":"TOT_SOMM"}},"Function":0},"Name":"Sum(TAB_MASTER.TOT_SOMM)"},{"Measure":{"Expression":{"SourceRef":{"Source":"t"}},"Property":"TassoVaccinazione"},"Name":"TAB_MASTER.TassoVaccinazione"},{"Aggregation":{"Expression":{"Column":{"Expression":{"SourceRef":{"Source":"t"}},"Property":"DOSI_CONSEGNATE"}},"Function":4},"Name":"Sum(TAB_MASTER.DOSI_CONSEGNATE)"}],"OrderBy":[{"Direction":1,"Expression":{"Column":{"Expression":{"SourceRef":{"Source":"t2"}},"Property":"AREA"}}}]},"Binding":{"Primary":{"Groupings":[{"Projections":[0,1,2,3,4,5]}]},"DataReduction":{"DataVolume":5,"Primary":{"Window":{"Count":500}}},"Version":1}}}]},"CacheKey":"{\"Commands\":[{\"SemanticQueryDataShapeCommand\":{\"Query\":{\"Version\":2,\"From\":[{\"Name\":\"t2\",\"Entity\":\"TAB_REGIONI\",\"Type\":0},{\"Name\":\"t\",\"Entity\":\"TAB_MASTER\",\"Type\":0}],\"Select\":[{\"Column\":{\"Expression\":{\"SourceRef\":{\"Source\":\"t2\"}},\"Property\":\"AREA\"},\"Name\":\"TAB_REGIONI.AREA\"},{\"Aggregation\":{\"Expression\":{\"Column\":{\"Expression\":{\"SourceRef\":{\"Source\":\"t\"}},\"Property\":\"TML_DOSE_1\"}},\"Function\":0},\"Name\":\"Sum(TAB_MASTER.TML_DOSE_1)\"},{\"Aggregation\":{\"Expression\":{\"Column\":{\"Expression\":{\"SourceRef\":{\"Source\":\"t\"}},\"Property\":\"TML_DOSE_2\"}},\"Function\":0},\"Name\":\"Sum(TAB_MASTER.TML_DOSE_2)\"},{\"Aggregation\":{\"Expression\":{\"Column\":{\"Expression\":{\"SourceRef\":{\"Source\":\"t\"}},\"Property\":\"TOT_SOMM\"}},\"Function\":0},\"Name\":\"Sum(TAB_MASTER.TOT_SOMM)\"},{\"Measure\":{\"Expression\":{\"SourceRef\":{\"Source\":\"t\"}},\"Property\":\"TassoVaccinazione\"},\"Name\":\"TAB_MASTER.TassoVaccinazione\"},{\"Aggregation\":{\"Expression\":{\"Column\":{\"Expression\":{\"SourceRef\":{\"Source\":\"t\"}},\"Property\":\"DOSI_CONSEGNATE\"}},\"Function\":4},\"Name\":\"Sum(TAB_MASTER.DOSI_CONSEGNATE)\"}],\"OrderBy\":[{\"Direction\":1,\"Expression\":{\"Column\":{\"Expression\":{\"SourceRef\":{\"Source\":\"t2\"}},\"Property\":\"AREA\"}}}]},\"Binding\":{\"Primary\":{\"Groupings\":[{\"Projections\":[0,1,2,3,4,5]}]},\"DataReduction\":{\"DataVolume\":5,\"Primary\":{\"Window\":{\"Count\":500}}},\"Version\":1}}}]}","QueryId":"","ApplicationContext":{"DatasetId":"5bff6260-1025-49e0-8e9b-169ade7c07f9","Sources":[{"ReportId":"b548a77c-ab0a-4d7c-a457-2e38c2914fc6"}]}}],"cancelQueries":[],"modelId":4280811}' \
-o resp_tmp \
https://wabi-europe-north-b-api.analysis.windows.net/public/reports/querydata?synchronous=true && \
printf "\n- Extracting regional data...\n" && \
# Removes HTTP headers from resp_tmp, decompresses the remaining data into cse-covid19-ita-regioni.json and removes resp_tmp.
FILENAME="cse-covid19-ita-regioni-${DATE}" && \
sed '/HTTP/,/^\s*$/{d}' resp_tmp | gzip -d > "../raw-json-regioni/${FILENAME}.json" && \
rm -f resp_tmp && \
# The following is for the age data
printf "\n- Downloading data by age groups...\n\n" && \
curl -i \
-H "Host: wabi-europe-north-b-api.analysis.windows.net" \
-H "Connection: keep-alive" \
-H "Content-Length: 1814" \
-H "Accept: application/json, text/plain, */*" \
-H "RequestId: 5476f08e-d8c9-1f0d-8857-01d62e65bd57" \
-H "X-PowerBI-ResourceKey: 388bb944-d39d-4e22-817c-90d1c8152a84" \
-H "Content-Type: application/json;charset=UTF-8" \
-H "ActivityId: 9f224cc0-0360-b683-2f0a-e38f7d993852" \
-H "Origin: https://app.powerbi.com" \
-H "Sec-Fetch-Site: cross-site" \
-H "Sec-Fetch-Mode: cors" \
-H "Sec-Fetch-Dest: empty" \
-H "Referer: https://app.powerbi.com/" \
-H "Accept-Encoding: gzip, deflate, br" \
-H "Accept-Language: it-IT,it;q=0.9,en-US;q=0.8,en;q=0.7" \
-d '{"version":"1.0.0","queries":[{"Query":{"Commands":[{"SemanticQueryDataShapeCommand":{"Query":{"Version":2,"From":[{"Name":"t","Entity":"TAB_MASTER","Type":0},{"Name":"t1","Entity":"TAB_MASTER_PIVOT","Type":0}],"Select":[{"Column":{"Expression":{"SourceRef":{"Source":"t"}},"Property":"TML_FASCIA_ETA"},"Name":"TAB_MASTER.TML_FASCIA_ETA"},{"Aggregation":{"Expression":{"Column":{"Expression":{"SourceRef":{"Source":"t1"}},"Property":"Valore"}},"Function":0},"Name":"Sum(TAB_MASTER_PIVOT.Valore)"}],"OrderBy":[{"Direction":1,"Expression":{"Column":{"Expression":{"SourceRef":{"Source":"t"}},"Property":"TML_FASCIA_ETA"}}}]},"Binding":{"Primary":{"Groupings":[{"Projections":[0,1]}]},"DataReduction":{"DataVolume":4,"Primary":{"Window":{"Count":1000}}},"Version":1}}}]},"CacheKey":"{\"Commands\":[{\"SemanticQueryDataShapeCommand\":{\"Query\":{\"Version\":2,\"From\":[{\"Name\":\"t\",\"Entity\":\"TAB_MASTER\",\"Type\":0},{\"Name\":\"t1\",\"Entity\":\"TAB_MASTER_PIVOT\",\"Type\":0}],\"Select\":[{\"Column\":{\"Expression\":{\"SourceRef\":{\"Source\":\"t\"}},\"Property\":\"TML_FASCIA_ETA\"},\"Name\":\"TAB_MASTER.TML_FASCIA_ETA\"},{\"Aggregation\":{\"Expression\":{\"Column\":{\"Expression\":{\"SourceRef\":{\"Source\":\"t1\"}},\"Property\":\"Valore\"}},\"Function\":0},\"Name\":\"Sum(TAB_MASTER_PIVOT.Valore)\"}],\"OrderBy\":[{\"Direction\":1,\"Expression\":{\"Column\":{\"Expression\":{\"SourceRef\":{\"Source\":\"t\"}},\"Property\":\"TML_FASCIA_ETA\"}}}]},\"Binding\":{\"Primary\":{\"Groupings\":[{\"Projections\":[0,1]}]},\"DataReduction\":{\"DataVolume\":4,\"Primary\":{\"Window\":{\"Count\":1000}}},\"Version\":1}}}]}","QueryId":"","ApplicationContext":{"DatasetId":"5bff6260-1025-49e0-8e9b-169ade7c07f9","Sources":[{"ReportId":"b548a77c-ab0a-4d7c-a457-2e38c2914fc6"}]}}],"cancelQueries":[],"modelId":4280811}' \
-o resp_age_tmp \
https://wabi-europe-north-b-api.analysis.windows.net/public/reports/querydata?synchronous=true && \
printf "\n- Extracting age data...\n" && \
# Removes HTTP headers from resp_age_tmp, decompresses the remaining data into cse-covid19-ita-eta.json and removes resp_age_tmp.
FILENAME2="cse-covid19-ita-eta-${DATE}" && \
sed '/HTTP/,/^\s*$/{d}' resp_age_tmp | gzip -d > "../raw-json-eta/${FILENAME2}.json" && \
rm -f resp_age_tmp && \
# Converts the JSON files into CSV files. The former are not removed.
printf "\n- Converting data...\n" && \
./JSONtoCSV.py $FILENAME $FILENAME2 && \
cp "../dati-regioni/${FILENAME}.csv" "../dati-regioni/cse-covid19-ita-regioni-latest.csv" && \
cp "../dati-eta/${FILENAME2}.csv" "../dati-eta/cse-covid19-ita-eta-latest.csv" && \
cp "../raw-json-regioni/${FILENAME}.json" "../raw-json-regioni/cse-covid19-ita-regioni-latest.json" && \
cp "../raw-json-eta/${FILENAME2}.json" "../raw-json-eta/cse-covid19-ita-eta-latest.json" && \
printf "\nAll done.\n\n"
