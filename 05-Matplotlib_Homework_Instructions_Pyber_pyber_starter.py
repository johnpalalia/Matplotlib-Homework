#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().run_line_magic('matplotlib', 'inline')
# Dependencies
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns


# In[2]:


# Read the City and Ride Data
city_data = pd.read_csv("Raw_Data/city_data.csv")
ride_data = pd.read_csv("Raw_Data/ride_data.csv")


# In[3]:


# Drop any duplicate values
city_data = city_data.drop_duplicates('city')
# Check city data
city_data.head()


# In[4]:


# Display the data table for preview
ride_data.head()


# In[5]:


# Combine the data into a single dataset
pyber_data = city_data.merge(ride_data, on = 'city', how = 'outer')
pyber_data.head()


# ## Bubble Plot of Ride Sharing Data

# In[6]:


# Obtain the x and y coordinates for each of the three city types
# Incorporate the other graph properties
# Create a legend
# Incorporate a text label regarding circle size

urban_city = pyber_data.loc[(pyber_data["type"] == "Urban")]
suburban_city = pyber_data.loc[(pyber_data["type"] == "Suburban")]
rural_city = pyber_data.loc[(pyber_data["type"] == "Rural")]


# In[7]:


avg_fare_urban_city = urban_city.groupby(['city'])['fare'].mean()
total_rides_urban_city = urban_city.groupby(['city']).count()['ride_id']
total_drivers_urban_city = urban_city.groupby(['city'])['driver_count'].value_counts()

avg_fare_suburban_city = suburban_city.groupby(['city'])['fare'].mean()
total_rides_suburban_city = suburban_city.groupby(['city']).count()['ride_id']
total_drivers_suburban_city = suburban_city.groupby(['city'])['driver_count'].value_counts()

avg_fare_rural_city = rural_city.groupby(['city'])['fare'].mean()
total_rides_rural_city = rural_city.groupby(['city']).count()['ride_id']
total_drivers_rural_city = rural_city.groupby(['city'])['driver_count'].value_counts()


# In[8]:


# Build the scatter plots for each city types
plt.scatter(total_rides_urban_city, avg_fare_urban_city,s=total_drivers_urban_city*10,
            marker ='o', facecolors ="lightcoral", edgecolors='black',alpha = 0.5, label="Urban")

plt.scatter(total_rides_suburban_city, avg_fare_suburban_city,s=total_drivers_suburban_city*10,
            marker ='o', facecolors ="lightskyblue", edgecolors='black',alpha = 0.5, label="Suburban")

plt.scatter(total_rides_rural_city, avg_fare_rural_city,s=total_drivers_rural_city*10,
            marker ='o', facecolors ="gold", edgecolors='black',alpha = 0.55, label="Rural")


# In[9]:


# Save an image of the chart and print to screen
plt.savefig("Images/Pyber Ride Sharing.png")
plt.show()


# ## Total Fares by City Type

# In[10]:


# Calculate Type Percents
# Build Pie Chart
# Save Figure

total_fare = pyber_data.groupby(['type'])['fare'].sum()

labels = ["Rural","Suburban","Urban" ]

colors = ["gold","lightskyblue","lightcoral"]
explode = (0, 0, 0.1)
plt.title("% of Total Fares By City Types")
plt.pie(total_fare, explode=explode, labels=labels, colors=colors, autopct="%1.1f%%",shadow=True, startangle=160)
plt.axis("equal")
plt.savefig("Images/% of Total Fares By City Types.png")
plt.show()


# ## Total Rides by City Type

# In[11]:


# Calculate Ride Percents
# Build Pie Chart
# Save Figure

total_rides = pyber_data.groupby(['type'])['ride_id'].count()

labels = ["Rural","Suburban","Urban" ]

colors = ["gold","lightskyblue","lightcoral"]
explode = (0, 0, 0.1)
plt.title("% of Total Rides By City Types")
plt.pie(total_rides, explode=explode, labels=labels, colors=colors,
        autopct="%1.1f%%", shadow=True, startangle=140)
plt.axis("equal")
plt.savefig("Images/% of Total Rides By City Types.png")
plt.show()


# ## Total Drivers by City Type

# In[12]:


# Calculate Driver Percents

# Build Pie Charts

# Save Figure

total_drivers = city_data.groupby(['type'])['driver_count'].sum()

labels = ["Rural","Suburban","Urban" ]

colors = ["gold","lightskyblue","lightcoral"]
explode = (0, 0, 0.1)
plt.title("% of Total Drivers By City Types")
plt.pie(total_drivers, explode=explode, labels=labels, colors=colors,
        autopct="%1.1f%%", shadow=True, startangle=140)
plt.axis("equal")
plt.savefig("Images/% of Total Drivers By City Types.png")
plt.show()


# In[ ]:


# all three pie charts show that urban areas have great percentage fares, total drivers, and total rides.


# In[ ]:


# From the data collected it can be said that it would be wise to invest and expand in the rural areas.


# In[ ]:


# From the data collected it can be said that rural areas are a lot less busy than suburban areas


# In[ ]:




