# Import necessary modules
from loader import *
from forward_curves import gen_forward_curve

# Load the full dataset using the data_import function from the loader module
full_data = data_import()

# Extract the keys (column names) from the full_data dictionary
keys = list(full_data.keys())

# Plot 12 plots for every column of the dataframe in the same plot
fig, axs = plt.subplots(3, 4, figsize=(16, 12), dpi=300, constrained_layout=True)
fig.suptitle('Forward curve - Oil futures', fontsize=16)

# Loop through the subplots in the 3x4 grid
for i in range(3):
    for j in range(4):
        ax = axs[i, j]
        if i * 4 + j < len(keys):
            # Select the column name based on the current position in the grid
            column_name = keys[i * 4 + j]
            
            # Extract data from the selected column and create corresponding date range
            data = np.array(full_data[column_name].loc[:, 'Close'].dropna())
            dates = np.linspace(1, 250, num=len(data))
            
            # Define the degree of the polynomial for curve fitting
            d = 4
            
            # Create future date range for curve prediction
            future_dates = np.linspace(250, 310, num=len(data))
            
            # Fit a polynomial curve to the observed data
            poly_coeffs = np.polyfit(dates, data, d)
            forward_curve = np.polyval(poly_coeffs, future_dates)

            # Plot the observed data and the estimated forward curve
            ax.plot(dates, data, linestyle='--', label='Observed Data', color='black')
            ax.plot(future_dates, forward_curve, label='Forward Curve (Polynomial)', color='red')
            
            # Set labels and title for the subplot
            ax.set_xlabel('Date')
            ax.set_ylabel('Price')
            ax.set_title(f'Expiry: {column_name}')

# Adjust layout and show the plots
plt.show()
