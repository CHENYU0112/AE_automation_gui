import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Load the data from the CSV files
data_131043 = pd.read_csv('efficiency_test_results_20240703_131043.csv')
data_150508 = pd.read_csv('efficiency_test_results_20240703_150508.csv')
data_tda48820 = pd.read_csv('TDA48820_TRIMMED_EFF_1.csv')

# Extract the relevant data
input_voltages = [5, 9, 12, 16]

# Plot 1: Load Current vs Efficiency
fig, ax = plt.subplots(figsize=(12, 6))
colors = ['b', 'g', 'r', 'c']
for i, v in enumerate(input_voltages):
    mask_131043 = (data_131043['input_voltage_setpoint'] == v) & (data_131043['i_output_current'] > 0)
    mask_150508 = (data_150508['input_voltage_setpoint'] == v) & (data_150508['i_output_current'] > 0)
    mask_tda48820 = (data_tda48820['input_voltage_setpoint'] == v) & (data_tda48820['i_output_current'] > 0)
    ax.plot(data_131043['i_output_current'][mask_131043], data_131043['efficiency'][mask_131043], color=colors[i], linestyle='-', label=f"Vin = {v}V (L1)")
    ax.plot(data_150508['i_output_current'][mask_150508], data_150508['efficiency'][mask_150508], color=colors[i], linestyle='--', label=f"Vin = {v}V (L2)")
    ax.plot(data_tda48820['i_output_current'][mask_tda48820], data_tda48820['efficiency'][mask_tda48820], color=colors[i], linestyle=':', label=f"Vin = {v}V (original)")
ax.set_xlabel('Load Current (A)')
ax.set_ylabel('Efficiency (%)')
ax.set_title('Load Current vs Efficiency')
ax.legend()
ax.grid()

# Plot 2: Load Current vs Switching Frequency
fig, ax = plt.subplots(figsize=(12, 6))
for i, v in enumerate(input_voltages):
    mask_131043 = (data_131043['input_voltage_setpoint'] == v) & (data_131043['i_output_current'] > 0)
    mask_150508 = (data_150508['input_voltage_setpoint'] == v) & (data_150508['i_output_current'] > 0)
    mask_tda48820 = (data_tda48820['input_voltage_setpoint'] == v) & (data_tda48820['i_output_current'] > 0)
    ax.plot(data_131043['i_output_current'][mask_131043], data_131043['switching_frequency'][mask_131043], color=colors[i], linestyle='-', label=f"Vin = {v}V (L1)")
    ax.plot(data_150508['i_output_current'][mask_150508], data_150508['switching_frequency'][mask_150508], color=colors[i], linestyle='--', label=f"Vin = {v}V (L2)")
    ax.plot(data_tda48820['i_output_current'][mask_tda48820], data_tda48820['switching_frequency'][mask_tda48820], color=colors[i], linestyle=':', label=f"Vin = {v}V (original)")
ax.set_xlabel('Load Current (A)')
ax.set_ylabel('Switching Frequency (Hz)')
ax.set_title('Load Current vs Switching Frequency')
ax.legend()
ax.grid()

# Plot 3: Load Current vs Output Voltage
fig, ax = plt.subplots(figsize=(12, 6))
for i, v in enumerate(input_voltages):
    mask_131043 = (data_131043['input_voltage_setpoint'] == v) & (data_131043['i_output_current'] > 0)
    mask_150508 = (data_150508['input_voltage_setpoint'] == v) & (data_150508['i_output_current'] > 0)
    mask_tda48820 = (data_tda48820['input_voltage_setpoint'] == v) & (data_tda48820['i_output_current'] > 0)
    ax.plot(data_131043['i_output_current'][mask_131043], data_131043['v_output_voltage'][mask_131043], color=colors[i], linestyle='-', label=f"Vin = {v}V (L1)")
    ax.plot(data_150508['i_output_current'][mask_150508], data_150508['v_output_voltage'][mask_150508], color=colors[i], linestyle='--', label=f"Vin = {v}V (L2)")
    ax.plot(data_tda48820['i_output_current'][mask_tda48820], data_tda48820['v_output_voltage'][mask_tda48820], color=colors[i], linestyle=':', label=f"Vin = {v}V (original)")
ax.set_xlabel('Load Current (A)')
ax.set_ylabel('Output Voltage (V)')
ax.set_title('Load Current vs Output Voltage')
ax.legend()
ax.grid()

plt.show()