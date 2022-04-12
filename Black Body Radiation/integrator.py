import os

dir="/Users/jwoo/Documents/GitHub/PHY294 Labs/Black Body Radiation/BlackbodyRadiationData1/"
files=os.listdir(dir)

f_write = open("/Users/jwoo/Documents/GitHub/PHY294 Labs/Black Body Radiation/integrals.txt", "w")

to_write = {4:[],
            5:[],
            6:[],
            7:[],
            8:[],
            9:[],
            1:[]}

for i in range(len(files)):
    if(not files[i].endswith(".txt")):
        continue
    file=open(dir + files[i], "r", 2)
    data=file.read().split("\n")
    data=data[2:]

    for f in range(len(data)):
        if(float(data[0].split("\t")[0]) < 10 or float(data[0].split("\t")[1]) < 0):
            data.pop(0)
        else:
            break

    pre=data[0].split("\t")
    pre = (float(pre[0]), float(pre[1]))
    cur=None
    r_sum = 0
    for e in range(1, len(data)):
        if(float(data[e].split("\t")[0]) > 26):
            break
        cur = data[e].split("\t")
        cur = (float(cur[0]), float(cur[1]))
        dx = cur[0] - pre[0]
        midpoint = (pre[1] + cur[1])/2
        if(pre[1] > 0 and cur[1] > 0):
            r_sum += midpoint * dx
        pre = cur
    to_write[int(files[i][3:4])].append(r_sum)
    file.close()

for list in to_write.values():
    for value in list:
        f_write.write(str(value) + "\n")
f_write.close()
print("done")