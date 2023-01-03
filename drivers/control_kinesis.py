import clr
clr.AddReference("System")

import sys
import time
import numpy as np
import matplotlib.pyplot as plt
import random  # only used for dummy data

from System import String
from System import Decimal
from System.Collections import *

# constants
sys.path.append(r"C:\Program Files\Thorlabs\Kinesis")

clr.AddReference("Thorlabs.MotionControl.DeviceManagerCLI")
clr.AddReference("Thorlabs.MotionControl.GenericMotorCLI")
clr.AddReference("Thorlabs.MotionControl.IntegratedStepperMotorsCLI")
clr.AddReference("ThorLabs.MotionControl.KCube.DCServoCLI")
clr.AddReference("Thorlabs.MotionControl.Controls")

import Thorlabs.MotionControl.Controls
from Thorlabs.MotionControl.KCube.DCServoCLI import KCubeDCServo
from Thorlabs.MotionControl.DeviceManagerCLI import *
from Thorlabs.MotionControl.GenericMotorCLI import *
from Thorlabs.MotionControl.IntegratedStepperMotorsCLI import *

POLLING_INTERVAL = 250
ENABLE_SLEEP_TIME = 0.1
INIT_TIMEOUT = 5000

class KCube():
    
    def __init__(self, sn):
        DeviceManagerCLI.BuildDeviceList()
        device = KCubeDCServo.CreateKCubeDCServo(sn)
        device.Connect(sn)
        device.WaitForSettingsInitialized(INIT_TIMEOUT)
        device.StartPolling(POLLING_INTERVAL)
        device.EnableDevice()
        config = device.LoadMotorConfiguration(sn)
        #print(f'position {Decimal.ToDouble(device.DevicePosition)}')
        self.device = device

    def kill(self):
        self.device.StopImmediate()
        self.device.Disconnect()
        del self

    def home(self):
        self.device.Home(0)
        time.sleep(1)
        
        while(not self.is_homed()):
            time.sleep(1)

    def is_homed(self):
        stat = self.device.Status.IsHomed
        return stat
    
    def is_moving(self):
        stat = self.device.Status.IsMoving
        return stat    
    
    def is_init(self):
        stat = self.device.IsSettingsInitialized
        return stat
    
    def get_status(self):
        status = self.device.Status
        return status
        
    def move_to(self, position): 
        try:
            self.device.MoveTo(Decimal(position),0)
            time.sleep(1)

            while(self.is_moving()):
                time.sleep(1)

            time.sleep(1)
        except:
            print("Cannot move to specified location.")
        
    def move_relative(self, increment):
        new_pos = self.get_position() + increment        
        self.move_to(new_pos)
    
    def get_position(self):
        return Decimal.ToDouble(self.device.DevicePosition)
        
    def disconnect(self):
        self.device.Disconnect()
        
    def stop_immediate(self):
        self.device.StopImmediate()
        
    def move_continuous(self, orientation = 'cw'):
        if orientation == 'cw':
            self.device.MoveContinuous(1)
        elif orientation == 'ccw':
            self.device.MoveContinuous(2)