#confidence interval for mean
import numpy as np
import scipy.stats as stats

#sample data
data=[160, 162, 165, 158, 159, 163, 160, 162, 161, 159]
mean=np.mean(data)
std=np.std(data)
n=len(data)

#calculate standard error:
se=std/np.sqrt(n) #std/n^2
zvalue=stats.norm.ppf(0.975) #95%confidence interval
#margin of error
margin_of_error=zvalue*se
ci=[mean-margin_of_error,mean+margin_of_error]
print(mean)
print(n)
print(zvalue)
print(ci)


#Confidence Interval For Proportion
import math
import scipy.stats as stats
success=60
total=100
probab=success/total
se=math.sqrt(probab*(1-probab)/total)
z_value=stats.norm.ppf(0.975)
m_of_error=z_value*se
ci=[probab-m_of_error,probab+m_of_error]
print("zvalue",z_value)
print("ci",ci)


#confidence interval for a population mean with t distribution
#confidence interval for a population mean with t distribution
import numpy as np
import math
import scipy.stats as stats

# Sample data
data = [75, 80, 85, 70, 78]

# Sample mean and standard deviation
sample_mean = np.mean(data)
std = np.std(data)
n = len(data)

# Standard error
se = std / np.sqrt(n)
alpha =1-0.975
# t-value for 95% confidence (with n-1 degrees of freedom)
t_value = stats.t.ppf(0.975, df=n-1)

# Margin of error
margin_of_error = t_value * se

# Confidence interval
ci = [sample_mean - margin_of_error, sample_mean + margin_of_error]

# Output
print("tvalue", t_value)
print("ci",ci)
print("margin of error",margin_of_error)



# Confidence Interval for Multiple Proportions (Chi-Square Test)
import numpy as np 
import scipy.stats as stats
import math

group1_success=35
group1_total=50
group2_success=25
group2_total=50

p1=group1_success/group1_total
p2=group2_success/group2_total

se=np.sqrt(p1*(1-p1)/group1_total+p2*(1-p2)/group2_total)

zvalue=stats.norm.ppf(0.975)

margin_of_error=se*zvalue

ci=[p1-p2-margin_of_error,p1-p2+margin_of_error]

print("ci",ci)
print("zval",zvalue)
print("margin of er",margin_of_error)
print("se",se)


