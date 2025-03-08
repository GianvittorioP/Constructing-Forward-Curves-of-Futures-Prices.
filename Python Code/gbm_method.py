# Import necessary modules
from loader import *
from forward_curves import gen_forward_curve

# Define a function for generating geometric Brownian motion with price-based volatility
def geometric_brownian_motion(initial_price, time, steps, historical_prices):
    # Calculate time step
    dt = time / steps
    # Create an array of time steps
    time_steps = np.linspace(0, time, steps + 1)
    # Initialize an array to store simulated prices
    price = np.zeros(steps + 1)
    price[0] = initial_price

    # Calculate volatility based on historical percentage changes
    returns = np.diff(historical_prices) / historical_prices[:-1]
    volatility = np.std(returns)

    # Generate the geometric Brownian motion simulation
    for i in range(1, steps + 1):
        dWt = np.random.normal(0, np.sqrt(dt))
        drift = volatility
        price[i] = price[i - 1] * np.exp((drift - 0.5 * volatility**2) * dt + volatility * dWt)

    return time_steps, price

if __name__ == "__main__":
    
    # Load the full dataset using a function called data_import from a module called loader
    full_data = data_import()
    
    # Extract a subset from the 'Mar24' column of the 'Close' prices and convert it to a numpy array
    subset = np.array(full_data['Mar24'].loc[:, 'Close'].dropna())
    
    
    # Create an array of dates for the subset
    dates = np.array(range(len(subset)))
    # Get the initial price for the simulation (the last price of the historical subset)
    initial_price = subset[-1]
    # Set the time horizon for the simulation (0.5 years) and the number of steps (126 steps for daily simulations in half a year)
    time = 0.5
    steps = 126
    
    # Generate geometric Brownian motion simulation using the defined function
    time_steps, price = geometric_brownian_motion(initial_price, time, steps, subset)
    
    # Create an array of future dates for the simulated prices
    future_dates = np.array(range(len(subset), len(subset) + 127))
    
    # Plot the historical subset and the simulated future prices
    fig = plt.figure(dpi=300)
    plt.plot(dates, subset, color='black', label='Historical Prices')
    plt.plot(future_dates, price, linestyle='--', color='red', label='Simulated Future Prices')
    plt.xlabel('Time (in years)')
    plt.ylabel('Price')
    plt.title('Geometric Brownian Motion with Price-Based Volatility')
    plt.legend()
    plt.show()
