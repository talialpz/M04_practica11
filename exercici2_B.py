#El programa mira si el num és parell o no
    #Demanem el num
print("Escriu un numero: ")
num = int(input())
    #Fem la operació per saber si es parell
num1 = num % 2
    #Si num1 == 2 es parell
if (num1 == 0):
    txt = "El num {nums} és parell!"
    print(txt.format(nums = num))
    #Si no es imparell
else:
    txt = "El num {nums} és imparell!"
    print(txt.format(nums = num))