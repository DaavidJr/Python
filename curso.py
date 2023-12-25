#Funcion------------------------------------------------------------------------
def mensaje():
    print("Hola David")
    print("Hola Fuentes")
    print("Como estamos")
mensaje()  

def suma():
    num1=5
    num=2
    print(num1+num)
suma() 

# Funcion con return------------------------------------------------------------
def suma(num1,num2):
    resultado=num1+num2
    return resultado
print(suma(2,6))


def suma(nom1,nom2):
    resultado=nom1*nom2
    return resultado
print (suma(2,6))


def resta(num1,num2):
    resultado=num1-num2
    return resultado
print (resta(3,5))

#Listas-------------------------------------------------------------------------------

miLista=["David","Fuentes","Oguea","Alejandro"]
print (miLista[3])

miLista=["David","Fuentes","Oguea","Alejandro"]
print (miLista[1:3])

miLista=["David","Fuentes","Oguea","Alejandro"]
miLista.insert(4,"Marcela")
print (miLista[:])






