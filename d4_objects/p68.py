import datetime
from datetime import datetime
from random import sample
class Lotto:
    def __init__(self):
        self.result = []
    def starting(self):
        self.result = sample(range(1,50), 6)
        print(self.__str__())
    def sorting(self):
        # sortowanie listy
        self.result = sorted(self.result, reverse = False)
        print(self.__str__())
    def __str__(self):
        return "%s data losowania: %s" % (self.result, datetime.today().strftime("%d.%m.%Yr"))


lotto1 = Lotto()
lotto1.starting()
lotto1.sorting()