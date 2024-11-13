import time
from . import VISAInstrumentDriver

class Boonton_4240_PM(VISAInstrumentDriver):
    """ Boonton 4240 (4242) Two-Channel RF Power Meter

        `Manual: <https://boonton.com/portals/0/products/rf%20power%20meters/4240/4240_instructionmanual.pdf>`__
    """

    def __init__(self, name="Booton 4240 PM", address=None, **kwargs):
        VISAInstrumentDriver.__init__(self, name=name, address=address, **kwargs)

    def reset(self):
        return self.write("*RST")
    
    def getID(self):
       return self.query("*IDN?")

    def getFilterTime(self, channel=1):
        return float(self.query(f"SENS{channel}:FILT:TIM?"))

    def setFilterTime(self, time=0.05, channel=1):
        self.write(f"SENS{channel}:FILT:TIM {time}")

    # Note: this function fails for filter times beyond 1. More investigation required
    def read(self, channel=1):
        for i in range(3):
            try:
                response = self.query(f"READ{channel}:CW:POW?")
                break
            except:
                pass

        splitted = response.split(",")
        if len(splitted) == 2:
            channel = int(splitted[0])
            power = float(splitted[1])
            return power
        return -99.99
        
        