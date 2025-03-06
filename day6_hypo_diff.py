import numpy as np
import scipy.stats as stats
import math

sample=np.array([55,60,52,58,61,53,59,60,56,57])
# sample=list(map(int,input("Enter sample").split(','))) it is for taking input from user
n=len(sample)
sample_mean= np.mean(sample)
sd=np.std(sample)
population_mean=57
z=(sample_mean-population_mean)/(sd/math.sqrt(n))
print("z",z)
alpha=0.05
p_value= 2*(1-stats.norm.cdf(abs(z)))
#pvalue is for if h0 is true
if p_value<alpha:
    print("Reject HO")
else:
    print("Accept")
print(p_value,z)

#large proportions
import numpy as np 
import scipy.stats as stats
from scipy.stats import norm
n= int(input())
x= int(input())

percentage=x/n

p_given=0.6
standard_error=np.sqrt((percentage*(1-p_given))/n)
z_score=(percentage-p_given)/np.sqrt((percentage*(1-p_given))/n)

# p_value= 2*(1-stats.norm.cdf(abs(z_score)))
alpha = 0.05
z_c = norm.ppf(1-alpha/2)

if  z_c_< alpha:
    print('reject ho')
else:
    print("accept")
print(z_c,p_value)