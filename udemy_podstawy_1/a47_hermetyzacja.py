from Thermometer import  Thermometer

temp = float(input("Podaj temperature "))
unit = input("podaj jednostke \'C\'  dla Celsiusza \'K\' - Kelwina i \'F\' dla Farenhajta ")

term = Thermometer()
term.setTemperature(temp, unit)

while True:
    choose = int(input("Podaj 0 jeżeli chcesz otrzymać tempereature w jakiść jednostkach 1 jeżeli chcesz podać jakąś temperature  9 jeżeli chcesz zakączyć"))
    if choose == 9:
        break
    elif choose == 0:
        unit = input("podaj jednostke \'C\'  dla Celsiusza \'K\' - Kelwina i \'F\' dla Farenhajta ")
        print(term.getTemperature(unit))
    elif choose ==1:
        temp = float(input("Podaj temperature"))
        unit = input("podaj jednostke \'C\'  dla Celsiusza \'K\' - Kelwina i \'F\' dla Farenhajta ")
        term.setTemperature(temp, unit)
    else:
        pass



