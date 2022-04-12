import matplotlib.pyplot as plt
import os

def plot(dir, name):
    file = open(dir + name, "r")
    data=file.read().split("\n")
    data = data[2:]

    position = []
    intensity = []

    for i in range(len(data)):
        data[i] = data[i].split()
        position.append(float(data[i][0]))
        intensity.append(float(data[i][1]))

    plt.figure()
    plt.plot(position, intensity)
    plt.title(name)
    plt.xlabel("Sensor Position (m)")
    plt.ylabel("Light Intensity (V)")
    plt.savefig("/Users/jwoo/Documents/GitHub/PHY294 Labs/Interference Diffraction/data/plots/"+name+".png")
    plt.show()

if __name__ == "__main__":
    #set directory
    dir="/Users/jwoo/Documents/GitHub/PHY294 Labs/Interference Diffraction/data/"

    #plot single
    files=os.listdir(dir+"single/")
    for file in files:
        plot(dir+"single/",file)

    #plot double
    files=os.listdir(dir+"double/")
    for file in files:
        plot(dir+"double/",file)

