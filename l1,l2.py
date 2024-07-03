import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Load the data from the CSV files
data_131043 = pd.read_csv('efficiency_test_results_20240703_131043.csv')
data_150508 = pd.read_csv('efficiency_test_results_20240703_150508.csv')

# Extract the relevant data
input_voltages = [5, 9, 12, 16]

# Plot 1: Load Current vs Efficiency
plt.figure(figsize=(12, 6))
for v in input_voltages:
    mask_131043 = (data_131043['input_voltage_setpoint'] == v) & (data_131043['i_output_current'] > 0)
    mask_150508 = (data_150508['input_voltage_setpoint'] == v) & (data_150508['i_output_current'] > 0)
    plt.plot(data_131043['i_output_current'][mask_131043], data_131043['efficiency'][mask_131043], label=f"Vin = {v}V (L1)")
    plt.plot(data_150508['i_output_current'][mask_150508], data_150508['efficiency'][mask_150508], label=f"Vin = {v}V (L2)")
plt.xlabel('Load Current (A)')
plt.ylabel('Efficiency (%)')
plt.title('Load Current vs Efficiency')
plt.legend()
plt.grid()
plt.savefig('load_current_vs_efficiency.png')