import requests
import pprint
r=requests.get('http://23.73.212.8:1909/csiuploader/rest/api/job/showAllPromoted')
a=r.json()['']
sorted_keys = sorted(a.keys())
sorted_dict = {key:a[key] for key in sorted_keys}
sd = sorted(sorted_dict.items())
with open("CH_Jobs.txt", 'w') as f:
   for k,v in sd:
      f.write('%s:%s\n' % (k, v))
f.close()
r=requests.get('http://172.24.84.35:1909/csiuploader/rest/api/job/showAllPromoted')
c=r.json()['']
sorted_keys = sorted(c.keys())
sorted_dict = {key:c[key] for key in sorted_keys}
sd = sorted(sorted_dict.items())
with open("SJ_Jobs.txt", 'w') as f:
   for k,v in sd:
      f.write('%s:%s\n' % (k, v))
f.close()
f1 = open("CH_jobs.txt", "r")
f2 = open("SJ_jobs.txt", "r")

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