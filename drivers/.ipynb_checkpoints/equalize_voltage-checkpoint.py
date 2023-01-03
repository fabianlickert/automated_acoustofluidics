def equalize_voltage(signal, init_voltage = 0.1, f = 10000):

    signal.set_voltage(init_voltage)
    signal.set_freq(f)

    signal.run()
    voltage_meas1 = signal.read_voltage(f, 4000, 1)
    #print(voltage_meas1)
    signal.stop()

    voltage_set1 = 2*init_voltage/voltage_meas1
    #print(voltage_set1)
    signal.set_voltage(voltage_set1)
    signal.set_freq(f)

    signal.run()
    voltage_meas2 = signal.read_voltage(f, 4000, 1)
    #print(voltage_meas2)
    signal.stop()

    voltage_set2 = 2*voltage_set1/voltage_meas2
    #print(voltage_set2)
    signal.set_voltage(voltage_set2)
    signal.set_freq(f)

    signal.run()
    final_voltage = signal.read_voltage(f, 4000, 1)
    #print(final_voltage)
    signal.stop()
    
    return final_voltage