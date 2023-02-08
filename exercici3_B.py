print("Digues la teva edat: ")
edat = int(input())
print("Digues els teus ingressos mensuals: ")
ingressos = int(input())
if (edat >= 18 and ingressos >= 1200):
    txt = "Com la teva edat es {edats} i els teus ingressos són {ing} has de fer la declaració a hisenda!"
    print(txt.format(edats = edat, ing = ingressos))
else:
    print("Encara no pots fer la declaració")