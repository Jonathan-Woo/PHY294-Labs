import matplotlib.pyplot as plt
import os

dir="/Users/jwoo/Documents/GitHub/PHY294 Labs/Black Body Radiation/BlackbodyRadiationData1/"
files=os.listdir(dir)

for i in range(len(files)):
    if(not files[i].endswith(".txt")):
        continue
    file=open(dir + files[i], "r", 2)
    data=file.read().split("\n")
    data=data[2:]

    theta=[]
    volt=[]

    for e in range(len(data)):
        data[e]=data[e].split("\t")
        volt.append(float(data[e][1]))
        theta.append(float(data[e][0]))

    plt.figure()
    plt.plot(theta,volt)
    plt.title(files[i][:-4])
    plt.xlabel("Sensor Position (Theta)")
    plt.ylabel("Light Intensity (Volts)")
    plt.savefig(dir+"plots/"+files[i][:-4]+".png")

plt.show()