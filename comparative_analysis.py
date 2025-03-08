from loader import *
from forward_curves import gen_forward_curve
from gbm_method import geometric_brownian_motion

# Load the full dataset
full_data = data_import()

# Extract a subset from the 'Mar24' column of the 'Close' prices and convert to numpy array
subset = np.array(full_data['Mar24'].loc[:, 'Close'].dropna())

# Generate forward curve, future dates, and dates using a polynomial model of degree 4
forward_curve, poly_coeffs, future_dates, dates = gen_forward_curve(subset, degree=4)

# Functions for calculating mean, standard deviation, and mean squared error
def calculate_mean(data):
    return np.mean(data)

def calculate_standard_deviation(data):
    return np.std(data)

def calculate_mse(observed, predicted):
    n = len(observed)
    return np.sum((observed - predicted)**2) / n

# Calculate mean, standard deviation, and mean squared error for the observed data
mean_data = calculate_mean(subset)
std_dev_data = calculate_standard_deviation(subset)
mse_data = calculate_mse(subset, forward_curve)

print("Mean of data:", round(mean_data, 2))
print("Standard Deviation of data:", round(std_dev_data, 2))

# Calculate mean, standard deviation, and mean squared error for the polynomial model
mean_predicted = calculate_mean(forward_curve)
std_dev_predicted = calculate_standard_deviation(forward_curve)
mse_predicted = calculate_mse(subset, forward_curve)

print("Mean of predicted POLYNOMIAL:", round(mean_predicted, 2))
print("Standard Deviation of predicted POLYNOMIAL:", round(std_dev_predicted, 2))
print("Mean Squared Error POLYNOMIAL:", round(mse_data, 2))


# Data for "Oil Price Forecast By Day" with min, max, and price
oil_forecast_data = {
    'date': ['02/05', '02/06', '02/07', '02/08', '02/09', '02/12', '02/13', '02/14', '02/15', '02/16',
             '02/19', '02/20', '02/21', '02/22', '02/23', '02/26', '02/27', '02/28', '02/29', '03/01',
             '03/04', '03/05', '03/06', '03/07'],
    'min_price': [69.93, 69.93, 69.24, 69.41, 68.31, 69.63, 71.33, 71.85, 71.66, 72.77,
                  72.53, 73.37, 73.62, 73.25, 73.07, 73.17, 74.62, 73.85, 75.04, 72.58,
                  73.73, 72.96, 75.38, 74.47],
    'max_price': [77.29, 77.29, 76.52, 76.71, 75.50, 76.95, 78.83, 79.41, 79.20, 80.43,
                  80.17, 81.09, 81.36, 80.97, 80.77, 80.87, 82.48, 81.63, 82.94, 80.22,
                  81.49, 80.64, 83.32, 82.31],
    'price': [73.61, 73.61, 72.88, 73.06, 71.90, 73.29, 75.08, 75.63, 75.43, 76.60,
              76.35, 77.23, 77.49, 77.11, 76.92, 77.02, 78.55, 77.74, 78.99, 76.40,
              77.61, 76.80, 79.35, 78.39]
}

# Data for "WTI Oil Price Forecast By Day"
wti_forecast_data = {
    'date': ['02/05', '02/06', '02/07', '02/08', '02/09', '02/12', '02/13', '02/14', '02/15', '02/16',
             '02/19', '02/20', '02/21', '02/22', '02/23', '02/26', '02/27', '02/28', '02/29', '03/01',
             '03/04', '03/05', '03/06', '03/07'],
    'min_price': [67.38, 65.67, 64.04, 64.71, 63.68, 64.61, 66.10, 66.85, 66.41, 67.57, 67.30, 68.38, 69.26, 68.70,
                  68.46, 68.37, 69.83, 68.95, 70.22, 67.35, 68.79, 68.21, 70.65, 69.83],
    'max_price': [74.48, 72.59, 70.78, 71.53, 70.38, 71.41, 73.06, 73.89, 73.40, 74.69, 74.38, 75.58, 76.56, 75.94,
                  75.66, 75.57, 77.19, 76.21, 77.62, 74.43, 76.03, 75.39, 78.09, 77.18],
    'price': [70.93, 69.13, 67.41, 68.12, 67.03, 68.01, 69.58, 70.37, 69.90, 71.13, 70.84, 71.98, 72.91, 72.32,
                  72.06, 71.97, 73.51, 72.58, 73.92, 70.89, 72.41, 71.80, 74.37, 73.50]
}

