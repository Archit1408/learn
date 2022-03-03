import requests
import json
r = requests.get(
    'http://flowmanager.csi2.akadns.net:8083/flowmanager/rest//monitor/data/instances/history/jobId/ReplicationManagerMRJob/timePeriodInDays/1day/list')
a = r.json()['dataInstances']
file = open('CH_DI.txt', 'wt')
for i in range(len(a)):
    b=a[i]
    file.write(str(b["metadata"]))
file.close()