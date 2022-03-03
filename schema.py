import requests
import re
r = requests.get('http://23.73.212.8:1909/csiuploader/rest/api/schema/showAllActivated')
a = r.json()['schema']
sorted_keys = sorted(a.keys())
sorted_dict = {key:a[key] for key in sorted_keys}
sd = sorted(sorted_dict.items())
with open("CH_schema.txt", 'w') as f:
   for k,v in sd:
      f.write('%s:%s\n' % (k, v))
f.close()
r = requests.get('http://172.24.84.35:1909/csiuploader/rest/api/schema/showAllActivated')
a = r.json()['schema']
sorted_keys = sorted(a.keys())
sorted_dict = {key:a[key] for key in sorted_keys}
sd = sorted(sorted_dict.items())
with open("schema.txt", 'w') as f:
   for k,v in sd:
      f.write('%s:%s\n' % (k, v))
f.close()


file = open('schema.txt', 'r')
df=open('SJ_schema.txt','w')

for line in file.readlines():
    if re.search('^etp', line, re.I):
        df.write(str(line))

a_file = open("SJ_schema.txt")
lines = a_file.readlines()[1:]
for line in lines:
    print(line.rstrip())
a_file.close()
f1 = open("CH_schema.txt", "r")
f2 = open("SJ_schema.txt", "r")

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