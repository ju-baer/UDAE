import csv
import numpy as np

# Generate 1000 timesteps of data
timesteps = range(1000)
x_position = 10.0
y_position = 5.0
data = []

for t in timesteps:
    x_position += 0.5 + np.random.normal(0, 0.1)  # Simulate movement
    y_position += 0.3 + np.random.normal(0, 0.1)
    action = np.random.randint(0, 4)  # Random action (0-3)
    reward = 1.0 + np.random.normal(0, 0.2)  # Random reward
    uncertainty = 0.02 + np.random.normal(0, 0.01)  # Simulated uncertainty
    data.append([t, x_position, y_position, action, reward, uncertainty])

# Write to CSV
with open('../data/sample_data/urban_navigation_log.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['timestep', 'x_position', 'y_position', 'action', 'reward', 'uncertainty'])
    writer.writerows(data)

print("Generated urban_navigation_log.csv with 1000 timesteps.")