# Calculate mean and standard deviation for "Oil Price Forecast By Day"
oil_prices = oil_forecast_data['price']
oil_mean = calculate_mean(oil_prices)
oil_std_dev = calculate_standard_deviation(oil_prices)
print("Oil Price Forecast By Day:")
print("Mean:", round(oil_mean, 2))
print("Standard Deviation:", round(oil_std_dev, 2))

# Calculate mean, standard deviation, and mean squared error for "WTI Oil Price Forecast By Day"
wti_prices = wti_forecast_data['price']
wti_mean = calculate_mean(wti_prices)
wti_std_dev = calculate_standard_deviation(wti_prices)

print("\nWTI Oil Price Forecast By Day:")
print("Mean:", round(wti_mean, 2))
print("Standard Deviation:", round(wti_std_dev, 2))

# Mean Squared Error for the predicted prices
oil_prices_predicted = oil_forecast_data['price']
wti_prices_predicted = wti_forecast_data['price']
oil_mse = calculate_mse(subset[:len(oil_prices_predicted)], oil_prices_predicted)
wti_mse = calculate_mse(subset[:len(wti_prices_predicted)], wti_prices_predicted)

print("Oil Price Forecast By Day:")
print("Mean Squared Error (MSE):", round(oil_mse, 2))

print("\nWTI Oil Price Forecast By Day:")
print("Mean Squared Error (MSE):", round(wti_mse, 2))

# Function to calculate the percentage growth between the first and last prices
def calculate_growth_percentage(prices):
    initial_price = prices[0]
    final_price = prices[-1]
    growth_percentage = ((final_price - initial_price) / initial_price) * 100
    return round(growth_percentage, 2)

# Example usage for "Oil Price Forecast By Day"
oil_prices_predicted = oil_forecast_data['price']
oil_growth_percentage = calculate_growth_percentage(oil_prices_predicted)
print("Percentage growth of Oil Price Forecast By Day:", oil_growth_percentage, "%")

# Example usage for "WTI Oil Price Forecast By Day"
wti_prices_predicted = wti_forecast_data['price']
wti_growth_percentage = calculate_growth_percentage(wti_prices_predicted)
print("Percentage growth of WTI Oil Price Forecast By Day:", wti_growth_percentage, "%")

# Plot general graph showing observed data, polynomial model, and additional forecast data
fig = plt.figure(dpi=300)
plt.plot(dates, subset, linestyle='--', label='Observed Data', color='black')
plt.plot(future_dates, forward_curve, label='Forward Curve (Polynomial)', color='red')
plt.plot([250 + i for i in range(24)], oil_forecast_data['price'], label='Oil Price Forecast', color='green')
plt.plot([250 + i for i in range(24)], wti_forecast_data['price'], label='WTI Oil Price Forecast', color='orange')
plt.xlabel('Date')
plt.ylabel('Price')
plt.title('Forward curve - Oil futures')
plt.legend()
plt.show()

# Chart showing only the polynomial model and forecast data
fig = plt.figure(dpi=300)
plt.plot(future_dates, forward_curve, label='Forward Curve (Polynomial)', color='red')
plt.plot([250 + i for i in range(24)], oil_forecast_data['price'], label='Oil Price Forecast', color='green')
plt.plot([250 + i for i in range(24)], wti_forecast_data['price'], label='WTI Oil Price Forecast', color='orange')

