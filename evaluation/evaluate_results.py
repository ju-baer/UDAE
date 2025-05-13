import pandas as pd
import matplotlib.pyplot as plt

def evaluate_success_rate(log_file, scenario_name):
    df = pd.read_csv(log_file)
    success = (df['reward'] >= 0).mean() * 100  # Simplified: success if reward >= 0
    print(f"Success rate for {scenario_name}: {success:.2f}%")
    return success

def plot_success_rates():
    scenarios = [
        ('../data/sample_data/urban_navigation_log.csv', 'Urban Navigation'),
        ('../data/sample_data/emergency_avoidance_log.csv', 'Emergency Avoidance')
    ]
    success_rates = []
    labels = []

    for log_file, scenario in scenarios:
        success = evaluate_success_rate(log_file, scenario)
        success_rates.append(success)
        labels.append(scenario)

    plt.figure(figsize=(6, 4))
    plt.bar(labels, success_rates, color=['blue', 'orange'])
    plt.ylabel('Success Rate (%)')
    plt.title('Success Rates Across Scenarios')
    plt.ylim(0, 100)
    plt.savefig('success_rates.pdf', format='pdf', dpi=300)
    plt.show()

if __name__ == '__main__':
    plot_success_rates()
