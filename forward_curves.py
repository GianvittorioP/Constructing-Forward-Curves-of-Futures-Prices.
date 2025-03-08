from loader import *

def gen_forward_curve(x, dates=None, future_dates=None, degree=4):
    # Create date ranges if not provided
    dates = np.linspace(1, 250, num=len(x))
    future_dates = np.linspace(250, 310, num=len(x))
    
    # Fit a polynomial curve to the observed data
    poly_coeffs = np.polyfit(dates, x, degree)
    
    # Generate the forward curve using the polynomial coefficients
    forward_curve = np.polyval(poly_coeffs, future_dates)
    
    return forward_curve, poly_coeffs, future_dates, dates

if __name__ == "__main__":
    
    # Load the full dataset using the data_import function from the loader module
    full_data = data_import()
    
    
    # Extract a subset from the 'Mar24' column of the 'Close' prices and convert it to a numpy array
    subset = np.array(full_data['Mar24'].loc[:, 'Close'].dropna())
    
    # Generate the forward curve and related information using the gen_forward_curve function
    forward_curve, poly_coeffs, future_dates, dates = gen_forward_curve(subset)
    
    # Plot the observed data and the estimated forward curve
    fig = plt.figure(dpi=300)
    plt.plot(dates, subset, linestyle='--', label='Observed Data', color='black')
    plt.plot(future_dates, forward_curve, label='Forward Curve (Polynomial)', color='red')
    plt.xlabel('Date')
    plt.ylabel('Price')
    plt.title('Forward curve - Oil futures expiring March 2024')
    plt.legend()
    plt.show()
