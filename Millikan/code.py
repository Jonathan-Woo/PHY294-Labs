import math
import matplotlib.pyplot as plt

q = [5.397607056, 5.69022139, 17.05716555, 5.425484013, 18.58488636, 6.211736761, 12.50690841, 18.94054695, 5.937701821, 12.88022606, 14.25486089, 8.326135655, 6.867909336, 11.17469657, 5.414720383, 13.78791971, 4.762774734, 6.737635118, 18.87453974, 6.947495753, 6.205899653, 5.274989017, 7.83869533, 6.017971993, 6.87976013, 10.56339633, 5.749882834, 5.546201906, 5.640441392]

error = []
cur_error=0
min_error=100
min_charge=0

#Setup range of fundamental charges
r = []
for e in range(int(0.5/0.001)):
    r.append(1.6 + e * 0.001)

#Iterate through each fundamental charge and compute total error for each
for e in range(len(r)):
    for i in range(len(q)):
        #use the minimum squared error of multiples of the fundamental charge
        cur_error += min((q[i] - r[e]*(math.floor(q[i]/r[e]))+1)**2, (q[i] - r[e]*math.floor(q[i]/r[e]))**2)

    error.append(cur_error)

    #store charge that produces minimum error
    if(cur_error < min_error):
        min_charge = r[e]
        min_error = cur_error

    cur_error = 0

#plot figure
fig = plt.figure()
plt.plot(r, error)
plt.title("Plot of Error vs Fundamental Charge")
plt.xlabel("Fundamental Charge (10^-19 C)")
plt.ylabel("Error")
plt.show()