import numpy as np
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt

def exponential_fit(x, a, b, c):
    return a*np.exp(-b*x) + c

if __name__ == "__main__":
    x= np.array([2001,2002,2003,2004,2005,2006,2007,2008,2009,2010,2011,2012,2013,2014,2015])
    y = np.array([485709,486722,475887,469311,453618,447977,436867,426885,392470,370021,351340,335504,306387,273781,238761])
    fitting_parameters, covariance = curve_fit(exponential_fit, x, y)
    a, b, c = fitting_parameters

    next_x = 6
    next_y = exponential_fit(next_x, a, b, c)

    plt.plot(y)
    plt.plot(np.append(y, next_y), 'ro')
    plt.show()