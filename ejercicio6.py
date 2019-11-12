##Ejercicio 1: Sea V = {0,1}, indicá la longitud de las siguientes palabras del alfabeto V:

def ejercicio1():
    V = {0,1}
    a = [0,1,0,1,1]
    b = [0,1]
    c = [0,0]
    d = []
    palabras = [a,b,c,d]

    for palabra in palabras:
        print(palabra, ":", len(palabra))
        
print("Ejercicio 1:")
ejercicio1()

##Ejercicio 2: Sea V = {a, b}, el alfabeto formado por los símbolos a y b, indicá cuáles de las siguientes son palabras de V*

def ejercicio2():

    V = {"a","b"}
   
    v = "ababbaca"
    z = "a"
    w = z

    palabras = [v,w,z]

    for palabra in palabras:
        if len(set(palabra.strip()) - V) == 0:
            print(palabra,"es palabra de V*")
        else:
            print(palabra,"no es palabra de V*")

print("")
print("Ejercicio 2:")
ejercicio2() 

##Ejercicio 3: Indicá si las siguientes opciones son verdaderas o falsas: sea V = {1, 2, 3}
##a. a=111 € L(V)
##b. b=312 € L(V)
##c. c=114 € L(V)

def ejercicio3():

    V = {"1","2","3"}
    
    a = "111"
    b = "312"
    c = "114"
    
    palabras = [a,b,c]
    
    for palabra in palabras:
        if len(set(palabra.strip()) - V) == 0:
            print(palabra,"€ a L(V)")
        else:
            print(palabra,"!€ a L(V)")

print("")
print("Ejercicio 3:")  
ejercicio3()

##Ejercicio 4: Sean V = {1,2,3} , a=111 € V; b=312 € V Concatená ab y ba. Indicá R v y R w , con v = ab y w = ba.

def ejercicio4():

    V = {1,2,3}

    a = 111
    b = 312
    
    
    
    
