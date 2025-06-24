import matplotlib.pyplot as plt
import numpy as np

# Sample data for session types and their durations/counts
session_types = ['Login', 'Browse', 'Checkout', 'Payment', 'Logout', 'Support']
session_durations = [15.5, 45.2, 10.1, 8.7, 5.3, 20.0] # Example: average duration in minutes

# Create the bar chart
plt.figure(figsize=(10, 6)) # Set the figure size for better readability
plt.bar(session_types, session_durations, color='skyblue')

# Add labels and title
plt.xlabel('Session Type')
plt.ylabel('Average Duration (minutes)')
plt.title('Average Session Duration by Type')

# Rotate x-axis labels if they are too long and overlap
plt.xticks(rotation=45, ha='right')

# Add a grid for better readability
plt.grid(axis='y', linestyle='--', alpha=0.7)

# Adjust layout to prevent labels from being cut off
plt.tight_layout()

# Display the chart
plt.show()