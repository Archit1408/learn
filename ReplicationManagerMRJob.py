import time
import requests
import psycopg2
ftimestamp = int(input("last_failed_time:\n"))
failure=time.strftime("%m-%d-%Y %H:%M:%S", time.gmtime(ftimestamp))
stimestamp = int(input("last_success_time:\n"))
success=time.strftime("%m-%d-%Y %H:%M:%S", time.gmtime(stimestamp))
DC=(input("Enter DC:\n"))
if DC == "b":
    fmip= 'flowmanager.csi2.akadns.net'
    B="http://%s:8083/flowmanager/rest//monitor/data/instances/history/jobId/ReplicationManagerMRJob/timePeriodInDays/5day/list" %(fmip)
    r = requests.get('http://flowmanager.csi2.akadns.net:8083/flowmanager/rest//monitor/data/instances/history/jobId/ReplicationManagerMRJob/timePeriodInDays/5day/list')
    a = r.json()['dataInstances']

    file = open('metadata.txt', 'wt')
    for i in range(len(a)):
        b = a[i]
        file.write(str(b["metadata"]))
    file.close()

    for i in range(len(a)):
        b = a[i]
        if failure == b["lasUpdateDate"]:
            string1 = b["metadata"]
            print('\033[2;31;40m  Failed DI is', b["id"], '\n \033[2;33;40m and its metadata is \n', "", string1)



    file = open("/Users/armalhot/PycharmProjects/pythonProject/metadata.txt", "r")
    # read content of file to string
    data = file.read()
    # get number of occurrences of the substring in the string
    occurrences = data.count(string1)
    if occurrences > 1:
        print(
            '\033[2;32;40m  Nothing needs to be done with this DI  as it already replayed,i see same metadata more than once')
        r = requests.get('http://flowmanager.csi2.akadns.net:8083/flowmanager/rest//monitor/data/instances/history/jobId/ReplicationManagerMRJob/timePeriodInDays/5day/list')
        c = r.json()['dataInstances']
        for j in range(len(c)):
            d = c[j]
            if success == d["lasUpdateDate"]:
                print('\033[2;32;40m  Success DI is', d["id"], 'We need to look for DI immediately next to it')
                d = c[j + 1]
                print('\033[2;34;40m  Our Target DI is', d["id"], 'and its in ', d["dataInstanceStatus"], 'status')
                di=d["id"]
                if d["dataInstanceStatus"] == 'FAILED':
                    print(" ", d["id"], "should be replayed")
                elif d["dataInstanceStatus"] == 'STUCK':
                    print('\033[2;34;40m  Checking in PG')



                    print("  ""Operation started for CH cluster")
                    conn = psycopg2.connect(
                        database="csi2", user='csi2',
                        password='akamaka', host='db.b.csi.akamai.com', port='5432'
                    )
                    print(di)
                    sql = "select * from public.data_instance_history where  job_id like 'ReplicationManagerMRJob' and data_instance_id=%d" %(di)


                    mycursor = conn.cursor()
                    mycursor.execute(sql)
                    myresult = mycursor.fetchone()
                    print(myresult[3])


                    string2 = d["metadata"]
                    file = open("/Users/armalhot/PycharmProjects/pythonProject/metadata.txt", "r")
                    # read content of file to string
                    data = file.read()
                    # get number of occurrences of the substring in the string
                    occurrences = data.count(string2)
                    if occurrences > 1:
                        print(
                            '\033[2;32;40m  Nothing needs to be done with this DI  You can  close the alert manually')
                    else:
                        print('\033[2;31;40m  Replay this', d["id"])
                else:
                    print("No action Required")
    else:
        print('\033[2;31;40m  Its not replayed yet, you need to replay it ')

