from tkinter import W


print("hola mundo! Soy luis:)")
print("hola mundo! Soy Gustavo:)")
print("hola mundo! Soy Puello:)")
print("hola mundo! Soy Puerta:)")
#soy un comentario
"""
somos cosas creadas para no estar
zomoz xosas creadas pata bada lo puedes creer

"""
#variable

texto = "resásando python por primera vez"
nombre = "Luid Hurtavo Puello"
altura = "165cm"
year = 2022
print(texto)
#print(f "{texto} - {nombre} - {altuta} - {str (year)} ")
print(texto + " - " + nombre + " - " + altura + " - " + str (year))
#entrada
sitioweb = input("¿Cual es tu pagina web?: ")
print("el citio web del usuario es:" + sitioweb)
#condiciones
"""altura = int (input("¿cual es tu altura?"))
if altura >= 187:
    print("eres una persona alta")
else:
    print("eres una persona bajita!!")"""
 #funciones:  me permite usar el codigo varuas veces

def mostrarAltura():

        altura = int (input("¿cual es tu altura?"))

        if altura >= 187:
           print("eres una persona alta")
        else:
           print("eres una persona bajita!!")

mostrarAltura()
mostrarAltura()
mostrarAltura()
#listas
personas = ["luis", "morca", " pepe"]
print(personas [0])

for persona in personas:
    print("-" + persona)
    
    

