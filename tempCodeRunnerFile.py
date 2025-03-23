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