elif DC == "c":
    fmip= 'flowmanager.csi3.akadns.net'
    B="http://%s:8083/flowmanager/rest//monitor/data/instances/history/jobId/ReplicationManagerMRJob/timePeriodInDays/1day/list" %(fmip)
    r = requests.get('http://flowmanager.csi3.akadns.net:8083/flowmanager/rest//monitor/data/instances/history/jobId/ReplicationManagerMRJob/timePeriodInDays/5day/list')
    c = r.json()['dataInstances']

    file = open('metadata.txt', 'wt')
    for i in range(len(c)):
        d = c[i]
        file.write(str(d["metadata"]))
    file.close()

    for i in range(len(c)):
        d = c[i]
        if failure == d["lasUpdateDate"]:
            string1 = d["metadata"]
            print('\033[2;31;40m  Failed DI is', d["id"], '\n \033[2;33;40m and its metadata is \n', "", string1)


    file = open("metadata.txt", "r")
    # read content of file to string
    data = file.read()
    # get number of occurrences of the substring in the string
    occurrences = data.count(string1)
    if occurrences > 1:
        print(
            '\033[2;32;40m  Nothing needs to be done with this DI  as it already replayed,i see same metadata more than once')
        r = requests.get('http://flowmanager.csi3.akadns.net:8083/flowmanager/rest//monitor/data/instances/history/jobId/ReplicationManagerMRJob/timePeriodInDays/5day/list')
        c = r.json()['dataInstances']
        for j in range(len(c)):
            d = c[j]
            if success == d["lasUpdateDate"]:
                print('\033[2;32;40m  Success DI is', d["id"], 'We need to look for DI immediately next to it')
                d = c[j + 1]
                print('\033[2;34;40m  Our Target DI is', d["id"], 'and its in ', d["dataInstanceStatus"], 'status')
                if d["dataInstanceStatus"] == 'FAILED':
                    print(" ", d["id"], "should be replayed")
                elif d["dataInstanceStatus"] == 'STUCK':
                    print('\033[2;34;40m  Checking in PG')
                    print("  ""Operation started for SJ cluster")
                    conn = psycopg2.connect(
                        database="csi2", user='csi2',
                        password='akamaka', host='db.c.csi.akamai.com', port='5432'
                    )
                    print(di)
                    sql = "select * from public.data_instance_history where  job_id like 'ReplicationManagerMRJob' and data_instance_id=%d" % (
                        di)

                    mycursor = conn.cursor()
                    mycursor.execute(sql)
                    myresult = mycursor.fetchone()
                    print(myresult[3])
                else:
                    print("No action Required")
    else:
        print('\033[2;31;40mIts not replayed yet, you need to replay it ')


elif DC == "d":
    fmip= 'flowmanager.csi4.akadns.net'
    B="http://%s:8083/flowmanager/rest//monitor/data/instances/history/jobId/ReplicationManagerMRJob/timePeriodInDays/1day/list" %(fmip)
    r = requests.get('http://flowmanager.csi4.akadns.net:8083/flowmanager/rest//monitor/data/instances/history/jobId/ReplicationManagerMRJob/timePeriodInDays/5day/list')
    a = r.json()['dataInstances']

    file = open('metadata.txt', 'wt')
    for i in range(len(a)):
        b = a[i]
        file.write(str(b["metadata"]))
    file.close()

    for i in range(len(a)):
        b = a[i]
        if failure == b["lasUpdateDate"]:
            print('\033[2;31;40m  Failed DI is', b["id"], '\n \033[2;33;40m and its metadata is \n', "", b["metadata"])

    string1 = b["metadata"]
    file = open("metadata.txt", "r")
    # read content of file to string
    data = file.read()
    # get number of occurrences of the substring in the string
    occurrences = data.count(string1)
    if occurrences > 1:
        print(
            '\033[2;32;40m  Nothing needs to be done with this DI  as it already replayed,i see same metadata more than once')
        r = requests.get('http://flowmanager.csi4.akadns.net:8083/flowmanager/rest//monitor/data/instances/history/jobId/ReplicationManagerMRJob/timePeriodInDays/5day/list')
        c = r.json()['dataInstances']
        for j in range(len(c)):
            d = c[j]
            if success == d["lasUpdateDate"]:
                print('\033[2;32;40m  Success DI is', d["id"], 'We need to look for DI immediately next to it')
                d = c[j + 1]
                print('\033[2;34;40m  Our Target DI is', d["id"], 'and its in ', d["dataInstanceStatus"], 'status')
                if d["dataInstanceStatus"] == 'FAILED':
                    print(" ", d["id"], "should be replayed")
                elif d["dataInstanceStatus"] == 'STUCK':
                    print('\033[2;34;40m  Checking in Rosetta')
                    print("  ""Operation started for ETP-CH cluster")
                    conn = psycopg2.connect(
                        database="csi2", user='csi2',
                        password='akamaka', host='db.d.csi.akamai.com', port='5432'
                    )
                    print(di)
                    sql = "select * from public.data_instance_history where  job_id like 'ReplicationManagerMRJob' and data_instance_id=%d" % (
                        di)

                    mycursor = conn.cursor()
                    mycursor.execute(sql)
                    myresult = mycursor.fetchone()
                    print(myresult[3])
                    string2 = d["metadata"]
                    file = open("/Users/armalhot/PycharmProjects/pythonProject/metadata.txt", "r")
                    # read content of file to string
                    data = file.read()
                    # get number of occurrences of the substring in the string
                    occurrences = data.count(string2)
                    if occurrences > 1:
                        print(
                            '\033[2;32;40m  Nothing needs to be done with this DI  as it already replayed,i see same metadata more than once')
                    else:
                        print('\033[2;31;40m  Replay this', d["id"])
                else:
                    print("No action Required")
    else:
        print('\033[2;31;40mIts not replayed yet, you need to replay it ')


