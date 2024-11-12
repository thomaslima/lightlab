from . import VISAInstrumentDriver

class HP_83712B_CWG(VISAInstrumentDriver):
    '''
        HP 83712B Synthesized Continuous Wave Generator

        `Manual <https://www.keysight.com/us/en/product/83712B/synthesized-cw-generator-10-mhz-to-20-ghz.html>`_
    '''

    def __init__(self, name='Continuous Wave Generator', address=None, **kwargs):
        VISAInstrumentDriver.__init__(self, name=name, address=address, **kwargs)

    def reset(self):
        self.write('*RST')

    def enable(self, newState=None):
        trueWords = [True, 1, '1', 'ON']
        if newState is not None:
            if newState:
                self.write(f"OUTP ON")
            else:
                self.write(f"OUTP OFF")
        return self.query("OUTP?") in trueWords

    def frequency(self, newFreq=None):
        if newFreq is not None:
            self.write(f"FREQ {newFreq}")
        return(float(self.query("FREQ?")))

    # Units of dBm
    def power(self, newPower=None):
        if newPower is not None:
            self.write(f"POW {newPower}")
        return(float(self.query("POW?")))

    
    
