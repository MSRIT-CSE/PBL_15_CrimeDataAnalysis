import xlrd
import xlwt
import numpy as np
import scipy
from numpy.lib.polynomial import polyval
from numpy.core.function_base import linspace


i,j,k,l,=0,0,0,0        
        
print(i)

x= [2001,2002,2003,2004,2005,2006,2007,2008,2009,2010,2011,2012,2013,2014,2015]
y = [485709,486722,475887,469311,453618,447977,436867,426885,392470,370021,351340,335504,306387,273781,238761]

p1= np.polyfit(x,y,1)
p2= np.polyfit(x,y,2)
p3= np.polyfit(x,y,3)
from scipy.interpolate import *



import matplotlib.pyplot as plt
xp = linspace(2000,2020,100)

fig,ax = plt.subplots()

plt.plot(xp,polyval(p1,xp),'r-')
plt.plot(xp,polyval(p2,xp),'m:')
plt.plot(xp,polyval(p3,xp),'b--')
ax.set_title("Prediction of Crime Data in Chicago")
ax.set_ylabel('Count')
ax.set_xlabel('Year')
plt.plot(x,y,'o')

#yfit = p1[0] * x + p1[1]
#yresid = y - yfit
#SSresid = sum(pow(yresid,2))
#SStotal = len(y) * np.var(y)

#rsq = 1- SSresid / SStotal

from scipy.stats import *

slope,intercept,r_value,p_value,std_error = linregress(x, y)
print(pow(r_value,2))


#print(rsq)
plt.show()