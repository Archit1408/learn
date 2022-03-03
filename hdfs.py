
import requests
import json
r=requests.get('http://23.73.212.8:1909/csiuploader/rest/api/hdfs/showAllUpdated')
lst=r.json()
df=open('CH_hdfs.txt','w')
for elem in lst:
    df.write(str(elem))
    df.write('\n')
df.close()
r=requests.get('http://172.24.84.35:1909/csiuploader/rest/api/hdfs/showAllUpdtated')
lst=r.json()
df=open('SJ_hdfs.txt','w')
for elem in lst:
    df.write(str(elem))
    df.write('\n')
df.close()
f1 = open("CH_hdfs.txt", "r")
f2 = open("SJ_hdfs.txt", "r")

i = 0
for line1 in f1:
   i += 1
   for line2 in f2:
      if line1 == line2:
         pass
      else:
         print("Line ", i, ":")
         # else print that line from both files
         print("\tChicago:", line1, end='')
         print("\tSanjose:", line2, end='')
      break
f1.close()
f2.close()