# Import all the libraries needed
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import os 
import glob 

# Set a seed for reproducibility
np.random.seed(0)

# Define a function to import data from Excel files
def data_import(asDataframe=False):
    # Get the current working directory
    path = os.getcwd() 

    # Use glob to find all files with the extension .xlsx in the 'data' directory
    files = glob.glob(os.path.join(path, "data/*.xlsx")) 

    # Create a dictionary to store data frames with keys representing months
    data = {
            'Feb24': None,
            'Mar24': None,
            'Apr24': None,
            'May24': None,
            'Jun24': None,
            'Jul24': None,
            'Ago24': None,
            'Sep24': None,
            'Oct24': None,
            'Nov24': None,
            'Dec24': None,
            'Jan25': None
            }
    
    if asDataframe:
        data = pd.DataFrame(columns=['Feb24','Mar24','Apr24','May24','Jun24','Jul24','Ago24','Sep24','Oct24','Nov24','Dec24','Jan25'])
      
    # Extract the keys from the data dictionary
    keys = list(data.keys())
    # Iterate over the enumerated list of files
    for idx, file in enumerate(files): 
        # Read each Excel file and assign it to the corresponding month key
        data[keys[idx]] = pd.read_excel(file, usecols="E")
        
    return data
