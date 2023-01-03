import serial
import time

class ControlPump:
    
    # initialize the serial port connection   
    def __init__(self, bdr=115200, port='COM4'):

        self.ser = serial.Serial()
        self.ser.baudrate = bdr
        self.ser.port = port
        self.ser.timeout = 5

        try:
            self.ser.open()
        except:
            print('Failed to open COM-port')

    # Move valve to position pos 1 or 2
    def run(self):

        pump_command = "run\r".encode('UTF-8') 
        self.ser.write(pump_command)

    # Stop connection
    def stop(self):

        pump_command = "stop\r".encode('UTF-8') 
        self.ser.write(pump_command)
        
    # set current rate
    def set_rate(self, rate=50):
        
        pump_command = f"irate {rate} uL/min\r".encode('UTF-8') 
        self.ser.write(pump_command)
        
     # Get current rate
    def get_rate(self):
        
        self.ser.reset_input_buffer()
        
        pump_command = "crate\r".encode('UTF-8') 
        self.ser.write(pump_command)
        
        rate = self.ser.read_until(b'\r')
        return rate
    
    def close(self):
        self.ser.close()

        