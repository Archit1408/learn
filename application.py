import requests
r=requests.get('http://flowmanager.csi4.akadns.net:8083/flowmanager/rest//monitor/applications/deployment/status')
a=r.json()['installedApplications']
sorted_keys = sorted(a.keys())
sorted_dict = {key:a[key] for key in sorted_keys}
sd = sorted(sorted_dict.items())
with open("CH.txt", 'w') as f:
   for k,v in sd:
      f.write('%s:%s\n' % (k, v))
f.close()
r = requests.get('http://flowmanager.csi5.akadns.net:8083/flowmanager/rest//monitor/applications/deployment/status')
b = r.json()['installedApplications']
sorted_keys = sorted(b.keys())
sorted_dict = {key:b[key] for key in sorted_keys}
sd = sorted(b.items())
with open("SJ.txt", 'w') as f:
   for k,v in sd:
      f.write('%s:%s\n' % (k, v))
f.close()
f1 = open("CH.txt", "r")
f2 = open("SJ.txt", "r")

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