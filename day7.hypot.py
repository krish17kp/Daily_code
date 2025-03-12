
# 2) Real-Life Example in Simple Terms
# Scenario: A nutrition researcher wants to see if a new diet plan reduces cholesterol levels. The researcher records the cholesterol levels of 10 volunteers before starting the new diet and again after they have been on the new diet for 8 weeks. The same 10 individuals are measured twice, giving us paired data.

# If the Paired t-Test shows a significant difference, it suggests that the new diet plan truly changes (in this case, reduces) cholesterol on average.
# If it is not significant, it suggests that any observed change could be due to chance, rather than the diet.
# In short, the Paired t-Test focuses on within-individual changes rather than on differences between two unrelated groups.

# Example Problem 1 (Easy)
# Context: A small pilot study. We want to check if a short meditation exercise improves students’ concentration test scores.

# Steps:
# Each of 5 students takes a concentration test before practicing a daily 10-minute meditation routine.
# After 4 weeks of the meditation routine, each student is tested again on the same concentration test.

import numpy as np
from scipy.stats import ttest_rel

scores_before=np.array([65,70,62,58,75])
scores_after=np.array([68,72,65,60,78])

tstat,p_value= ttest_rel(scores_before,scores_after)
print("tstat",tstat)
print("pval",p_value)

alpha =0.05
if p_value<alpha:
    print("Result: Significant difference (reject H0).")
else:
    print("Result: Not significant (fail to reject H0).")