# Imagine you want to know how many people like chocolate ice cream in a whole city. You can’t ask everyone, so you ask a sample (a smaller group). Suppose 60 out of 100 people in your sample say yes — that's 60% (sample proportion = 0.6).

# Now, suppose a company claims that only 50% of people like chocolate ice cream. You want to test if this claim is true based on your sample.

# 👉 This is called a large sample test for proportion — it helps us check if the sample result is different from the claimed proportion in the population.
# z= (p^ - p)/ √p(1-p)/n  ---formula

# A phone company claims that 50% of people like their service.
# You ask 200 people, and 130 say yes (65%).
# Is their claim correct?
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