plt.xlabel('Date')
plt.ylabel('Price')
plt.title('Forward curve - (for 90 days)')
plt.legend()
plt.show()

# Chart showing only the polynomial model and forecast data for 25 days
fig = plt.figure(dpi=300)
plt.plot(future_dates, forward_curve, label='Forward Curve (Polynomial)', color='red')
plt.plot([250 + i for i in range(24)], oil_forecast_data['price'], label='Oil Price Forecast', color='green')
plt.plot([250 + i for i in range(24)], wti_forecast_data['price'], label='WTI Oil Price Forecast', color='orange')
plt.xlabel('Date')
plt.ylabel('Price')
plt.title('Forward curve - (for 25 days)')
plt.legend()
plt.xlim(250, 275)
plt.show()

# Chart showing only OIL and the polynomial model for 25 days
fig = plt.figure(dpi=300)
plt.plot(future_dates, forward_curve, label='Forward Curve (Polynomial)', color='red')
plt.plot([250 + i for i in range(24)], oil_forecast_data['price'], label='Oil Price Forecast', color='green')
plt.xlabel('Date')
plt.ylabel('Price')
plt.title('Forward curve (for 25 days)')
plt.legend()
plt.xlim(250, 275)
plt.show()

# Chart showing the polynomial model, min, max, and average of OIL prices for 60 days
fig = plt.figure(dpi=300)
plt.plot(future_dates, forward_curve, label='Forward Curve (Polynomial)', color='red')
plt.plot([250 + i for i in range(24)], oil_forecast_data['min_price'], label='Min Price Forecast', color='purple', linestyle='--')
plt.plot([250 + i for i in range(24)], oil_forecast_data['max_price'], label='Max Price Forecast', color='brown', linestyle='--')
plt.plot([250 + i for i in range(24)], oil_forecast_data['price'], label='Price Forecast', color='green', linestyle='--')
plt.xlabel('Date')
plt.ylabel('Price')
plt.title('Forward curve - Oil futures (from 250th observation)')
plt.legend()
plt.show()

# Generate geometric Brownian motion simulation for the next 25 days
time_steps, price = geometric_brownian_motion(subset[-1], 0.5, 126, subset)
future_dates = np.array(range(len(subset), len(subset) + 127))

plt.plot(future_dates, price, linestyle='--', color='red', label='GBM Model Price')
oil_prices = oil_forecast_data['price']
plt.plot(future_dates[:len(oil_prices)], oil_prices, label='Oil Price Forecast', color='green')
wti_prices = wti_forecast_data['price']
plt.plot(future_dates[:len(wti_prices)], wti_prices, label='WTI Oil Price Forecast', color='orange')
plt.xlabel('Date')
plt.ylabel('Price')
plt.title('Price Forecasts for 25 days')
plt.legend()
plt.xlim(249, 275)
plt.show()

# Calculate mean and standard deviation and Mean Squared Error for the predicted prices using GBM
mean_predicted_price_GBM = np.mean(price)
std_dev_predicted_price_GBM = np.std(price)
model_gbm_mse = calculate_mse(subset[:len(price)], price)

print("Mean of predicted GBM  :", round(mean_predicted_price_GBM, 2))
print("Standard Deviation of predicted GBM:", round(std_dev_predicted_price_GBM, 2))
print("MSE del modello GBM:", round(model_gbm_mse,2))

# Calculate percentage growth between days 250 and 310 for the GBM model
growth_percentage_250_310_GBM = calculate_growth_percentage(price[0:100])
print("Percentage growth between days 250 and 310 (GBM):", growth_percentage_250_310_GBM, "%")

# Calculate percentage growth between days 250 and 275 for the GBM model
growth_percentage_250_275_GBM = calculate_growth_percentage(price[0:25])
print("Percentage growth between days 250 and 275 (GBM):", growth_percentage_250_275_GBM, "%")
