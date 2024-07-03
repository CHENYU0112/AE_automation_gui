import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Load the data from the CSV file
data = pd.read_csv('efficiency_test_results_20240703_150508.csv')

# Extract the relevant data
input_voltages = [5, 9, 12, 16]
load_currents = data['i_output_current']
efficiencies = data['efficiency']
switch_frequencies = data['switching_frequency']
output_voltages = data['v_output_voltage']

# Plot 1: Load current vs Efficiency
plt.figure(figsize=(12, 6))
for v in input_voltages:
    mask = (data['input_voltage_setpoint'] == v) & (data['i_output_current'] > 0)
    plt.plot(load_currents[mask], efficiencies[mask], label=f"Vin = {v}V")
plt.xlabel('Load Current (A)')
plt.ylabel('Efficiency (%)')
plt.title('Load Current vs Efficiency')
plt.legend()
plt.grid()
plt.savefig('load_current_vs_efficiency.png')

# Plot 2: Load current vs Switching Frequency
plt.figure(figsize=(12, 6))
for v in input_voltages:
    mask = (data['input_voltage_setpoint'] == v) & (data['i_output_current'] > 0)
    plt.plot(load_currents[mask], switch_frequencies[mask], label=f"Vin = {v}V")
plt.xlabel('Load Current (A)')
plt.ylabel('Switching Frequency (Hz)')
plt.title('Load Current vs Switching Frequency')
plt.legend()
plt.grid()
plt.savefig('load_current_vs_switch_frequency.png')

# Plot 3: Load current vs Output Voltage
plt.figure(figsize=(12, 6))
for v in input_voltages:
    mask = (data['input_voltage_setpoint'] == v) & (data['i_output_current'] > 0)
    plt.plot(load_currents[mask], output_voltages[mask], label=f"Vin = {v}V")
plt.xlabel('Load Current (A)')
plt.ylabel('Output Voltage (V)')
plt.title('Load Current vs Output Voltage')
plt.legend()
plt.grid()
plt.savefig('load_current_vs_output_voltage.png')