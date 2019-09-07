class Thermometer:
    def __init__(self, temp=0):
        self.celsjusz =  temp

    def setTemperature(self, temp, unit):
        if unit == 'C':
            self.celsjusz = temp
        elif unit == 'K':
            self.celsjusz = temp + 273.15
        else:
            self.celsjusz = (5/9) * (temp - 32)

    def getTemperature(self, unit='C'):
            if unit == 'C':
                return self.celsjusz
            elif unit == 'K':
                return  self.celsjusz - 273.15
            else:
                return  (self.celsjusz * 9/5) + 32


