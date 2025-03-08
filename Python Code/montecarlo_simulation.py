from loader import *
from forward_curves import gen_forward_curve

# Load the full dataset
full_data = data_import()

# Extract a subset from the 'Mar24' column of the 'Close' prices and convert to numpy array
subset = np.array(full_data['Mar24'].loc[:, 'Close'].dropna())

# Generate forward curve, future dates, and dates
forward_curve, poly_coeffs, future_dates, dates = gen_forward_curve(subset, degree=4)

def historical_volatility(data):
    data = pd.Series(data)
    returns = np.log(data / data.shift(1))
    volatility = np.std(returns)
    return volatility

def monte_carlo_simulation(dates, observed_data, poly_coeffs, num_simulations=100, historical_volatility=None):
    simulations = []

    for _ in range(num_simulations):
        # Generate random perturbations to the polynomial coefficients using historical volatility
        perturbations = np.random.normal(0, historical_volatility, len(poly_coeffs))
        perturbed_coeffs = poly_coeffs * np.exp(perturbations)

        # Generate a new forward curve based on perturbed coefficients
        simulated_forward_curve = np.polyval(perturbed_coeffs, dates)
        simulations.append(simulated_forward_curve)

    return np.array(simulations)
  
# Estimate historical volatility from the observed subset
historical_volatility_estimate = historical_volatility(subset)

# Number of Monte Carlo simulations
num_simulations = 50

# Perform Monte Carlo simulation with the volatility model
simulations = monte_carlo_simulation(future_dates, subset, poly_coeffs, num_simulations, historical_volatility_estimate)

# Plot the observed data, the estimated forward curve, and advanced Monte Carlo simulations
plt.plot(dates, subset, linestyle='--', label='Observed Data', color='black')
plt.plot(future_dates, forward_curve, label='Forward Curve (Polynomial)', color='red')
plt.plot(future_dates, simulations.T, color='green', alpha=0.1)
plt.xlabel('Date')
plt.ylabel('Price')
plt.legend()
plt.show()
