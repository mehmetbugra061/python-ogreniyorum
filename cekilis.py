import random

def cekilis(isimler):
    index = 0
    boy = len(isimler)
    rastgele = random.randint(0, boy -1)
    return isimler[rastgele]


isimlerVG = ["Fatih", "Serkan", "Taha", "Mehmet"]

print(cekilis(isimlerVG))

