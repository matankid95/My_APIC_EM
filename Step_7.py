import json
from tabulate import *

json_data = json.load(open("path_trace_data.json"))
print("Source IP", json_data["response"]["request"]["sourceIP"])
print("Destination IP", json_data["response"]["request"]["destIP"])

networkElementsInfo = json_data["response"]["networkElementsInfo"]
print("Total Network Elements Info: ", len(networkElementsInfo))

table_header = [""]
table_body = []
body = []
n = 0
for i in networkElementsInfo:
    n += 1
    body = [n, i["id"], i["ip"]]
    table_body.append( body )


print(tabulate(table_body, table_header))
