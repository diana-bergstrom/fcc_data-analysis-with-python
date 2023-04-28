# In this project, you will visualize and make calculations from medical examination data using matplotlib, seaborn, and pandas.
# The dataset values were collected during medical examinations.
# Data description
# The rows in the dataset represent patients and the columns represent information like body measurements, results from various blood tests, and lifestyle choices
# You will use the dataset to explore the relationship between cardiac disease, body measurements, blood markers, and lifestyle choices.
# File name: medical_examination.csv
# Tasks
# Create a chart similar to examples/Figure_1.png, where we show the counts of good and bad outcomes for the cholesterol, gluc, alco, active, and smoke variables for patients with cardio=1 and cardio=0 in different panels.
# Use the data to complete the following tasks in medical_data_visualizer.py:
# Add an overweight column to the data
# To determine if a person is overweight, first calculate their BMI by dividing their weight in kilograms by the square of their height in meters.
# If that value is > 25 then the person is overweight.
# Use the value 0 for NOT overweight and the value 1 for overweight.
# Normalize the data by making 0 always good and 1 always bad.
# If the value of cholesterol or gluc is 1, make the value 0.
# If the value is more than 1, make the value 1.
# Convert the data into long format and create a chart that shows the value counts of the categorical features using seaborn's catplot().
# The dataset should be split by 'Cardio' so there is one chart for each cardio value.
# The chart should look like examples/Figure_1.png.
# Clean the data.
# Filter out the following patient segments that represent incorrect data:
# diastolic pressure is higher than systolic (Keep the correct data with (df['ap_lo'] <= df['ap_hi']))
# height is less than the 2.5th percentile (Keep the correct data with (df['height'] >= df['height'].quantile(0.025)))
# height is more than the 97.5th percentile
# weight is less than the 2.5th percentile
# weight is more than the 97.5th percentile
# Create a correlation matrix using the dataset.
# Plot the correlation matrix using seaborn's heatmap().
# Mask the upper triangle.
# The chart should look like examples/Figure_2.png.
# Any time a variable is set to None, make sure to set it to the correct code.

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# Import data
df = pd.read_csv('/kaggle/input/d/dianabergstrom/medical-examination/medical_examination.csv')

# Add 'overweight' column
# height was given in cm so divide by 100 to get m
# .apply(lambda x: y if x parameter else z); lambda takes value x and compares it to a specified value, returns a value if true otherwise returns the second value
df['overweight'] = (df['weight'] / (df['height'] / 100) ** 2).apply(lambda x: 0 if x < 25 else 1)

# Normalize data by making 0 always good and 1 always bad
# If the value of 'cholesterol' or 'gluc' is 1, make the value 0; if the value is more than 1, make the value 1.
df['cholesterol'] = df['cholesterol'].apply(lambda x: 0 if x == 1 else 1)
df['gluc'] = df['gluc'].apply(lambda x: 0 if x == 1 else 1)

# Draw Categorical Plot
def draw_cat_plot():
    # Create DataFrame for cat plot using `pd.melt` using just the values from 'cholesterol', 'gluc', 'smoke', 'alco', 'active', and 'overweight'.
    # pd.melt transforms wide data into long data
    # id_vars keeps column as is (specifically cardio column in this example)
    # value_vars transforms cholesterol, gluc, smoke, alco, active, and overweight rows into columns
    df_cat = pd.melt(df, id_vars=['cardio'], value_vars=['cholesterol', 'gluc', 'smoke', 'alco', 'active', 'overweight'])

    # Group and reformat the data to split it by 'cardio'.
    # Show the counts of each feature.
    # You will have to rename one of the columns for the catplot to work correctly.
    # add new column named "total" to the df
    # Set value of 1 for each row so that the number of occurrences of each combination of categorical variables can be counted using groupby() and count()
    df_cat["total"] = 1
    df_cat = df_cat.groupby(['cardio', 'variable', 'value'], as_index=False).count()

    # Draw the catplot with 'sns.catplot()'
    # col='cardio' separates the plots into two columns based on whether a patient has a cardiovascular disease or not (0 or 1)
    # kind specifies bar plot
    # hue colors the bar based on the value of the 'value' column
    catplot = sns.catplot(data=df_cat, x='variable', y='total', col='cardio', kind='bar', hue='value', order=['active', 'alco', 'cholesterol', 'gluc', 'overweight', 'smoke',])

    # Get the figure for the output
    fig = catplot.fig

    # Do not modify the next two lines
    fig.savefig('catplot.png')
    return fig

# Draw Heat Map
def draw_heat_map():
    # Clean the data using specifications from directions (height and weight should be between 2.5th and 97.5th percentiles)
    df_heat = df[
      (df['ap_lo'] <= df['ap_hi']) &
      (df['height'] >= df['height'].quantile(0.025)) &
      (df['height'] <= df['height'].quantile(0.975)) &
      (df['weight'] >= df['weight'].quantile(0.025)) &
      (df['weight'] <= df['height'].quantile(0.975))]

    # Calculate the correlation matrix
    
    # pearson correlation coefficient is a measure of the linear correlation between two variables
    # -1 indicates a perfect negative correlation
    # 0 indicates no correlation
    # 1 indicates a perfect positive correlation)
    corr = df_heat.corr(method='pearson')

    # Generate a mask for the upper triangle
    
    # np.triu masks upper triangle of an array
    # np.tril would mask the lower triangle of an array
    mask = np.triu(corr)

    # Set up the matplotlib figure
    
    # entering figsize=(10,10) inside the () of the .subplots would specify a figure size instead of the default which can help with readability if needed
    fig, ax = plt.subplots()

    # Draw the heatmap with 'sns.heatmap()'
    
    # annotate map to show correation coefficient
    # mask hides the upper triangle of the plot
    # vmax is max value of the color map
    # set the correlation coefficients to display to one decimal place
    # linewidth sets the width of the line/space between cells
    # cbar_kws shrink colorbar to half the size of the heatmap
    # center color sclae of heatmap to 0
    sns.heatmap(data=corr, 
                annot=True, 
                fmt=".1f", 
                linewidth=.5, 
                mask=mask, 
                cbar_kws={"shrink": .5}, 
                square=True,
                vmax=.5,
                center=0);

    # Do not modify the next two lines
    fig.savefig('heatmap.png')
    return fig
