import numpy as np
import time
from config import *
import pyvisa
from pverifyDrivers import _scope
from pverifyDrivers import powsup
from pverifyDrivers import daq
from pverifyDrivers import load
def transient(selected_ic, power_supply_settings, scope_settings, scope_persistence, scope_us_div, load_settings, protection, instrument_manager):
    print(f"Debug: transient function started for {selected_ic}")
    results = {}
    print("Transient test started")
    try:
        # Get instruments from the instrument manager
        power_supply_address = instrument_manager.instruments.get('supply', '')
        electronic_load_address = instrument_manager.instruments.get('load', '')
        scope_address = instrument_manager.instruments.get('o_scope', '')
        
        electronic_load = load.Chroma63600(electronic_load_address)
        power_supply = powsup.N6705C(power_supply_address)
        power_supply_channel = power_supply.GetChannel(power_supply_settings['vin_channel'])
        sc = _scope.TEK_MSO5XB(scope_address, Simulate=False, Reset=True)
        
        # Set up power supply
        power_supply_channel.Configure_VoltageLevel(Level=power_supply_settings['vin'], CurrentLimit=power_supply_settings['iin'])
        power_supply_channel.Enable(True)

        # Find channel numbers for SW, Vout, and Iout
        sw_ch_num = next(ch for ch, signal in scope_settings.items() if signal == 'SW')
        vout_ch_num = next(ch for ch, signal in scope_settings.items() if signal == 'output V')
        iout_ch_num = next(ch for ch, signal in scope_settings.items() if signal == 'output I')

        # Setup oscilloscope channels
        sw_ch = sc.GetChannel(int(sw_ch_num[-1]))
        vout_ch = sc.GetChannel(int(vout_ch_num[-1]))
        iout_ch = sc.GetChannel(int(iout_ch_num[-1]))

        # Enable channels
        sw_ch.Enable(True)
        vout_ch.Enable(True)
        iout_ch.Enable(True)

        # Set up channels with provided settings and adjust vertical positions
        sw_ch.ProbeSetup(Coupling='DC', Bandwidth='20E+06', Vrange=5, Impedance=50, Position=3.5)  # 0.5V/div, 50 ohm, 20MHz, top position
        iout_ch.ProbeSetup(Coupling='DC', Bandwidth='120E+06', Vrange=50, Impedance=1e+6, Position=0)  # 5A/div, 1Mohm, 120MHz, middle position
        vout_ch.ProbeSetup(Coupling='AC', Bandwidth='20E+06', Vrange=0.2, Impedance=1e+6, Position=-3.5)  # 20mV/div, 1Mohm, 20MHz, bottom position

        # Set channel labels
        sc.set_channel_label(ChannelIndex=int(sw_ch_num[-1]), Label="SW", Xpos="5", Ypos="80")
        sc.set_channel_label(ChannelIndex=int(iout_ch_num[-1]), Label="Iout", Xpos="5", Ypos="50")
        sc.set_channel_label(ChannelIndex=int(vout_ch_num[-1]), Label="Vout", Xpos="5", Ypos="20")

        # Set horizontal scale
        print(f"Debug: About to set horizontal scale to {scope_us_div}us")
        sc._write(f'HOR:SCALE {scope_us_div}e-6')  
        
        # Set trigger on the current channel for load transition
        trigger_level = (load_settings['i_high'] + load_settings['i_low']) / 2
        sc.Trigger_Edge(Level=trigger_level, Slope='RISE', Coupling='DC', ChannelIndex=int(iout_ch_num[-1]))

        sc.set_acquisition_mode('HIRes')
        sc.set_record_length(10000000)  # 10M points for higher resolution

        # Set measurements
        sc.set_measurement(MeasureIndex=1, MeasureType='MAXIMUM', State='ON', Source=int(vout_ch_num[-1]))  # Vout max
        sc.set_measurement(MeasureIndex=2, MeasureType='MINIMUM', State='ON', Source=int(vout_ch_num[-1]))  # Vout min
        sc.set_measurement(MeasureIndex=3, MeasureType='RISETIME', State='ON', Source=int(iout_ch_num[-1]))  # Iout rise time
        sc.set_measurement(MeasureIndex=4, MeasureType='FALLTIME', State='ON', Source=int(iout_ch_num[-1]))  # Iout fall time
        
        # Enable display overlay
        sc.display_overlay()
        
        # Setup electronic load for dynamic mode
        electronic_load.set_mode('CCDH')  # Set to dynamic high mode
        electronic_load._write(f'CURR:DYN:L1 {load_settings["i_low"]}')  # Set low current
        electronic_load._write(f'CURR:DYN:L2 {load_settings["i_high"]}')  # Set high current
        electronic_load._write(f'CURR:DYN:RISE MAX')  # Set rising slew rate
        electronic_load._write(f'CURR:DYN:FALL MAX')  # Set falling slew rate
        electronic_load._write(f'CURR:DYN:T1 {load_settings["low_time"]}us')  # Set T1 duration
        electronic_load._write(f'CURR:DYN:T2 {load_settings["high_time"]}us')  # Set T2 duration
        electronic_load._write('CURR:DYN:REP 0')  # Set to continuous repeat

        # Start the load cycling
        electronic_load.output('ON')

        # Allow some time for the waveform to stabilize
        time.sleep(2)

        # Capture waveform
        sc.run()
        time.sleep((load_settings['low_time'] + load_settings['high_time']) / 1e6 * 5)  # Capture multiple cycles

        # Save full waveform image
        sc.set_screen_text(text=f"I low: {load_settings['i_low']}A, I high: {load_settings['i_high']}A", text_no=1, xpos="10", ypos="20")
        sc.set_screen_text(text=f"Low time: {load_settings['low_time']}us, High time: {load_settings['high_time']}us", text_no=2, xpos="10", ypos="25")
        sc.saveimage("transient_full_cycle.png")
        
        # Analyze results
        vout_max = float(sc.get_max_measurement(Index=1))
        vout_min = float(sc.get_min_measurement(Index=2))
        rise_time = float(sc.get_val_measurement(Index=3))
        fall_time = float(sc.get_val_measurement(Index=4))

        # Convert overshoot and undershoot to mV
        overshoot_mv = vout_max * 1000
        undershoot_mv = vout_min * 1000

        # Convert rise and fall times to µs
        rise_time_us = rise_time * 1e6
        fall_time_us = fall_time * 1e6

        results = {
            'overshoot': f"{overshoot_mv:.2f} mV",
            'undershoot': f"{undershoot_mv:.2f} mV",
            'rise_time': f"{rise_time_us:.2f} µs",
            'fall_time': f"{fall_time_us:.2f} µs"
        }


        print("Transient test completed")
  

    except Exception as e:
        print(f"An error occurred: {str(e)}")
        import traceback
        print(traceback.format_exc())
        set_stop_flag()
    finally:
        if 'electronic_load' in locals():
            electronic_load.output('OFF')
        if 'power_supply_channel' in locals():
            power_supply_channel.Enable(False)
        sc.set_screen_text(text="", text_no=1)  # Clear text annotations
        sc.set_screen_text(text="", text_no=2)
        print("Test ended, instruments turned off")

    return results