import numpy as np
from scipy.optimize import minimize
from scipy.stats import norm

# Sample data
data = np.array([2.3, 2.1, 2.5, 2.5, 2.8, 3.0])

# Initial guess for parameters (mean and standard deviation)
parameters = [0, 2]

# Negative log-likelihood function for the normal distribution
def neg_LL(parameters, data):
    mu, sd = parameters
    if sd < 0:  # Standard deviation cannot be negative
        return np.inf
    # Log-likelihood calculation (sum of log(PDF) for each data point)
    l = np.sum(np.log(norm.pdf(data, mu, sd)))
    return -l  # Return negative log-likelihood

# Constraint to ensure that standard deviation (sd) is positive
def cons(parameters):
    return parameters[1]  # Standard deviation must be greater than 0

# Define the constraint as an inequality
const = {"type": "ineq", "fun": cons}

# Minimize the negative log-likelihood function with constraints
m = minimize(neg_LL, parameters, args=(data,), constraints=const)

# Print the estimated parameters (mean and standard deviation)
print("Estimated parameters (mean, standard deviation):", m.x)



