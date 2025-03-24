import math
from math import sqrt
from scipy.stats import norm
p=0.5
n=200 
x=130 #(number of people who said yes)
p_hat= x/n  #(sample proportion)
alpha =0.05
z=(p_hat-p) / sqrt(p*(1-p)/n)
z_critical=norm.ppf(1-alpha/2)

margin = z_critical * sqrt(p*(1-p)/n)
ci_low= p_hat - margin
ci_high= p_hat +margin

print("Z-score is:", z)
print("Z-critical value is:", z_critical)
print("Confidence interval is:", ci_low, "to", ci_high)

print("\n✅ Use this to decide:")
print("- If |Z| > Z-critical → Reject H0")
print("- If population proportion (", p, ") is outside the interval → Reject H0")