# P 55

# Woda zamarza przy 32 stopniach Fahrenheita, a wrze przy 212 stopniach Fahrenheita.
# Napisz program, który wyświetli tabelę przeliczeń stopni Celsjusza na stopnie Fahrenheita
# w zakresie od –20 do +40 stopni Celsjusza (co 5 stopni). Pamiętaj o wyświetlaniu znaku plus/minus przy temperaturze.

print("   C |  F")
for temp_c in reversed(range(-20, 41, 5)):
    print("%+3iC | %+3iF" % (temp_c, round((9 / 5) * temp_c + 32)))

print()

c_to_f = {}

for temp_c in reversed(range(-20, 45, 1)):
    c_to_f[temp_c] = (9/5) * temp_c + 32
    if(temp_c != 0):
        print("%+4iC | %5.1fF" % (temp_c, c_to_f[temp_c]))
    else:
        print("%4iC | %5.1fF" % (temp_c, c_to_f[temp_c]))

print(c_to_f)

