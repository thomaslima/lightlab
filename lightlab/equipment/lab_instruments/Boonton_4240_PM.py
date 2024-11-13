import time
from . import VISAInstrumentDriver

# TODO: Need to ensure the wait time matches the filter time properly, and implement waiting here

class Boonton_4240_PM(VISAInstrumentDriver):

    def __init__(self, name="Booton 4240 PM", address=None, **kwargs):
        VISAInstrumentDriver.__init__(self, name=name, address=address, **kwargs)

    def reset(self):
        return self.write("*RST")
    
    def get_id(self):
       return self.query("*IDN?")

    def get_filter_time(self, channel=1):
        return float(self.query(f"SENS{channel}:FILT:TIM?"))

    def set_filter_time(self, time=0.05, channel=1):
        self.time
        self.write(f"SENS{channel}:FILT:TIM {time}")

    def read(self, channel=1, wait_time=5):
        for i in range(10):
            try:
                response = self.query(f"READ{channel}:CW:POW?", wait_time=wait_time) # Averaging time
                break
            except:
                pass

        splitted = response.split(",")
        channel = int(splitted[0])
        power = float(splitted[1])
        return power
        
        