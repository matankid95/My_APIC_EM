import requests
import json
from my_apic_em_functions import *
from tabulate import *

requests.packages.urllib3.disable_warnings()

def get_Flow(s_ip, d_ip):
    api_url = "https://devnetsbx-netacad-apicem-2.cisco.com/api/v1/flow-analysis"
    ticket = get_ticket()
    headers = {"content-type": "application/json", "X-Auth-Token": ticket}
    data = {"sourceIP" : s_ip, "destIP" : d_ip}
    response = requests.post(api_url, data = json.dumps(data), headers=headers, verify=False)
    response_json = response.json()
    flowAnalysisId = response_json["response"]["flowAnalysisId"]
    print("Flow Analysis ID: ", flowAnalysisId)

    check_url = "https://devnetsbx-netacad-apicem-2.cisco.com/api/v1/flow-analysis/%s" % flowAnalysisId
    print("Flow Analysis URL: ", check_url)
    response1 = requests.get(check_url, headers=headers, verify=False)
    response_json1 = response1.json()
    status = response_json1["response"]["request"]["status"]
    print("Status:", status)

def get_devices():
    json_data = json.load(open("path_trace_data.json"))
    print("Source IP", json_data["response"]["request"]["sourceIP"])
    print("Destination IP", json_data["response"]["request"]["destIP"])

    networkElementsInfo = json_data["response"]["networkElementsInfo"]
    print("Total Network Elements Info: ", len(networkElementsInfo))
    i = 0
    device_list = []
    for item in networkElementsInfo:
        i += 1
        device = [i , item["id"], str(item["ip"])]
        device_list.append(device)
    table_header = ["No.", "ID", "IP"]
    print("List of Network Elements Info:\n", tabulate(device_list, table_header))

print("Source IP: 10.1.15.117\nDestination IP: 10.1.12.20\n")
s_ip = input("Source IP: ")
d_ip = input("Destination IP: ")

get_Flow('10.1.15.117', '10.1.12.20')
get_devices()
