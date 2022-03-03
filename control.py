import time
import json
import requests
ftimestamp = int(input("last_failed_time:\n"))
failure=time.strftime("%H:%M:%S", time.gmtime(ftimestamp))
stimestamp = int(input("last_success_time:\n"))
success=time.strftime("%H:%M:%S", time.gmtime(stimestamp))
DC=input("Enter the DC  for which alert has fired for: \n" )
if DC == 'b' :
    r=requests.get('http://flowmanager.csi2.akadns.net:8083/flowmanager/rest//monitor/data/instances/history/jobId/ReplicationManagerMRJob/timePeriodInDays/1day/list')
    a = r.json()
    # Serializing json
    json_object = json.dumps(a, indent=4)
    file = open('CH_DI.txt', 'wt')
    file.write(str(json_object))
    file.close()
    a_file = open("CH_DI.txt")
    lines = a_file.readlines()[1:]
    for line in lines:
        print(line.rstrip())
    a_file.close()

DIList = []
print("Started Reading JSON file which contains multiple JSON document")
with open('CH_DI.txt') as f:
    for jsonObj in f:
        DIDict = json.loads(jsonObj)
        DIList.append(DIDict)

print("Printing each JSON Decoded Object")
for di in DIList:
    print(di["id"], di["creationDate"])