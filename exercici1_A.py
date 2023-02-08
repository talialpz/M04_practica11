#Es crea una funció que demana a l'usuari dos numeros i després els compara, imprimint quin és el més petit, més gran o si son iguals.
def mesGran ():
    print("Inserti dos numeros")
    #Es demanan els numeros per consola
    primerNumero = input()
    segonNumero = input()

    #Es compara si el primer numero es més gran i en cas que si s'imprimeix el missatge corresponent
    if(primerNumero > segonNumero):
        txt = "El número {numPrimer} és més gran que el {numSegon}"
        print(txt.format(numPrimer = primerNumero, numSegon = segonNumero))

    #En cas de que l'anterior condició no es compleixi, passa a aquesta i compara si es més petita, en cas que si, s'imprimeix el missatge
    elif(segonNumero > primerNumero):
        txt = "El número {numSegon} és més gran que el {numPrimer}"
        print(txt.format(numSegon = segonNumero, numPrimer = primerNumero))

    #Si no es més gran ni més petita, sera igual i s'imprimeix el missatge corresponent
    else:
        txt = "El número {numPrimer} i el número {numSegon} son iguals"
        print(txt.format(numPrimer = primerNumero, numSegon = segonNumero))
        

