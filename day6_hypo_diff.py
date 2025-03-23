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


# A company claims their light bulbs last 1200 hours. A sample of 100 bulbs shows a mean of 1170 hours and std dev of 100. Test the claim at 5% level.

import numpy as np 
from scipy.stats import norm
import math
sample_mean=1170
mu=1200
sd=100
n=100
alpha =0.05
z= (sample_mean-mu)/(sd/math.sqrt(n))
z_critical = norm.ppf(1-alpha/2)

margin=z_critical*(sd/ math.sqrt(n))
ci_low=sample_mean-margin
ci_high=sample_mean+margin

print("Z-score is:", z)
print("Z-critical value is:", z_critical)
print("Confidence interval is:", ci_low, "to", ci_high)

print("If z is more than z critical - reject hO")
print("If population mean(1200) is outside confidence interval - reject hO")


# The average weight of cereal boxes is 500g. A sample of 50 shows a mean of 490g with σ = 30. Is the packing machine faulty?
import math
import numpy as np
from scipy.stats import norm
mu=500
n=50
xbar=490
sd=30
alpha=0.05
z=(xbar-mu)/(sd/math.sqrt(n))
z_critical=norm.ppf(1-alpha/2)
margin=z_critical*(sd/math.sqrt(n))
ci_low=xbar-margin
ci_high=xbar+margin
print("Z-score is:", z)
print("Z-critical value is:", z_critical)
print("Confidence interval is:", ci_low, "to", ci_high)
print("If z is more than z critical - reject hO")
print("If population mean(500) is outside confidence interval - reject hO")
