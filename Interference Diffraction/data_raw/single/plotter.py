import math
import numpy as np
import matplotlib.pyplot as plt
data = np.loadtxt("/Users/jwoo/Documents/GitHub/PHY294 Labs/Interference Diffraction/data2/single/Single Slit 0.16 mm.txt")
x = data[:,0]
y = data[:,1]
from scipy.optimize import curve_fit
from scipy.stats import linregress

def fitter(x, A, wavelength, slit_width, center):
    y = A * (np.sin(math.pi*slit_width/wavelength*np.sin(np.arctan(abs(center-x)/1.1)))/(math.pi*slit_width/wavelength*np.sin(np.arctan(abs(center-x)/1.1))))**2
    return y

xdata = x
ydata = y
parameters, covariance = curve_fit(fitter, xdata, ydata, maxfev=5000)
fit_y = fitter(xdata, *parameters)
plt.figure()
plt.plot(xdata, ydata, 'r-', label='data')
plt.plot(xdata, fit_y, 'b-', label='fit')
plt.xlabel("Sensor Position (m)")
plt.ylabel("Light Intensity (V)")
plt.title("Non-Linear Curve Fit of Single Slit (a = 0.16 mm)")
plt.legend()
plt.show()

res = ydata - fitter(xdata, *parameters)
linreg = linregress(xdata, res)
plt.figure()
plt.plot(xdata, res, 'r-', label='Residuals')
plt.plot(xdata, xdata*linreg.slope + linreg.intercept, 'b-', label='Line of Best Fit')
plt.xlabel("Sensor Position (m)")
plt.ylabel("Difference in Light Intensity (V)`")
plt.title("Residuals of Best Fit")
plt.legend()
plt.show()

chi2 = ((fitter(xdata,*parameters)-ydata)**2)/(fitter(xdata,*parameters))
chi2 = np.asarray(chi2)
chi2 = np.sum(chi2)
print(chi2)