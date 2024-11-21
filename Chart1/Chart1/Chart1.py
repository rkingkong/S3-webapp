import pandas as pd
import matplotlib.pyplot as plt

# Data for plotting from the user input
data = {
    'Years': [2022, 2026],
    'Sales': [6.7, 9.1]  # Sales in billions
}

# Create DataFrame
df = pd.DataFrame(data)

# Creating the figure and axis objects
fig, ax = plt.subplots()

# Plotting the sales data
ax.plot(df['Years'], df['Sales'], marker='o')

# Setting the title and labels
ax.set_title('Forecasted Growth of Packaged Food Products Retail Sales in Guatemala')
ax.set_xlabel('Year')
ax.set_ylabel('Sales (in billions USD)')

# Adding the data labels
for year, sales in zip(df['Years'], df['Sales']):
    ax.annotate(f'${sales} billion', (year, sales), textcoords="offset points", xytext=(0,10), ha='center')

# Show the plot
plt.tight_layout()

# Save the plot to a file
chart_file = '/mnt/data/forecasted_sales_chart.png'
plt.savefig(chart_file)
plt.close()  # Close the plot to prevent it from displaying in the notebook

# Return the path to the saved plot image
chart_file

