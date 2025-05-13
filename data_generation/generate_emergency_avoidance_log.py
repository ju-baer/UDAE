import csv
import numpy as np

# Generate timesteps 450 to 550
timesteps = range(450, 551)
x_position = 50.0
y_position = 10.0
data = []

for t in timesteps:
    x_position += 0.5 + np.random.normal(0, 0.1)
    y_position += 0.2 + np.random.normal(0, 0.05)
    action = 0 if t == 500 else 1  # Brake at timestep 500 (pedestrian event)
    reward = 2.0 if t == 500 else (1.0 + np.random.normal(0, 0.2))  # Higher reward for braking
    uncertainty = 0.15 if t == 500 else (0.02 + np.random.normal(0, 0.01))  # Spike in uncertainty
    data.append([t, x_position, y_position, action, reward, uncertainty])

# Write to CSV
with open('../data/sample_data/emergency_avoidance_log.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['timestep', 'x_position', 'y_position', 'action', 'reward', 'uncertainty'])
    writer.writerows(data)

print("Generated emergency_avoidance_log.csv with 101 timesteps.")
