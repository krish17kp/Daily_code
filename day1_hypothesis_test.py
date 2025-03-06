#q1
import numpy as np 
import scipy.stats as stats
from scipy.stats import norm
n=12
mu=27.2
sd=3.8
mu2=32.4
n2=9
sd2=4.3
alpha=0.01
sp=np.sqrt(((n-1)*sd**2+(n2-1)*sd2**2)/(n+n2-2))
se=sp*np.sqrt(1/n+1/n2)
t=((mu-mu2)-0)/se
print()
print("t value is: ",t)
alpha=0.01
df=n+n2-2
print(se)

#q2 
import numpy as np
import scipy.stats as stats


data1=[2.86,2.77,3.18,2.80,3.14,2.87,3.19,3.24,2.91,3,2.83]
data2=[3.35,3.32,3.36,3.63,3.41,3.37,3.45,3.43,3.44,3.17,3.26,3.18,3.41]
mean1=np.mean(data1)
mean2=np.mean(data2)
std1=np.std(data1)
std2=np.std(data2)
n1=len(data1)
n2=len(data2)
alpha=0.02
sp=np.sqrt(((n1-1)*std1**2+(n2-1)*std2**2)/(n1+n2-2))
se=sp*np.sqrt(1/n1+1/n2)
t=((mean1-mean2)-(-0.25))/se
print()
print("t value is: ",t)
df=n1+n2-2
print(se)
