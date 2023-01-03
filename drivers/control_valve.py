import serial
import time

class ControlValve:
    
    # initialize the serial port connection   
    def __init__(self, bdr=19200, port='COM3'):

        self.ser = serial.Serial()
        self.ser.baudrate = bdr
        self.ser.port = port
        self.ser.timeout = 5

        try:
            self.ser.open()
        except:
            print('Failed to open COM-port')

    # Move valve to position pos 1 or 2
    def set_pos(self, pos=1):

        valve_command = f"P0{pos}\r".encode('UTF-8') 
        self.ser.write(valve_command)
        time.sleep(1)

    # Get position of valve
    def get_pos(self):

        self.ser.reset_input_buffer()
        self.ser.write(b'S\r')
        valveStatus = self.ser.read_until(b'\r')

        try:
            valveNo = int(valveStatus.decode("utf-8"))
            #print(valveNo)

        except:
            print('Could not fetch status.')
            valveNo = 0

        return valveNo
    
    def close(self):
        self.ser.close()

        