#!/bin/bash
#
# Shell script for downloading the italian vaccination campaign regional data in CSV format
#

# Downloads the gzipped regional vaccination data and saves it as resp_tmp.
# POST request headers are taken straight from my browser's developer tools.
printf "\n- Downloading regional data...\n\n" && \
curl -i \
-H "Host: wabi-europe-north-b-api.analysis.windows.net" \
-H "Connection: keep-alive" \
-H "Content-Length: 2380" \
-H "Accept: application/json, text/plain, */*" \
-H "RequestId: 5061c7bd-81bc-29c0-33a8-7ac97223d8ea" \
-H "X-PowerBI-ResourceKey: 388bb944-d39d-4e22-817c-90d1c8152a84" \
-H "Content-Type: application/json;charset=UTF-8" \
-H "ActivityId: eb7f5a49-9150-e52f-7760-361e6b2eddb6" \
-H "Origin: https://app.powerbi.com" \
-H "Sec-Fetch-Site: cross-site" \
-H "Sec-Fetch-Mode: cors" \
-H "Sec-Fetch-Dest: empty" \
-H "Referer: https://app.powerbi.com/" \
-H "Accept-Encoding: gzip, deflate, br" \
-H "Accept-Language: it-IT,it;q=0.9,en-US;q=0.8,en;q=0.7" \
-d '{"version":"1.0.0","queries":[{"Query":{"Commands":[{"SemanticQueryDataShapeCommand":{"Query":{"Version":2,"From":[{"Name":"t2","Entity":"TAB_REGIONI","Type":0},{"Name":"t","Entity":"TAB_MASTER","Type":0}],"Select":[{"Column":{"Expression":{"SourceRef":{"Source":"t2"}},"Property":"AREA"},"Name":"TAB_REGIONI.AREA"},{"Aggregation":{"Expression":{"Column":{"Expression":{"SourceRef":{"Source":"t"}},"Property":"TOT_SOMM"}},"Function":0},"Name":"Sum(TAB_MASTER.TOT_SOMM)"},{"Measure":{"Expression":{"SourceRef":{"Source":"t"}},"Property":"TassoVaccinazione"},"Name":"TAB_MASTER.TassoVaccinazione"},{"Aggregation":{"Expression":{"Column":{"Expression":{"SourceRef":{"Source":"t"}},"Property":"DOSI_CONSEGNATE"}},"Function":4},"Name":"Sum(TAB_MASTER.DOSI_CONSEGNATE)"}],"OrderBy":[{"Direction":1,"Expression":{"Column":{"Expression":{"SourceRef":{"Source":"t2"}},"Property":"AREA"}}}]},"Binding":{"Primary":{"Groupings":[{"Projections":[0,1,2,3]}]},"DataReduction":{"DataVolume":3,"Primary":{"Window":{"Count":500}}},"Version":1}}}]},"CacheKey":"{\"Commands\":[{\"SemanticQueryDataShapeCommand\":{\"Query\":{\"Version\":2,\"From\":[{\"Name\":\"t2\",\"Entity\":\"TAB_REGIONI\",\"Type\":0},{\"Name\":\"t\",\"Entity\":\"TAB_MASTER\",\"Type\":0}],\"Select\":[{\"Column\":{\"Expression\":{\"SourceRef\":{\"Source\":\"t2\"}},\"Property\":\"AREA\"},\"Name\":\"TAB_REGIONI.AREA\"},{\"Aggregation\":{\"Expression\":{\"Column\":{\"Expression\":{\"SourceRef\":{\"Source\":\"t\"}},\"Property\":\"TOT_SOMM\"}},\"Function\":0},\"Name\":\"Sum(TAB_MASTER.TOT_SOMM)\"},{\"Measure\":{\"Expression\":{\"SourceRef\":{\"Source\":\"t\"}},\"Property\":\"TassoVaccinazione\"},\"Name\":\"TAB_MASTER.TassoVaccinazione\"},{\"Aggregation\":{\"Expression\":{\"Column\":{\"Expression\":{\"SourceRef\":{\"Source\":\"t\"}},\"Property\":\"DOSI_CONSEGNATE\"}},\"Function\":4},\"Name\":\"Sum(TAB_MASTER.DOSI_CONSEGNATE)\"}],\"OrderBy\":[{\"Direction\":1,\"Expression\":{\"Column\":{\"Expression\":{\"SourceRef\":{\"Source\":\"t2\"}},\"Property\":\"AREA\"}}}]},\"Binding\":{\"Primary\":{\"Groupings\":[{\"Projections\":[0,1,2,3]}]},\"DataReduction\":{\"DataVolume\":3,\"Primary\":{\"Window\":{\"Count\":500}}},\"Version\":1}}}]}","QueryId":"","ApplicationContext":{"DatasetId":"5bff6260-1025-49e0-8e9b-169ade7c07f9","Sources":[{"ReportId":"b548a77c-ab0a-4d7c-a457-2e38c2914fc6"}]}}],"cancelQueries":[],"modelId":4280811}' \
-o resp_tmp \
https://wabi-europe-north-b-api.analysis.windows.net/public/reports/querydata?synchronous=true && \
DATE=$(date +%Y%m%d) && \
printf "\n- Extracting data...\n" && \
# Removes HTTP headers from resp_tmp, decompresses the remaining data into cse-covid19-ita-regioni.json and removes resp_tmp.
FILENAME="cse-covid19-ita-regioni-${DATE}" && \
sed '/HTTP/,/^\s*$/{d}' resp_tmp | gzip -d > "../raw-json/${FILENAME}.json" && \
rm -f resp_tmp && \
printf "\n- Converting data...\n" && \
# Converts the JSON file cse-covid19-ita-regioni.json into a CSV file cse-covid19-ita-regioni.csv. The former is not removed.
./JSONtoCSV.py $FILENAME && \
cp "../dati-regioni/${FILENAME}.csv" "../dati-regioni/cse-covid19-ita-regioni-latest.csv" && \
printf "\nAll done.\n\n"
