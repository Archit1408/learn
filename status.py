import requests
import pprint
def Application ():
    print("Checking  Application")
    import requests
    r = requests.get('http://flowmanager.csi4.akadns.net:8083/flowmanager/rest//monitor/applications/deployment/status')
    a = r.json()['installedApplications']
    sorted_keys = sorted(a.keys())
    sorted_dict = {key: a[key] for key in sorted_keys}
    sd = sorted(sorted_dict.items())
    with open("CH.txt", 'w') as f:
        for k, v in sd:
            f.write('%s:%s\n' % (k, v))
    f.close()
    r = requests.get('http://flowmanager.csi5.akadns.net:8083/flowmanager/rest//monitor/applications/deployment/status')
    b = r.json()['installedApplications']
    sorted_keys = sorted(b.keys())
    sorted_dict = {key: b[key] for key in sorted_keys}
    sd = sorted(b.items())
    with open("SJ.txt", 'w') as f:
        for k, v in sd:
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
    print("Checking  Jobs")

def Jobs ():
   chjobs="http://23.73.212.8:1909/csiuploader/rest/api/job/showAllActivated"
   sjjobs = "http://23.208.17.11:1909/csiuploader/rest/api/job/showAllActivated"
   r = requests.get(chjobs)
   a = r.json()
   b = pprint.pformat(a)
   file = open('CH_jobs.txt', 'wt')
   file.write(str(b))
   file.close()
   r = requests.get(sjjobs)
   c = r.json()
   d = pprint.pformat(c)
   file = open('SJ_jobs.txt', 'wt')
   file.write(str(d))
   file.close()
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
def Schema ():
    print("Checking Schema")
    import requests
    import pprint
    r = requests.get('http://23.73.212.8:1909/csiuploader/rest/api/schema/showAllActivated')
    a = r.json()
    b = pprint.pformat(a)
    file = open('CH_schema.txt', 'wt')
    file.write(str(b))
    file.close()
    r = requests.get('http://23.208.17.11:1909/csiuploader/rest/api/schema/showAllActivated')
    c = r.json()
    d = pprint.pformat(c)
    file = open('SJ_schema.txt', 'wt')
    file.write(str(d))
    file.close()
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
def Hdfs ():
    print("Checking HDFS")
    import requests
    import json
    r = requests.get('http://23.73.212.8:1909/csiuploader/rest/api/hdfs/showAllActivated')
    lst = r.json()
    df = open('CH_hdfs.txt', 'w')
    for elem in lst:
        df.write(str(elem))
        df.write('\n')
    df.close()
    r = requests.get('http://23.208.17.11:1909/csiuploader/rest/api/hdfs/showAllActivated')
    lst = r.json()
    df = open('SJ_hdfs.txt', 'w')
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


Application()
Jobs()
Schema()
Hdfs()


