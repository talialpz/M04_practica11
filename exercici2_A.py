#Funcio que demana que insereix un nombre que es trobi a la llista, si no, tornara un missatge dient que el nombre es incorrecte
def noms():

    MyList = ['Talia', 'Maria', 'Roger', 'Ramon', 'Aleksandra']

    print("Insereix un nom que es trobi a la llista {llista}".format(llista = MyList))
    #Es demana el nombre
    nombre = input()

    #Es fa la comparacio del nombre introduït amb el nom de la llista i en cas de que sigui correcta també imprimeix la posició
    if (nombre == 'Talia'):
            print("Molt bé! Aquest nom es troba a la posició {posicio}".format(posicio = MyList.index('Talia')))
    elif (nombre == 'Maria'):
            print("Molt bé! Aquest nom es troba a la posicio {posicio}".format(posicio = MyList.index('Maria')))
    elif (nombre == 'Roger'):
            print("Molt bé! Aquest nom es troba a la posicio {posicio}".format(posicio = MyList.index('Roger')))
    elif (nombre == 'Ramon'):
            print("Molt bé! Aquest nom es troba a la posicio {posicio}".format(posicio = MyList.index('Ramon')))
    elif (nombre == 'Aleksandra'):
            print("Molt bé! Aquest nom es troba a la posicio {posicio}".format(posicio = MyList.index('Aleksandra')))
            
    #Si no es troba a la llista, imprimeix el missatge d'error
    else:
        print("Aquest nombre no es troba a la llista, fixa't bé!")

    
