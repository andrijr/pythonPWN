# P60
# Napisz program do wyliczania odległości między dwoma punktami na płaszczyźnie.

def distanceMeasure(x_start, y_start, x_stop, y_stop):
    return sqrt(pow(x_stop - x_start, 2) + pow(y_stop - y_start, 2))

print(distanceMeasure(1,1,2,2))
