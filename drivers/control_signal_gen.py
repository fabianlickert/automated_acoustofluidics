from ctypes import *
import time
from drivers.dwfconstants import *
import sys
import numpy as np

class ControlSignalGenNew:
    
    # initialize the connection to the Analog Discovery 2
    def __init__(self, channel=0):
        
        try:
            if sys.platform.startswith("win"):
                self.dwf = cdll.dwf
            elif sys.platform.startswith("darwin"):
                self.dwf = cdll.LoadLibrary("/Library/Frameworks/dwf.framework/dwf")
            else:
                self.dwf = cdll.LoadLibrary("libdwf.so")

            self.hdwf = c_int()
            self.channel = c_int(0)

            version = create_string_buffer(16)
            self.dwf.FDwfGetVersion(version)
            print("DWF Version: "+str(version.value))

            self.dwf.FDwfParamSet(DwfParamOnClose, c_int(0)) # 0 = run, 1 = stop, 2 = shutdown

            #open device
            print("Opening first device...")
            self.dwf.FDwfDeviceOpen(c_int(-1), byref(self.hdwf))


            if self.hdwf.value == hdwfNone.value:
                print("failed to open device")
                quit()

            self.dwf.FDwfDeviceAutoConfigureSet(self.hdwf, c_int(0))# 0 = the device will be configured only when calling FDwf###Configure
            self.dwf.FDwfAnalogOutNodeFunctionSet(self.hdwf, self.channel, AnalogOutNodeCarrier, funcSine)
            self.dwf.FDwfAnalogOutNodeOffsetSet(self.hdwf, self.channel, AnalogOutNodeCarrier, c_double(0))
            self.dwf.FDwfAnalogOutNodeEnableSet(self.hdwf, self.channel, AnalogOutNodeCarrier, c_bool(True))

        except:
            print('Failed to access Analog Discovery.')
        
    # set the trigger
    def set_trigger(self, wait_time=1, run_time=0, repeat_num=1):   
        # set the trigger source to DetectorAnalogIn
        self.dwf.FDwfAnalogOutTriggerSourceSet(self.hdwf, self.channel, trigsrcDetectorAnalogIn)
        self.dwf.FDwfAnalogOutTriggerSlopeSet(self.hdwf, self.channel, DwfTriggerSlopeRise)
        self.dwf.FDwfAnalogOutWaitSet(self.hdwf, self.channel, c_double(wait_time))
        self.dwf.FDwfAnalogOutRunSet(self.hdwf, self.channel, c_double(run_time))
        self.dwf.FDwfAnalogOutRepeatSet(self.hdwf, self.channel, c_int(repeat_num))

    # reset the trigger
    def reset_trigger(self):
        self.dwf.FDwfAnalogOutTriggerSourceSet(self.hdwf, self.channel, trigsrcNone)
  
    # set the actuation frequency
    def set_freq(self, freq=1000000):
        self.dwf.FDwfAnalogOutNodeFrequencySet(self.hdwf, self.channel, AnalogOutNodeCarrier, c_double(freq))

    # set the actuation voltage
    def set_voltage(self, voltage=1):
        self.dwf.FDwfAnalogOutNodeAmplitudeSet(self.hdwf, self.channel, AnalogOutNodeCarrier, c_double(voltage))

    # read the voltage
    def read_voltage(self, freq = 1000000, buffer_size = 1000, channel = 1):
        
        self.dwf.FDwfAnalogInReset(self.hdwf)
        self.dwf.FDwfAnalogInChannelEnableSet(self.hdwf, c_int(channel), c_int(1))
        self.dwf.FDwfAnalogInChannelOffsetSet(self.hdwf, c_int(channel), c_double(0))
        
        if (freq > 1000000):
            self.dwf.FDwfAnalogInFrequencySet(self.hdwf, c_double(100000000))
        else:
            self.dwf.FDwfAnalogInFrequencySet(self.hdwf, c_double(freq*100))        
            
        self.dwf.FDwfAnalogInTriggerSourceSet(self.hdwf, trigsrcNone)

        #print("Set range for all channels")
        self.dwf.FDwfAnalogInChannelRangeSet(self.hdwf, c_int(-1), c_double(8))

        #self.dwf.FDwfAnalogInChannelRangeSet(self.hdwf, c_int(0), c_double(1))
        #self.dwf.FDwfAnalogInChannelRangeSet(self.hdwf, c_int(1), c_double(8))

        self.dwf.FDwfAnalogInBufferSizeSet(self.hdwf, c_int(buffer_size))

        #print("Wait after first device opening the analog in offset to stabilize")
        time.sleep(2)

        #print("Starting acquisition...")
        self.dwf.FDwfAnalogInConfigure(self.hdwf, c_int(1), c_int(1))

        sts = c_int()
        while True:
            self.dwf.FDwfAnalogInStatus(self.hdwf, c_int(1), byref(sts))
            if sts.value == DwfStateDone.value :
                break
            time.sleep(0.1)
        #print("   done")

        rg = (c_double*buffer_size)()
        self.dwf.FDwfAnalogInStatusData(self.hdwf, c_int(channel), rg, len(rg)) # get channel 2 data

        #self.dwf.FDwfAnalogOutReset(self.hdwf, c_int(1))
        #self.dwf.FDwfDeviceCloseAll()

        dc = sum(rg)/len(rg)
        maxVal = np.max(rg)
        minVal = np.min(rg)
        
        amplitude = (maxVal-minVal)/2
        #print("DC: "+str(dc)+"V")
        #print("Max value: "+str(maxVal)+"V")
        #print("Min value: "+str(minVal)+"V")
        
        #print(rg[:1000])
        
        return amplitude
    
    # run for a set duration
    def run_set_time(self, duration=10):
        self.dwf.FDwfAnalogOutConfigure(self.hdwf, self.channel, c_bool(True))
        time.sleep(duration)
        self.dwf.FDwfAnalogOutConfigure(self.hdwf, self.channel, c_bool(False))

    # run for unlimited time
    def run(self):
        self.dwf.FDwfAnalogOutConfigure(self.hdwf, self.channel, c_bool(True))

    # stop the signal generation
    def stop(self):
        self.dwf.FDwfAnalogOutConfigure(self.hdwf, self.channel, c_bool(False))
        
    # close connection to the Analog Discovery 2
    def close(self):
        self.dwf.FDwfDeviceClose(self.hdwf)


        