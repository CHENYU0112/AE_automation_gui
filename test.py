from measure_eff_Tek import eff
from mock_instruments import MockInstrumentManager

def test_efficiency():
    settings = {
        'input_shunt_max_voltage': 0.1,
        'input_shunt_max_current': 1.0,
        'output_shunt_max_voltage': 0.1,
        'output_shunt_max_current': 1.0,
        'input_v_ch': 1,
        'input_i_ch': 2,
        'output_v_ch': 3,
        'output_i_ch': 4,
        'vcc_ch': 5,
        'ldo_ch': 6,
        'Max_input_voltage': 20,
        'Max_input_current': 2,
        'Max_load_current': 1,
        'Input_V': [5, 10, 15],
        'Input_I': 1,
        'Low_load_start': 0.1,
        'Low_load_step': 0.1,
        'Low_load_stop': 0.5,
        'High_load_stop': 1,
        'High_load_step': 0.1,
        'low_load_timing': 1,
        'high_load_timing': 1,
        'FRE': 1
    }

    instrument_manager = MockInstrumentManager()

    def progress_callback(value):
        print(f"Progress: {value}%")

    def result_callback(message):
        print(f"Result: {message}")

    def graph_callback(buffer):
        print("Graph generated")

    try:
        excel_buffer = eff(settings, instrument_manager, progress_callback, result_callback, graph_callback)
        print("Test completed successfully")
    except Exception as e:
        print(f"Test failed: {str(e)}")

if __name__ == "__main__":
    test_efficiency()