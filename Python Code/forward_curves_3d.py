# Import necessary modules
from loader import *
from forward_curves import gen_forward_curve

# Load the full dataset using a function called data_import from a module called loader
full_data = data_import(asDataframe=True)

# Create a 3D figure
fig = plt.figure(figsize=(12, 12), dpi=300)
ax = fig.add_subplot(111, projection='3d')

# Get column labels and days
cols = full_data.columns
days = range(len(full_data))

# Create meshgrid for the x and y axes
# Meshgrid generates the points for a grid
X, Y = np.meshgrid(days, np.arange(len(cols)))

# Convert column labels to numerical values
Z = np.array([full_data[col].astype(float) for col in cols])

# Plot 3D lines for each column
for i, col in enumerate(cols):
    ax.plot(X[i], Y[i], Z[i], label=col, color='black')

# Add labels and title
ax.set_xlabel('Days')
ax.set_zlabel('Futures price')
ax.set_yticklabels(cols, rotation=-45)
ax.yaxis.set_major_locator(plt.MaxNLocator(nbins=13)) 
ax.set_title('Forwards curves in 3D')

# Plot forward curves for an additional 60 days
extended_days = np.arange(len(days), len(days) + 60)
for i, col in enumerate(cols):
    # Generate forward curve using np.polyfit and np.polyval
    coeffs = np.polyfit(X[i], Z[i], deg=4)
    forward_curve = np.polyval(coeffs, extended_days)
    
    # Plot forward curve separately for extended days
    ax.plot(extended_days, [i]*len(extended_days), forward_curve, linestyle='dashed', color='red')

# Set a different angle
ax.view_init(elev=10, azim=-75) 

# Show the plot
plt.show() 