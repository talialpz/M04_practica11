import random
#Demana a l'usuari que introdueixi un numero i el compara amb un numero random processat, fins que no l'adivini va donant pistes
#de si el numero introduït és més gran o més petit que el numero a adivinar

def numAleatori():
    print("Inserti un numero del 0 al 100")
    numeroInsertat = int(input())

    numeroAleatori = random.randrange(0,100,1)
    
    while numeroInsertat != numeroAleatori:

        if (numeroInsertat > numeroAleatori):
            print("El número secret és més petit que el {numInsertat}".format(numInsertat = numeroInsertat))
            numeroInsertat = int(input())
        
        elif(numeroInsertat < numeroAleatori):
            print("El número secret és més gran que el {numInsertat}".format(numInsertat = numeroInsertat))
            numeroInsertat = int(input())

    if (numeroInsertat == numeroAleatori):
        print("Molt bé! Has endevinat el número")


    

