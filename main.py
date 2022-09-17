import random
import time
BLUE='\033[34m'
RESET='\033[39m'
YELLOW='\033[33m'
CYAN='\033[36m'
GREEN='\033[32m'
MAGENTA='\033[35m'
RED='\033[31m'
print("Empezaremos en 5 segundos...")
time.sleep(2)
print("5")
time.sleep(1)
print("4")
time.sleep(1)
print("3")
time.sleep(1)
print("2")
time.sleep(1)
print("1")
time.sleep(1)
iniciartrivia=True
intentos=0

while iniciartrivia == True: #  Mientras iniciar_trivia sea True, repite:
  intentos += 1
  
  print("\nIntento número: ", intentos)
  input("Presiona Enter para continuar")
 
        
  print(GREEN+"\nBienvenido a mi trivia sobre computación.")
  print("Pondremos a prueba tus conocimientos."+RESET)
  time.sleep(2)
  nombre = input(YELLOW+"\n¿Cuál es tu Nombre?: "+RESET)
  time.sleep(1)
  apellido = input(YELLOW+"¿Cuál es tu Apellido?: "+RESET)
      
  puntajeinicial=random.randint(0,10)
      
      #Instrucciones de cómo jugar
  time.sleep(2)
  print("\n Hola,",nombre,"",apellido,".Responde a las siguientes preguntas escribiendo la letra  \n de la alternativa correcta y presionando 'Enter' para enviar la respuesta:\n" )
  time.sleep(7)
  print(YELLOW+"- ",nombre," tienes ",puntajeinicial," puntos iniciales, buena suerte."+RESET)
  time.sleep(3)
  print(MAGENTA+"\n *******************************************************************"+RESET)
  Respuesta_Correcta =0
  Respuesta_Incorrecta =0
  puntajexpregunta=0
  puntajexpreguntamala=-5
  mensajeoculto=10
  contaroculto=0
  restarpuntosaleatorio1=random.randint(-10,0)
  restarpuntosaleatorio2=random.randint(-10,0)
  restarpuntosaleatorio3=random.randint(-10,0)
  sumarpuntosaleatorio=random.randint(0,10)
  sumarpuntosaleatorio2=random.randint(0,10)
  sumarpuntosaleatorio3=random.randint(0,10)
  sumarpuntosaleatorio4=random.randint(0,10)
  #Pregunta 1
  time.sleep(2)
  print("Primera pregunta en:")
  time.sleep(2)
  for x in range(5,0,-1):
    print(x)
    time.sleep(1)
  print (CYAN+"\n 1.  ¿Quién fue el creador de Windows? (1 a 10 puntos)"+RESET)
  print (RED+"a) Linus Torvalds"+RESET)
  print (RED+"b) Bill Gates"+RESET)
  print (RED+"c) Mark Zuckerberg"+RESET)
  print (RED+"d) Dennis Ritchie"+RESET)
  
  respuesta_1 = input("\n Tu respuesta es: ")
  while respuesta_1 not in ("a", "b", "c", "d","P"):
        respuesta_1 = input("Debes responder a, b, c o d.\n Ingresa nuevamente tu respuesta: ")
  
  if respuesta_1 == "a":
        print("Respuesta incorrecta,",nombre,". Linus Torvalds fue el creador de Linux ")
        Respuesta_Incorrecta =  Respuesta_Incorrecta + 1
        
        puntajeinicial=puntajeinicial+restarpuntosaleatorio1
        print("\n")
        print(GREEN+"Puntaje por pregunta: "+RESET,restarpuntosaleatorio1)
        print(GREEN+"Puntaje acumulado: "+RESET,puntajeinicial)
        print("\n")
  elif respuesta_1 == "c":
        print("Respuesta incorrecta,",nombre,". Mark Zuckerberg fue el creador de Facebook ")
        Respuesta_Incorrecta =  Respuesta_Incorrecta + 1
        
        puntajeinicial=puntajeinicial+restarpuntosaleatorio2
        print("\n")
        print(GREEN+"Puntaje por pregunta: "+RESET,restarpuntosaleatorio2)
        print(GREEN+"Puntaje acumulado: "+RESET,puntajeinicial)
        print("\n")
  elif respuesta_1 == "d":
        print("Respuesta incorrecta,",nombre,". Dennis Ritchie fue el creador del lenguaje C ")
        Respuesta_Incorrecta =  Respuesta_Incorrecta + 1
        
        puntajeinicial=puntajeinicial+restarpuntosaleatorio3
        print("\n")
        print(GREEN+"Puntaje por pregunta: "+RESET,restarpuntosaleatorio3)
        print(GREEN+"Puntaje acumulado: "+RESET,puntajeinicial)
        print("\n")
  elif respuesta_1 == "P":
        print("\n ¡Genial ",nombre,"!, desbloqueaste el mensaje oculto y ganste 10 puntos ")
        puntajeinicial+=10
        contaroculto+=1
        print(GREEN+"Puntos del mensaje oculto: "+RESET,mensajeoculto)
        print(GREEN+"Puntaje acumulado: "+RESET,puntajeinicial)
      
  else:
        while respuesta_1 not in ("a", "b", "c", "d"):
          respuesta_1 = input("Debes responder a, b, c o d.\n Ingresa nuevamente tu respuesta: ")
        print("\n ¡Muy Bien ",nombre,", Respuesta correcta! ")
        Respuesta_Correcta = Respuesta_Correcta + 1
        puntajeinicial=puntajeinicial+sumarpuntosaleatorio
        print("\n")
        print(GREEN+"Puntaje por pregunta: "+RESET,sumarpuntosaleatorio)
        print(GREEN+"Puntaje acumulado: "+RESET,puntajeinicial)
        print("\n")
      
      
  print(MAGENTA+"\n *******************************************************************"+RESET)
  time.sleep(2)
  print("\n Segunda pregunta en 3 segundos")
  time.sleep(1)
  print("3")
  time.sleep(1)
  print("2")
  time.sleep(1)
  print("1")
  time.sleep(1)
  #Pregunta 2
  
  ##########
  print (CYAN+"\n 2. ¿Cuál no es un navegador Web? (1 a 10 puntos)"+RESET)
  print (RED+"a) Safari"+RESET)
  print (RED+"b) Opera"+RESET)
  print (RED+"c) Microsoft Edge"+RESET)
  print (RED+"d) DuckDuckGo"+RESET)
  
  respuesta_1 = input("\n Tu respuesta es: ")
  while respuesta_1 not in ("a", "b", "c", "d","E"):
        respuesta_1 = input("Debes responder a, b, c o d.\n Ingresa nuevamente tu respuesta: ")
      
  if respuesta_1 == "a":
    
    print("Respuesta incorrecta,",nombre,". Safari si es un navegador Web ")
    Respuesta_Incorrecta =  Respuesta_Incorrecta + 1
    
    puntajeinicial=puntajeinicial+restarpuntosaleatorio1
    print("\n")
    print(GREEN+"Puntaje por pregunta: "+RESET,restarpuntosaleatorio1)
    print(GREEN+"Puntaje acumulado: "+RESET,puntajeinicial)
    print("\n")
  elif respuesta_1 == "b":
    print("Respuesta incorrecta,",nombre,". Opera si es un navegador Web ")
    Respuesta_Incorrecta =  Respuesta_Incorrecta + 1
    
    puntajeinicial=puntajeinicial+restarpuntosaleatorio2
    print("\n")
    print(GREEN+"Puntaje por pregunta: "+RESET,restarpuntosaleatorio2)
    print(GREEN+"Puntaje acumulado: "+RESET,puntajeinicial)
    print("\n")
  elif respuesta_1 == "c":
    print("Respuesta incorrecta,",nombre,". Microsoft Edge si es un navegador Web ")
    Respuesta_Incorrecta =  Respuesta_Incorrecta + 1
    
    puntajeinicial=puntajeinicial+restarpuntosaleatorio3
    print("\n")
    print(GREEN+"Puntaje por pregunta: "+RESET,restarpuntosaleatorio3)
    print(GREEN+"Puntaje acumulado: "+RESET,puntajeinicial)
    print("\n")
  elif respuesta_1 == "E":
    print("\n ¡Genial ",nombre,"!, desbloqueaste el mensaje oculto y ganste 10 puntos ")
    puntajeinicial+=10
    contaroculto+=1
    print(GREEN+"Puntos del mensaje oculto: "+RESET,mensajeoculto)
    print(GREEN+"Puntaje acumulado: "+RESET,puntajeinicial)
  
  else:
    while respuesta_1 not in ("a", "b", "c", "d"):
      respuesta_1 = input("Debes responder a, b, c o d.\n Ingresa nuevamente tu respuesta: ")
    print("\n ¡Muy Bien ",nombre,", Respuesta correcta! ")
    Respuesta_Correcta = Respuesta_Correcta + 1
    puntajeinicial=puntajeinicial+sumarpuntosaleatorio2
    print("\n")
    print(GREEN+"Puntaje por pregunta: "+RESET,sumarpuntosaleatorio2)
    print(GREEN+"Puntaje acumulado: "+RESET,puntajeinicial)
    print("\n")
  
  
  print(MAGENTA+"\n *******************************************************************"+RESET)
  
      
  
  #Pregunta 3
  time.sleep(2)
  print("\n Tercera pregunta en 3 segundos")
  time.sleep(1)
  print("3")
  time.sleep(1)
  print("2")
  time.sleep(1)
  print("1")
  time.sleep(1)
  
  print (CYAN+"\n 3. ¿Cuál no es un lenguaje de programación? (1 a 10 puntos)"+RESET)
  print (RED+"a) Java"+RESET)
  print (RED+"b) Python"+RESET)
  print (RED+"c) Notepad"+RESET)
  print (RED+"d) JavaScript"+RESET)
  
  respuesta_1 = input("\n Tu respuesta es: ")
  while respuesta_1 not in ("a", "b", "c", "d","R"):
    respuesta_1 = input("Debes responder a, b, c o d.\n Ingresa nuevamente tu respuesta: ")
  
  if respuesta_1 == "a":
    
    print("Respuesta incorrecta,",nombre,". Java si es un un lenguaje de programación ")
    Respuesta_Incorrecta =  Respuesta_Incorrecta + 1
    
    puntajeinicial=puntajeinicial+restarpuntosaleatorio1
    print("\n")
    print(GREEN+"Puntaje por pregunta: "+RESET,restarpuntosaleatorio1)
    print(GREEN+"Puntaje acumulado: "+RESET,puntajeinicial)
    print("\n")
  elif respuesta_1 == "b":
    print("Respuesta incorrecta,",nombre,". Python si es un lenguaje de programación ")
    Respuesta_Incorrecta =  Respuesta_Incorrecta + 1
    
    puntajeinicial=puntajeinicial+restarpuntosaleatorio2
    print("\n")
    print(GREEN+"Puntaje por pregunta: "+RESET,restarpuntosaleatorio2)
    print(GREEN+"Puntaje acumulado: "+RESET,puntajeinicial)
    print("\n")
  elif respuesta_1 == "d":
    print("Respuesta incorrecta,",nombre,". JavaScript si es un lenguaje de programación ")
    Respuesta_Incorrecta =  Respuesta_Incorrecta + 1
    
    puntajeinicial=puntajeinicial+restarpuntosaleatorio3
    print("\n")
    print(GREEN+"Puntaje por pregunta: "+RESET,restarpuntosaleatorio3)
    print(GREEN+"Puntaje acumulado: "+RESET,puntajeinicial)
    print("\n")
  elif respuesta_1 == "R":
    print("\n ¡Genial ",nombre,"!, desbloqueaste el mensaje oculto y ganste 10 puntos ")
    puntajeinicial+=10
    contaroculto+=1
    print(GREEN+"Puntos del mensaje oculto: "+RESET,mensajeoculto)
    print(GREEN+"Puntaje acumulado: "+RESET,puntajeinicial)
  
  else:
    while respuesta_1 not in ("a", "b", "c", "d"):
      respuesta_1 = input("Debes responder a, b, c o d.\n Ingresa nuevamente tu respuesta: ")
    print("\n ¡Muy Bien ",nombre,", Respuesta correcta! ")
    Respuesta_Correcta = Respuesta_Correcta + 1
    puntajeinicial=puntajeinicial+sumarpuntosaleatorio3
    print("\n")
    print(GREEN+"Puntaje por pregunta: "+RESET,sumarpuntosaleatorio3)
    print(GREEN+"Puntaje acumulado: "+RESET,puntajeinicial)
    print("\n")
  
  
  print(MAGENTA+"\n *******************************************************************"+RESET)
  
      
      #Pregunta 4
  time.sleep(2)
  print("\n Cuarta pregunta en 3 segundos")
  time.sleep(1)
  print("3")
  time.sleep(1)
  print("2")
  time.sleep(1)
  print("1")
  time.sleep(1)
  
  print (CYAN+"1. ¿Cuál es la plataforma del curso de selección Back End? (1 a 10 puntos)"+RESET)
  print (RED+"a) Microsoft Teams"+RESET)
  print (RED+"b) Google Forms"+RESET)
  print (RED+"c) Silabuz"+RESET)
  print (RED+"d) Goole Meet"+RESET)
  
  respuesta_1 = input("\n Tu respuesta es: ")
  while respuesta_1 not in ("a", "b", "c", "d","U"):
    respuesta_1 = input("Debes responder a, b, c o d.\n Ingresa nuevamente tu respuesta: ")
  
  if respuesta_1 == "a":
    
    print("Respuesta incorrecta,",nombre,". Microsoft Teams no es la plataforma del curso de selección Back End ")
    Respuesta_Incorrecta =  Respuesta_Incorrecta + 1
    
    puntajeinicial=puntajeinicial+restarpuntosaleatorio1
    print("\n")
    print(GREEN+"Puntaje por pregunta: "+RESET,restarpuntosaleatorio1)
    print(GREEN+"Puntaje acumulado: "+RESET,puntajeinicial)
    print("\n")
  elif respuesta_1 == "b":
    print("Respuesta incorrecta,",nombre,". Google Forms no es la plataforma del curso de selección Back End ")
    Respuesta_Incorrecta =  Respuesta_Incorrecta + 1
    
    puntajeinicial=puntajeinicial+restarpuntosaleatorio2
    print("\n")
    print(GREEN+"Puntaje por pregunta: "+RESET,restarpuntosaleatorio2)
    print(GREEN+"Puntaje acumulado: "+RESET,puntajeinicial)
    print("\n")
  elif respuesta_1 == "d":
    print("Respuesta incorrecta,",nombre,". Google Meet no es la plataforma del curso de selección Back End ")
    Respuesta_Incorrecta =  Respuesta_Incorrecta + 1
    
    puntajeinicial=puntajeinicial+restarpuntosaleatorio3
    print("\n")
    print(GREEN+"Puntaje por pregunta: "+RESET,restarpuntosaleatorio3)
    print(GREEN+"Puntaje acumulado: "+RESET,puntajeinicial)
    print("\n")
  elif respuesta_1 == "U":
    print("\n ¡Genial ",nombre,"!, desbloqueaste el mensaje oculto y ganste 10 puntos ")
    puntajeinicial+=10
    contaroculto+=1
    print(GREEN+"Puntos del mensaje oculto: "+RESET,mensajeoculto)
    print(GREEN+"Puntaje acumulado: "+RESET,puntajeinicial)
  
  else:
    while respuesta_1 not in ("a", "b", "c", "d"):
      respuesta_1 = input("Debes responder a, b, c o d.\n Ingresa nuevamente tu respuesta: ")
    print("\n ¡Muy Bien ",nombre,", Respuesta correcta! ")
    Respuesta_Correcta = Respuesta_Correcta + 1
    puntajeinicial=puntajeinicial+sumarpuntosaleatorio4
    print("\n")
    print(GREEN+"Puntaje por pregunta: "+RESET,sumarpuntosaleatorio4)
    print(GREEN+"Puntaje acumulado: "+RESET,puntajeinicial)
    print("\n")
  print(MAGENTA+"\n *******************************************************************"+RESET)
  time.sleep(2)
  print("Calculando resultados...")
  time.sleep(3)
  
  print(BLUE,"\n Resultados de la trivia"+RESET)
  print("-------------------------")
  print(YELLOW+"Nombre: "+RESET,nombre)
  print(YELLOW+"Apellido: "+RESET,apellido)
  print(YELLOW+"Respuestas correctas: "+RESET,Respuesta_Correcta)
  print(YELLOW+"Respuestas incorrectas: "+RESET,Respuesta_Incorrecta)
  print(YELLOW+"Total de mensajes ocultos: "+RESET,contaroculto)
  time.sleep(2)
  print(GREEN+"Puntuación Total: "+RESET,puntajeinicial)
  time.sleep(2)
  print(MAGENTA+"\n *******************************************************************"+RESET)
  print("\n ¿Desea intentar la Trivia nuevamente?")
  repetir_trivia=input("\n Escriba 'si' para repetir o cualquier tecla para finalizar la Trivia: ").lower()
  if repetir_trivia !="si":
     print("\n Hasta pronto, ",nombre)
     iniciartrivia=False
     print(MAGENTA+"\n *******************************************************************"+RESET)
