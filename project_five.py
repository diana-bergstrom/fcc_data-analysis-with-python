# You will analyze a dataset of the global average sea level change since 1880.
# You will use the data to predict the sea level change through year 2050.
# Use the data to complete the following tasks:
# Use Pandas to import the data from epa-sea-level.csv.
# Use matplotlib to create a scatter plot using the Year column as the x-axis and the CSIRO Adjusted Sea Level column as the y-axis.
# Use the linregress function from scipy.stats to get the slope and y-intercept of the line of best fit. 
# Plot the line of best fit over the top of the scatter plot. 
# Make the line go through the year 2050 to predict the sea level rise in 2050.
# Plot a new line of best fit just using the data from year 2000 through the most recent year in the dataset. 
# Make the line also go through the year 2050 to predict the sea level rise in 2050 if the rate of rise continues as it has since the year 2000.
# The x label should be Year, the y label should be Sea Level (inches), and the title should be Rise in Sea Level.

import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    
    df = pd.read_csv('epa-sea-level.csv')
    
    # Create scatter plot
    
    plt.scatter(df["Year"], df["CSIRO Adjusted Sea Level"])
    
    # Create first line of best fit
    
    stats = linregress(df["Year"], df["CSIRO Adjusted Sea Level"])
    slope, intercept, r_value, p_value, std_err = stats
    # filter range of years desired and assign that to a variable for x
    x_data = range(1880, 2051)
    # create line (y=mx+b)
    y_data = slope * x_data + intercept
    # plot the linear regression line on the scatter plot
    plt.plot(x_data, y_data, color='r', label='Linear regression')
    # filter data to include years 2000 and after
    recent_df = df[df["Year"] >= 2000]
    # create a scatter plot with that data
    plt.scatter(recent_df["Year"], recent_df["CSIRO Adjusted Sea Level"])
    # calculate linear regression
    slope, intercept, r_value, p_value, std_err = linregress(recent_df["Year"], recent_df["CSIRO Adjusted Sea Level"])
    # assign range of years to variable x
    x_data = range(2000, 2051)
    
    # Add 2050 to the x-range
    
    # create line with data for new year range and plot it on the previously created scatterplot
    y_data = slope * x_data + intercept
    plt.plot(x_data, y_data, color='g', label='Linear regression since 2000')
    # calculate predicted sea level rise in 2050
    sea_level_2050 = slope * 2050 + intercept
    # print predicted sea level rise in 2050 and round to 2 decimal places
    print(f"Sea level rise in 2050: {sea_level_2050:.2f} inches")
    
    # Add labels and title
    
    plt.xlabel("Year")
    plt.ylabel("Sea Level (inches)")
    plt.title("Rise in Sea Level")
    
    # Save plot and return data for testing (DO NOT MODIFY)
    
    plt.savefig('sea_level_plot.png')
    return plt.gca()
  
  