else:
    fmip= 'flowmanager.csi5.akadns.net'
    r = requests.get('http://flowmanager.csi5.akadns.net:8083/flowmanager/rest//monitor/data/instances/history/jobId/ReplicationManagerMRJob/timePeriodInDays/5day/list')
    a = r.json()['dataInstances']

    file = open('metadata.txt', 'wt')
    for i in range(len(a)):
        b = a[i]
        file.write(str(b["metadata"]))
    file.close()

    for i in range(len(a)):
        b = a[i]
        if failure == b["lasUpdateDate"]:
            print('\033[2;31;40m  Failed DI is', b["id"], '\n \033[2;33;40m and its metadata is \n', "", b["metadata"])

    string1 = b["metadata"]
    file = open("metadata.txt", "r")
    # read content of file to string
    data = file.read()
    # get number of occurrences of the substring in the string
    occurrences = data.count(string1)
    if occurrences > 1:
        print('\033[2;32;40m  Nothing needs to be done with this DI  as it already replayed,i see same metadata more than once')
        r = requests.get('http://flowmanager.csi5.akadns.net:8083/flowmanager/rest//monitor/data/instances/history/jobId/ReplicationManagerMRJob/timePeriodInDays/5day/list')
        c = r.json()['dataInstances']
        for j in range(len(c)):
            d = c[j]
            if success == d["lasUpdateDate"]:
                print('\033[2;32;40m  Success DI is', d["id"], 'We need to look for DI immediately next to it')
                d = c[j + 1]
                print('\033[2;34;40m  Our Target DI is', d["id"], 'and its in ', d["dataInstanceStatus"], 'status')
                if d["dataInstanceStatus"] == 'FAILED':
                    print(" ", d["id"], "should be replayed")
                elif d["dataInstanceStatus"] == 'STUCK':
                    print('\033[2;34;40m  Checking in PG')
                    print("  ""Operation started for ETP-SJ cluster")
                    conn = psycopg2.connect(
                        database="csi2", user='csi2',
                        password='akamaka', host='db.e.csi.akamai.com', port='5432'
                    )
                    print(di)
                    sql = "select * from public.data_instance_history where  job_id like 'ReplicationManagerMRJob' and data_instance_id=%d" % (
                        di)

                    mycursor = conn.cursor()
                    mycursor.execute(sql)
                    myresult = mycursor.fetchone()
                    print(myresult[3])
                    string2 = d["metadata"]
                    file = open("/Users/armalhot/PycharmProjects/pythonProject/metadata.txt", "r")
                    # read content of file to string
                    data = file.read()
                    # get number of occurrences of the substring in the string
                    occurrences = data.count(string2)
                    if occurrences > 1:
                        print(
                            '\033[2;32;40m  Nothing needs to be done with this DI  as it already replayed,i see same metadata more than once')
                    else:
                        print('\033[2;31;40m  Replay this', d["id"])
                else:
                    print("No action Required")
    else:
        print('\033[2;31;40mIts not replayed yet, you need to replay it ')










