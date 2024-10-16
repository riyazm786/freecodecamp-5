import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress
import numpy as np

# Import data
df = pd.read_csv('epa-sea-level.csv')

def draw_plot():
    # Create scatter plot
    plt.figure(figsize=(12, 6))
    plt.scatter(df['Year'], df['CSIRO Adjusted Sea Level'], alpha=0.5)

    # Create first line of best fit
    res = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
    years_extended = np.arange(df['Year'].min(), 2051)
    plt.plot(years_extended, res.intercept + res.slope * years_extended, 'r', label='Fitted line 1')

    # Create second line of best fit
    df_recent = df[df['Year'] >= 2000]
    res_recent = linregress(df_recent['Year'], df_recent['CSIRO Adjusted Sea Level'])
    plt.plot(years_extended, res_recent.intercept + res_recent.slope * years_extended, 'g', label='Fitted line 2')

    # Add labels and title
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.title('Rise in Sea Level')
    plt.legend()

    # Save plot and return data for testing (do not modify)
    plt.savefig('sea_level_plot.png')
    return plt.gca()

# Example usage
if __name__ == "__main__":
    draw_plot()
