import pandas as pd
import matplotlib.pyplot as plt
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

def evaluate_success_rate(log_file, scenario_name):
    try:
        df = pd.read_csv(log_file)
        if 'reward' not in df.columns:
            raise ValueError(f"'reward' column missing in {log_file}")
        success = (df['reward'] >= 0.5).mean() * 100
        logger.info(f"Success rate for {scenario_name}: {success:.2f}%")
        return success
    except Exception as e:
        logger.error(f"Error evaluating {log_file}: {e}")
        raise

def plot_success_rates():
    scenarios = [
        ('../data/sample_data/urban_navigation_log.csv', 'Urban Navigation (UDAE)'),
        ('../data/sample_data/emergency_avoidance_log.csv', 'Emergency Avoidance (UDAE)'),
        ('../data/sample_data/epsilon_greedy_log.csv', 'Urban Navigation (Epsilon-Greedy)')
    ]
    success_rates = []
    labels = []

    for log_file, scenario in scenarios:
        success = evaluate_success_rate(log_file, scenario)
        success_rates.append(success)
        labels.append(scenario)

    plt.figure(figsize=(8, 4))
    plt.bar(labels, success_rates, color=['blue', 'orange', 'green'])
    plt.ylabel('Success Rate (%)')
    plt.title('Success Rates Across Scenarios')
    plt.ylim(0, 100)
    plt.xticks(rotation=15)
    plt.savefig('success_rates.pdf', format='pdf', dpi=300)
    plt.show()

if __name__ == '__main__':
    plot_success_rates()
