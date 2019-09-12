# PRZYPISZ 12 osób do 4 grup - w każdej grupie wylosuj jednego lidera
from random import sample, choice

osoby = set(["AN","TSz", "MP","ZJ","PM","AP","FŚ","MT","AR","IS","MS","MK"])
group_dict = {}
i = 1
while len(osoby) > 0:
    grupa = sample(osoby, 3)
    for osoba in grupa:
        group_dict[osoba] = str(i)
        osoby.discard(osoba)
    group_dict[choice(grupa)] = str(i)+"L"
    i += 1
print(group_dict)