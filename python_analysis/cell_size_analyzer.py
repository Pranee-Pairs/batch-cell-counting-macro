#!/usr/bin/env python
# coding: utf-8

# In[1]:


import seaborn as sns
import pandas as pd
from matplotlib import pyplot as plt
import numpy as np
import glob

csv_files = glob.glob('*.csv')

# Process each file
for filename in csv_files:
    print(f"Processing {filename}...")
    
    # Read the file
    data = pd.read_csv(filename)
    areas = data['Area']
    diameters = 2 * np.sqrt(areas/np.pi)
    areas_bins = np.arange(np.floor(areas.min()), np.ceil(areas.max()), 10)
    diameters_bins = np.arange(np.floor(diameters.min()), np.ceil(diameters.max()), 1)
    
    # Make area histogram
    sns.histplot(areas, bins = areas_bins, color = 'black', fill = False).set(title = 'Cell Areas')
    plt.xlabel(u'Area (\u03bcm\u00B2)')
    plt.savefig(f'{filename}_areas.png', dpi = 600)
    plt.clf()  # Clear the plot
    
    # Make diameter histogram
    sns.histplot(diameters, bins = diameters_bins, color = 'black', fill = False).set(title = 'Cell Diameters')
    plt.xlabel(u'Diameter (\u03bcm)')
    plt.savefig(f'{filename}_diameters.png', dpi = 600)
    plt.clf()  # Clear the plot

print("Done!")


# In[ ]:




