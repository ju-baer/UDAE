import csv
import numpy as np
import random

# Generate 5 scenarios, each with timesteps 450 to 550
data = []
for scenario in range(1, 6):
    x_position = 50.0 + np.random.normal(0, 2)
    y_position = 10.0 + np.random.normal(0, 2)
    pedestrian_timestep = random.randint(470, 530)  # Random pedestrian event

    for t in range(450, 551):
        x_position += 0.5 + np.random.normal(0, 0.1)
        y_position += 0.2 + np.random.normal(0, 0.05)
        action = 0 if t == pedestrian_timestep else 1
        reward = 2.0 if t == pedestrian_timestep else (1.0 + np.random.normal(0, 0.2))
        uncertainty = 0.15 if t == pedestrian_timestep else (0.02 + np.random.normal(0, 0.01))
        data.append([scenario, t, x_position, y_position, action, reward, uncertainty])

# Write to CSV
with open('../data/sample_data/emergency_avoidance_multiple.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['scenario', 'timestep', 'x_position', 'y_position', 'action', 'reward', 'uncertainty'])
    writer.writerows(data)

print("Generated emergency_avoidance_multiple.csv with 5 scenarios (505 timesteps).")
