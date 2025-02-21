# 1.Escribe una función que reciba una cadena de texto como parámetro y
# devuelva un diccionario con las frecuencias

def diccionario_frecuencias(cadena):
    """Devuelve el número de veces que se repite cada palabra de una cadena de texto

    Args:
        cadena (str): cadena de texto, como una frase

    Returns:
        dict: Devuelve un diccionario donde las claves son cada palabra o string de la cadena
        y el numero de veces que parece como valor
    """
    palabras_sueltas = cadena.split()
    diccionario_palabras = {}

    for palabra in palabras_sueltas:
        # Por cada palabra de la variable palabras_sueltas la añado al diccionario_palabras 
        # Con el get selecciono el elemento palabra y que tenga como valor inicial 0 y sume 1.
        # Algunas palabras pueden repetirse.
        diccionario_palabras[palabra] = diccionario_palabras.get(palabra, 0) + 1
    return diccionario_palabras


# Ejemplo de la función, se repiten varias palabras
texto_prueba = 'Hola de nuevo, esto es el primer ejercicio de python y es el ejercicio más sencillo'
# Invocamos la función con la variable texto_prueba
diccionario_frecuencias(texto_prueba)



#2.Dada una lista de números, obtén una nueva lista con el doble de cada valor.
# Usa la función map()

lista_num = [2,21,14,53,5]

def doblar_el_valor(num):
    """funcion para que devuelva de un o unos numeros el doble

    Args:
        num (list): Coge los números de la lista que pongamos

    Returns:
        list: Devuelve lista de numeros por dos
    """
    return num * 2

resultado_dobles = map(doblar_el_valor,lista_num)
#En el print he de convertir el objeto de devuelve map a una lista list()
# para que pueda hacer el print correctamente
print(f'El resultado del doble de {lista_num} es {list(resultado_dobles)}')



# 3.Escribe una función que tome una lista de palabras y una palabra objetivo
# como parámetros. La función debe devolver una lista con todas las palabras
# de la lista original que contengan la palabra objetivo.

def lista_con_palabra_objetivo(lista_palabras, palabra_objetivo):
    """Devuelve una lista con todas las palabras que contengan la palabra deseada.

    Args:
        lista_palabras (list): Lista de palabras
        palabra_objetivo (str): Palabra deseada

    Returns:
        list: Lista de palabras que contienen la palabra deseada
    """
    # lista de palabras filtradas por el objetivo
    palabras_filtradas = []

    for palabra in lista_palabras:
        if palabra_objetivo in palabra:
            palabras_filtradas.append(palabra)

    return palabras_filtradas

# Ejemplo de la función, se repiten varias palabras
lista1 = ["brocoli","chocolate","maiz","chorizo","coco"]
objetivo = "cho"

resultado = lista_con_palabra_objetivo(lista1,objetivo)
print(resultado)




# 4.Genera una función que calcule la diferencia entre los valores de dos listas.
# Usa la función map()

from itertools import zip_longest

lista1 = [27, 11, 3, 78, 30, 5] 
lista2 = [4, 15, 37, 41, 8]

def calcular_resta(lista_a, lista_b):
    """
    Calcula la resta entre los elementos de dos listas posición a posición.

    Args:
        lista_a (list[int | float]): Lista de números.
        lista_b (list[int | float]): Lista de números.

    Returns:
        list: Lista con las diferencias entre los elementos de ambas listas.
    """
    return list(map(lambda x, y: x - y, lista_a, lista_b))
    # podemos hacer todo en una función lambda directamente


resultado_diferencia = calcular_resta(lista1, lista2)

print(f'La diferencia de {lista1} y {lista2} es ', resultado_diferencia)




# 5.Escribe una función que tome una lista de números como parámetro y un valor opcional
# nota_aprobado, que por defecto es 5.
# La función debe calcular la media de los números en la lista y determinar si la media
# es mayor o igual que nota aprobado.
# Si es así, el estado será "aprobado", de lo contrario, será "suspenso".
# La función debe devolver una tupla que contenga la media y el estado.

lista_notas = [2,6,3,9,5,5,7,2]

def calcular_media(lista, nota_aprobado = 5):
    """
    Calcula la media de una lista de números y verifica si la media es mayor o igual
    a la nota de aprobado.

    Args:
        lista (list): Lista de números.
        nota_aprobado (int, opcional): Nota mínima para aprobar por defecto es 5.

    Returns:
        tuple: Media calculada y un mensaje indicando si se ha aprobado o no.
    """
    # calculo la media de las notas d ela lista
    media =  round(sum(lista) / len(lista),2)
    if media >= nota_aprobado:
        print('¡Aprobado!')
        return media
    else:
        print('Suspenso... :(')
        return media
    
# Ejemplo de prueba:
resultado_notas = calcular_media(lista_notas)
print(resultado_notas)



# 6.Escribe una función que calcule el factorial de un número de manera recursiva.

def calcular_factorial_recursivo(num):
    """Calcula el factorial de un numero que toma como argumento

    Returns:
        int: devuelve el factorial
    """
    # En este if else hace que cuando el numero sea 0 o 1 la función devuelve 1 y no hace más cálculos
    if num == 0 or num == 1:
        return 1 
    # Else recursivo 
    else: 
        return num * calcular_factorial_recursivo(num - 1)

# Ejemplo de uso:
numero = 5
print(f"El factorial de {numero} es {calcular_factorial_recursivo(numero)}")




# 7.Genera una función que convierta una lista de tuplas a una lista de strings.
# Usa la función map()

def convertir_a_lista_strings(lista_tupla):
    """Devuelve una tupla en una lista de strings

    Args:
        lista_tupla (tuple): Una tupla de diferentes tipos de valores

    Returns:
        list: Devuelve una lista de strings con cada valor de la tupla
    """
    return list(map(str,lista_tupla))

tupla = (3,'ojo',-2.35,'nariz',12,'mano',True)

resultado_lista = convertir_a_lista_strings(tupla)
print(f'El resultado final es: {resultado_lista}')



# 8.Escribe un programa que pida al usuario dos números e intente dividirlos.
# Si el usuario ingresa un valor no numérico o intenta dividir por cero,
# maneja esas excepciones de manera adecuada. Asegúrate de mostrar un mensaje 
# indicando si la división fue exitosa o no.

try:
    num1 = int(input('Dame un primer número'))
    num2 = int(input('Dame un segundo número'))
    resultado_division = num1 / num2
# Comprobamos que los valores input sean del tipo correcto (int)
except ValueError:
    print('Lo sentimos, los valores deben de ser sólo números')
# Comprobamos que ninguno de los valores input no sean el número 0
except ZeroDivisionError:
    print('Vaya...lo sentimos, pero no podemos hacer una división con el número 0')
else: 
    print(f'¡Bravo! El resultado de la división {num1} entre {num2} es,',round(resultado_division, 2))




# 9.Escribe una función que tome una lista de nombres de mascotas como parámetro y
# devuelva una nueva lista excluyendo ciertas mascotas prohibidas en España.
# La lista de mascotas a excluir es
# ["Mapache", "Tigre", "Serpiente Pitón", "Cocodrilo", "Oso"].Usa la función filter()

def mascotas_permitidas(mascotas):
    """Devuelve una lista de los animales permitidos en España.
    Filtra la lista dada de animales para comprobar si cada animal es prohibido o no en España (True o False)

    Args:
        mascotas (list): lista de animales

    Returns:
        (list): lista de animales con los animales prohibidos exluidos 
    """
    mascotas_prohibidas = ["Mapache", "Tigre", "Serpiente Pitón", "Cocodrilo", "Oso"]

    # Convertimos a minúsculas para comparar sin problemas
    mascotas_prohibidas = [elem.lower() for elem in mascotas_prohibidas]
    mascotas = [elem.lower() for elem in mascotas]

    def es_permitida(mascota):
        # Excluimos la mascota si alguna palabra prohibida está en su nombre
        return not any(prohibida in mascota for prohibida in mascotas_prohibidas)
    
    animales_legales = list(filter(es_permitida, mascotas))
    return animales_legales


# Lista de animales
animales_obtenidos = [' Ratón', 'Serpiente Pitón', 'Agapornis', 'Ajolote', 'Gato', 'Cocodrilo',
                      'Tigre', 'Erizo', 'Cerdo vietnamita']

resultado = mascotas_permitidas(animales_obtenidos)

print(f'Estos son los animales permitidos en España: {resultado}')



# 10.Escribe una función que reciba una lista de números y calcule su promedio.
# Si la lista está vacía, lanza una excepción personalizada y maneja el error adecuadamente

def calcular_promedio(lista_num):
    """Calcula el promedio de una lista d enumeros

    Args:
        lista_num (lits): Lista de numeros

    Raises:
        ValueError: Da error si la lista está vacía

    Returns:
        float: Devuelve el resultado del promedio
    """

    #Si la lista esta vacía ponme este mensaje de error.
    # not lista_num significa "si la lista está vacía".
    if not lista_num:
        # raise para lanzar el error manualmente
        raise ValueError("Error....la lista está vacía y no se puede calcular el promedio.")
    #Si la lista está con contenido, hazme el promedio
    return sum(lista_num) / len(lista_num)

lista_numerica = [9,2,5,7,23,17,1,4,12]

resultado = calcular_promedio(lista_numerica)

print(f'He aquí el promedio de la lista numérica', round(resultado,2))




#11.Escribe un programa que pida al usuario que introduzca su edad. Si el usuario ingresa un valor no numérico
# o un valor fuera del rango esperado (por ejemplo, menor que 0 o mayor que 120, maneja las excepciones adecuadamente

try: 
    edad = int(input('Dime tu edad'))
    
    #Compruebo que la edad esta dentro del rango esperado
    if edad <= 0 or edad > 120:
        raise ValueError('Lo siento pero no puedes tener esa edad')
    else: 
        print(f'Gracias, tu edad es: {edad}')
except ValueError:
    print('Necesitamos que ingreses un valor numérico para saber tu edad')





#12.Genera una función que al recibir una frase devuelva una lista con la longitud de cada palabra. Usa la función map()

def longitud_de_cada_palabra(frase):
    """Devuelve la longitud de las palabras de una frase

    Args:
        frase (str): La frase que se va a dividir por palabras

    Returns:
        list: Lista de longitud por palabra
    """
    palabras_frase = frase.split()
    longitud_palabras = list(map(len, palabras_frase)) 
    return longitud_palabras


frase_ejem = 'Esto es una prueba de python'
resultado = longitud_de_cada_palabra(frase_ejem)

print(f'El resultado de la longitud de las palabras de la frase... {frase_ejem} ... es {resultado}')




#13.Genera una función la cual, para un conjunto de caracteres, devuelva una lista de tuplas
# con cada letra en mayúsculas y minúsculas. Las letras no pueden estar repetidas. Usa la función map()

def devolver_lista_tuplas(caracteres):
    """Devuelve una lista de tuplas con los caracteres en minúsucla y mayúscula
    de una lista de carácteres. La letras no se repiten, ya que ponemos la función set().

    Args:
        caracteres (list): Lista de carácteres

    Returns:
        List: Devuelve una única lista con una tupla por caracter en minúscula y mayúscula
    """

    #Asegurarse que convertimos a un set el conjunto de caraceteres
    # y ademas verificamos que son strings
    # str.isalpha devuelve True si todos los caracteres de la lista caracteres son letras 
    set_caracteres =  set(filter(str.isalpha, caracteres))

    # Convertir cada caracter en minuscula y mayuscula
    def convertir_minus_mayus(elem):
        return (elem.upper(), elem.lower())
    
    # Con la variable set_caracteres y la funcion de converir a minus y mayus
    # lo metemos en una variable resultado que ademas convierte el resultado final
    # en una lista y hace map() a todos los elementos de set_caraceteres
    resultado_caracteres = list(map(convertir_minus_mayus,set_caracteres))
    return resultado_caracteres


lista_caracteres = {'D', 'e', 'A', 'b', 'C'}

r = devolver_lista_tuplas(lista_caracteres)

print(f'El resultado de la lista es, {r}')
    




#14. Crea una función que retorne las palabras de una lista de palabras que comience con una letra en especifico.
# Usa la función filter()

def devolver_palabras_por_letra(lista, letra):
    """Devuelve las palabras de una lista que empiezan por una letra concreta

    Args:
        lista (list): lista depalabras dadas
        letra (str): caracter por el que vamos a filtrar las palabras

    Returns:
        list: Devuelve una lista de palabras que empiezan por la letra deseada que pongamos
    """
    #Ponemos el parámetro letra a minúscula para hacerlo después con el primer caracter de cada palabra e igualarlas
    letra = letra.lower()

    # funcion interna que comprueba la primera letra, empezando por comprobar que la palabra no esta vacia,
    # despues la pasamos a minuscula y ponemos que sea igual que la letra dada. Devovlemos esa primera letra
    def comienza_con_letra(palabra):
        primera_letra = palabra and palabra[0].lower() == letra
        return primera_letra
    # debvolvemos la lista filtrada por aquellas palabras cuya primera letra y la letra deseada coinciden
    return list(filter(comienza_con_letra, lista))

lista_palabras = ['comida','atuendo','bricolaje','astronomía','facturación','cubertería',
                  'forraje','artillería','botánica','britocerámica','armamento']
letra_objetivo = 'c'
r = devolver_palabras_por_letra(lista_palabras, letra_objetivo)
print(f'Las palabras dadas son estas: {r}')





#15. Crea a una función lambda que sume 3 a cada número de una lista dada.

lista_numeros = [1,2,3,4,5]

#Hago esa suma con map() para que lo hago en cada uno de los elementos de la 'lista_numeros'
sumar_valores = list(map(lambda x: x + 3, lista_numeros))

print(sumar_valores)






#16 Escribe una función que tome una cadena de texto y un número entero n como parámetros y
# devuelva una lista de todas las palabras que sean más largas que n. Usa la función filter()

def devolver_palabras_mas_largas(cadena, n):
    """Devuelve aquellas palabras de una lista donde su longitud sea más larga que el número que
    metemos como argumento.

    Args:
        cadena (str): Cadena de texto
        n (int): Número por el que vamos a filtrar las palabras

    Returns:
        list: Devuelve lista de las palabras que sean más largas que el número deseado
    """
    # Separamos las palabras de la cadena de texto
    palabras = cadena.split()

    # Usamos filter con lambda para filtrar las palabras
    return list(filter(lambda palabra: len(palabra) > n, palabras))

cadena_texto = 'Hola mundo, esto es un ejercicio de python'
num = 4

r = devolver_palabras_mas_largas(cadena_texto, num)
print(f'Estas son las palabras más largas que {num}: {r}')






#17. Crea una función que tome una lista de dígitos y devuelva el número correspondiente.
# Por ejemplo, 5,7,2 corresponde al número quinientos setenta y dos 572. Usa la función reduce()

# Primero importamos la función reduce
from functools import reduce

def unir_digitos(digitos):
    """Devolvemos de una lista de dígitos separados el número completo sin comas ni espacios.

    Args:
        digitos (list): Lista de dígitos
    """
    # Usamos reduce con lambda para combinar los dígitos
    return reduce(lambda x, y: x * 10 + y, digitos)

# Ejemplo de uso
lista_digitos = [5, 7, 2]
numero_resultante = unir_digitos(lista_digitos)
print(numero_resultante)  # Salida: 572





#18.Escribe un programa en Python que cree una lista de diccionarios que contenga información de estudiantes
# (nombre, edad, calificación) y use la función filter para extraer a los estudiantes
# con una calificación mayor o igual a 90. Usa la función filter()

estudiantes = [{'nombre':'Maria','edad':31,'calificacion':90},
                {'nombre':'Juan','edad':29,'calificacion':95},
                {'nombre':'Alberto','edad':26,'calificacion':80},
                {'nombre':'Celia','edad':27,'calificacion':75},
                {'nombre':'Pedro','edad':23,'calificacion':93},
                {'nombre':'Sara','edad':22,'calificacion':72},
                {'nombre':'Sergio','edad':32,'calificacion':82},
                {'nombre':'Miguel','edad':36,'calificacion':95}]

def calificacion_alta(estudiante):

    """Devuelve el nombre, edad y calificacoin de aquellos estudiantes cuya nota es de 90 o superior

    Returns:
        dic: Devuelve un diccionario con los datos del estudiante con muy buena nota.
        Pueden salir varias líneas, es decir, varios diccionarios
    """

    return estudiante['calificacion'] >= 90
    
#Aplicamos el filtro de la funcion calificacion_alta a la lista de estudiantes que tenemos.
#Aquí solo se filtrarán/ aparecerán aquellos estudiantes con nota 90 o mayor
estudiantes_matricula = list(filter(calificacion_alta, estudiantes))

#for estudiante in estudiantes_matricula:
 #print(f'Estos son los estudiantes con una nota de 90 o más: {estudiante}')

print(f'Aquí la lista de diccionarios con los estudiantes aprobados:\n {resultado}')





#19.Crea una función lambda que filtre los números impares de una lista dada.

#Creamos la lista de numeros
numeros = [1,2,5,3,8,6,4,7,9,10]

# Generamos la funcion lambda donde va a generar una lista 
# que filtre aquellos elementos (numeros) de la lista 'numeros' 
# que sean impares
impares = list(filter(lambda x: x % 2 != 0, numeros))
print(impares)






#20.Crea una lista con elementos tipo integer y string obtén una nueva lista sólo con los valores int. Usa la función filter()

elementos = [2,'fresa','lechuga',7,'pan',3,'huevos',138,'parmesano']

solo_int = list(filter(lambda x: isinstance(x, int), elementos))
#isinstance(objeto, tipo) para verificar si el objeto 'x' pertenece al tipo de datos integer.


#Pintamos por pantalla la funcion 
print(solo_int)

#pequeña prueba con str
#solo_str = list(filter(lambda x: isinstance(x, str), elementos))
#print(solo_str)





#21.Crea una función que calcule el cubo de un número dado mediante una función lambda

num = 3

calcular_cubo_num = lambda x: x **3
print(calcular_cubo_num(num))





#22.Dada una lista numérica, obtén el producto total de los valores de dicha lista.Usa la función reduce().

numeros = [2,3,4]

producto_total = reduce(lambda x, y: x * y, numeros)
print(f'El producto toal de {numeros} es {producto_total}')




#23.Concatena una lista de palabras.Usa la función reduce() 

lista_palabras = ['La','abeja', 'reina', 'está', 'en', 'la', 'colmena']

concatenacion = reduce(lambda x, y: x + ' ' + y, lista_palabras)
print(concatenacion)





#24.Calcula la diferencia total en los valores de una lista. Usa la función reduce().

def diferencia_total(lista_num):
    """Devuelve la diferencia total de los numeros de una lista

    Args:
        lista_num (list): Lista de numeros

    Raises:
        ValueError: Devuelve el error en caso de la lista esté vacía

    Returns:
        int: Devuelve un integer de la diferencia total de todos lo números
    """
    #Si la lista esta vacía...
    if not lista_num:
        raise ValueError('La lista no puede estar vacía')
    
    return reduce(lambda x, y: x - y, lista_num)



numeros = [23,7,3,11,72,28]
numeros_vacio = []
resultado = diferencia_total(numeros)

print(f'La diferencia total de la lista {numeros} es {resultado}')






#25.Crea una función que cuente el número de caracteres en una cadena de texto dada.

def contar_num_caracteres(cadena):
    """Devuelve el número de caracteres de una cadena de texto dada

    Args:
        cadena (str): cadena de texto

    Returns:
        int: Devuelve el número de caracteres
    """
    return len(cadena)

mi_cadena = 'Hola mundo'

r = contar_num_caracteres(mi_cadena)
print(r)






#26.Crea una función lambda que calcule el resto de la división entre dos números dados.

num1 = 2
num2 = 4

resto_division = lambda x, y: x % y

r = resto_division(num1, num2)
print(f'El resto de la divisón da {r}')





#27.Crea una función que calcule el promedio de una lista de números

def promedio(numeros):
    """Sacar el promedio de una lista de números

    Args:
        numeros (lis): Lista de numeros

    Returns:
        int: promedio de los numeros
    """
    return sum(numeros) / len(numeros)

numeros_varios = [8,2,5,9,3]
r = promedio(numeros_varios)
print(f'El promedio de la listade numeros {numeros_varios} es {r}')







#28.Crea una función que busque y devuelva el primer elemento duplicado en una lista dada

def primer_duplicado(list):
    """Devuelve el primer elemento que se repite de una lista de elementos 

    Args:
        list (list): Lista de elementos de diferentes tipos, int, str, boolean

    Returns:
        int, str o boolean: Devuelve el primer valor que se repite en la lista de elementos
    """
    #generamos una variable donde los elementos va a pasar a un set() por lo que no podrán repetirse 
    # Cuando uno se repita en el lo pintaremos por pantalla
    vistos = set()

    for elem in list:
        if elem in vistos:
            #Devolvemos el elemento que ya esta en vistos
            return elem
            #Añadimos la funcion add a vistos porque es un set, en este caso append no valdría
        else:
            vistos.add(elem)
    

lista_dada = [3,'octogono',4,'cuadrado',3,'hexagono','circulo',4, 3, 'cuadrado',2,
              'rectángulo','cuadrado', 4,3,8,'triángulo', True]
r = primer_duplicado(lista_dada)
print(f'El primer elemento en repetirse en la lista de elementos es... {r}')





#29.Crea una función que convierta una variable en una cadena de texto y enmascare todos los caracteres 
# con el carácter '#', excepto los últimos cuatro

def convertir_a_str(variable):
    """Devuelve una cadena de texto que proviene de una variable y además
    sustituye los caracteres por '#' menos los ultimos 4 caracteres que los mantiene igual

    Args:
        variable (int,str): peueden ser variables de tipo int o str

    Returns:
        str: Devuelve un string 
    """
    cadena = str(variable)
   
    if len(cadena) > 4:
        # Vamos a usar aquí el slice de Python (start:stop[:step])
        # Decimos que nos ponga '#' en la cadena menos en los ultimos 4 caracteres y que nos concatene con
        # los ultimos 4 caracteres de la cadena empezando desde atrás (-4) y que no haga ni stop ni step porque no hacen falta
        caracteres_enmascarados = "#" * (len(cadena)- 4) + cadena[-4::]
    else:
        caracteres_enmascarados = cadena
    
    return caracteres_enmascarados


mi_variable = 12345678910
mi_variable2 = 'cadena de texto'

r = convertir_a_str(mi_variable2)
print(r)
type(r)







#30.Crea una función que determine si dos palabras son anagramas, es decir,
# si están formadas por las mismas letras pero en diferente orden.

def son_anagramas(palabra1, palabra2):
    """Devuelve un mensaje de si dos palabras como argumentos son anagramas entre si o no.

    Args:
        palabra1 (str): Palabra 1 a comprar
        palabra2 (str): Palabra 2 a comprar

    Returns:
        str: Devuelve un print donde se declare si es true o false 
    """
    #Igualamos las palabras a minusculas y sin espacios
    palabra1 = palabra1.replace(" ","").lower()
    palabra2 = palabra2.replace(" ","").lower()


    if sorted(palabra1) == sorted(palabra2):
        resultado_anagrama = f'¡Bravo! Las palabras "{palabra1}" y "{palabra2}" son anagramas'
    else:
        resultado_anagrama = f'Error...Las palabras "{palabra1}" y "{palabra2}" NO son anagramas'
    
    return resultado_anagrama

# Ejemplo de uso
pal1 = "nave"
pal2 = "vena"

r = son_anagramas(pal1,pal2)

print(r)






#31.Crea una función que solicite al usuario ingresar una lista de nombres y
# luego solicite un nombre para buscar en esa lista. Si el nombre está en la lista,
# se imprime un mensaje indicando que fue encontrado, de lo contrario, se lanza una excepción.

def buscar_nombre():
    try: 
        solicitud = input('Dame una lista de nombres separados por comas')
        #Convertimos el contenido metido por el usuario como un alista, pues separamos por comas
        lista_nombres = solicitud.split(",")
        #Quitamos los espacios en blanco al principio y al final, por si acaso,
        # y en cada uno de los elementos (nombres) de la lista de nombres. Igualamos a minusculas
        lista_nombres = [nombre.strip().lower() for nombre in lista_nombres]

        #Preguntamos el nombre deseado y le quitamos de nuevo los espacios en blanco
        # al inicio y al final para igualarlo a los nombres de la lista. Igualamos también a minusculas
        nombre = input('Dime un nombre de la lista que quieras encontrar').strip().lower()

        #Verificar el nomnre en la lista
        if nombre in lista_nombres:
                                    #.title() es para poner la primera letra de la palabra en mayuscula
            print(f'Bravo, el nombre {nombre.title()} está en la lista')
        else:
            raise ValueError(f'El nombre {nombre.title()} no se encuentra en esta lista')
    except ValueError:
        print('error')
    

lista_nom = "María,Alberto,Esther,Marcela,Enric,Jose,Juan,Elisa,Lucía,Javier"
buscar_nombre()
    





#32.Crea una función que tome un nombre completo y una lista de empleados, busque el nombre completo en la lista y
# devuelve el puesto del empleado si está en la lista, de lo contrario, devuelve un mensaje indicando que la persona 
# no trabaja aquí.

empleados = [
    {'nombre': 'Juan', 'apellido': 'Pascual', 'puesto': 'Gerente'},
    {'nombre': 'Ana', 'apellido': 'García', 'puesto': 'Diseñadora'},
    {'nombre': 'Luis', 'apellido': 'Corral', 'puesto': 'Desarrollador'},
    {'nombre': 'Marta', 'apellido': 'López', 'puesto': 'Analista'},
    {'nombre': 'Carlos', 'apellido': 'Velasco', 'puesto': 'Marketing'},
    {'nombre': 'Laura', 'apellido': 'Pineda', 'puesto': 'Recursos Humanos'}
]

def buscar_empleados(nombre_completo, lista_empleados):
    """Devuelve si al introducir el nombre y apellido de un empleado aparece en la lista y te dice de que trabaja,
    sino, devuelve un mensaje diciendo que ese empelado no existe en la lista

    Args:
        nombre_completo (str): nombre y apellido juntos
        lista_empleados (dicc): diccionario de empleados

    Returns:
        str: Frase con el resultado
    """

    for empleado in lista_empleados:
        # Ponemos aqui que compare el nombre y apellido con el nombre completo.
        # Igualamos todo quitando espacios al inicio y final y lo adaptamos a lower case.
        if f"{empleado['nombre']} {empleado['apellido']}".strip().lower() == nombre_completo.strip().lower():
       #if f"{empleado['nombre']} {empleado['apellido']}".lower() == nombre_completo.lower():
            return f'{nombre_completo.title()} está en la lista y trabaja como {empleado["puesto"]}'
       
    return  f'{nombre_completo.title()} no está en la lista'


nombre = input('Dame un nombre de empleado para poder buscarlo').lower()

resultado = buscar_empleados(nombre, empleados)
print(resultado)





#33.Crea una función lambda que sume elementos correspondientes de dos listas dadas.

lista1 = [2,4,6,8,5]
lista2 = [8,9,3,2,5]

sumar_listas = lambda lista1, lista2: list(map(lambda x, y: x + y, lista1, lista2))

r = sumar_listas(lista1, lista2)
print(r)






#34.Crea la clase Arbol , define un árbol genérico con un tronco y ramas como atributos. Los métodos disponibles son: 
# crecer_tronco,
# nueva_rama ,
# crecer_ramas ,
# quitar_rama
# info_arbol
# El objetivo es implementar estos métodos para manipular la estructura del árbol.

#Código a seguir:
#1. Inicializar un árbol con un tronco de longitud 1 y una lista vacía de ramas.
#2. Implementar el método crecer_tronco para aumentar la longitud del tronco en una unidad.
#3. Implementar el método nueva_rama para agregar una nueva rama de longitud 1 a la lista de ramas.
#4. Implementar el método crecer_ramas para aumentar en una unidad la longitud de todas las ramas existentes.
#5. Implementar el método quitar_rama para eliminar una rama en una posición específica.
#6. Implementar el método info_arbol para devolver información sobre la longitud del tronco, el número de ramas 
# y las longitudes de las mismas.

# Caso de uso: 
# 1. Crear un árbol.
# 2. Hacer crecer el tronco del árbol una unidad.
# 3. Añadir una nueva rama al árbol.
# 4. Hacer crecer todas las ramas del árbol una unidad.
# 5. Añadir dos nuevas ramas al árbol.
# 6. Retirar la rama situada en la posición 2.
# 7. Obtener información sobre el árbol.

class Arbol:

    def __init__(self, tronco, ramas):
        """Constructor de la clase Arbol

        Args:
            tronco (int): Longitud del troncos 
            ramas (list): Lista de las ramas que tiene
        """
        # Creamos los atributos y los asignamos al método constructor
        self.tronco = tronco
        self.ramas = ramas

    # Métodos de la clase Arbol

    def crecer_tronco(self):
        """Aumenta la longitud del tronco"""
        self.tronco += 1

    def nueva_rama(self):
        """Añade una nueva rama"""
        self.ramas.append(1)
            
    def crecer_ramas(self):
        """Aumenta la longitud de las ramas"""
        self.ramas = [rama + 1 for rama in self.ramas]  # Aumenta todas las ramas en 1
 
    def quitar_rama(self):
        """Eliminar una rama"""
        if self.ramas:
            self.ramas.pop()
            print(f"Una rama ha sido retirada. El árbol tiene {len(self.ramas)} ramas ahora.")
        else:
            print("El árbol no tiene ramas para quitar.")

    def info_arbol(self):
        """Devuelve la información sobre el árbol: tronco y las ramas."""
        return f"Tronco: {self.tronco}, Número de ramas: {len(self.ramas)}, Longitudes de las ramas: {self.ramas}"

# Instanciar un objeto Arbol
arbol_1 = Arbol(1, [])

# Métodos árbol
arbol_1.crecer_tronco()  # El tronco crece 1 unidad
arbol_1.nueva_rama()  # Añadir una rama
arbol_1.crecer_ramas()  # Las ramas crecen en una unidad (+1)
arbol_1.nueva_rama()  # Añadir otra nueva rama
arbol_1.quitar_rama()  # Quitar una rama
info = arbol_1.info_arbol()  # Muestra la información final

print(info)  # Imprimir la información final







# 36.Crea la clase UsuarioBanco ,representa a un usuario de un banco con su nombre, saldo y si tiene o no cuenta corriente.
# Proporciona métodos para realizar operaciones como retirar dinero, transferir dinero desde otro usuario y agregar dinero
# al saldo.

#Código a seguir:
# 1.Inicializar un usuario con su nombre, saldo y si tiene o no cuenta corriente mediante True y False .
# 2.Implementar el método retirar_dinero para retirar dinero del saldo del usuario. Lanzará un error en caso de no poder hacerse.
# 3.Implementar el método transferir_dinero para realizar una transferencia desde otro usuario al usuario actual. Lanzará un error en caso de no poder hacerse.
# 4. Implementar el método agregar_dinero para agregar dinero al saldo del usuario.
# CASO DE USO:
# 1. Crear dos usuarios: "Alicia" con saldo inicial de 100 y "Bob" con saldo inicial de 50, ambos con cuenta corriente.
# 2. Agregar 20 unidades de saldo de "Bob".
# 3. Hacer una transferencia de 80 unidades desde "Bob" a "Alicia".
# 4. Retirar 50 unidades de saldo a "Alicia".


class UsuarioBanco: 

    def __init__(self, nombre, saldo, cuenta_corriente):
        """Constructor de la clase UsuarioBanco.
        
        Args:
            nombre (str): Nombre del usuario del banco.
            saldo (float): Saldo en la cuenta del usuario.
            cuenta_corriente (bool): Indica si el usuario tiene cuenta corriente.
        """
        
    
        # Creamos los atributos y los asignamos al método constructor
        self.nombre = nombre
        self.saldo = saldo
        self.cuenta_corriente = cuenta_corriente
    
    #Métodos de la clase
    def retirar_dinero(self, cantidad):
        """Retira una cantidad de dinero al saldo si hay suficiente"""
        if cantidad > self.saldo:
            raise ValueError(f'{self.nombre} saldo insuficiente para retirar {cantidad}€.')
        else:
            self.saldo -= cantidad
            print(f'{self.nombre} has retirado {cantidad}€. Tu saldo restante es: {self.saldo}€')
    

    def transferir_dinero_desde_otro_usuario(self, cantidad, receptor):
        """Se transfiere dinero desde otra cuenta de usuario a la del usuario actual"""
        self.saldo += cantidad
        print(f'{self.nombre} el usuario {receptor.nombre} te ha transferido a tu saldo {cantidad}€. Tu saldo total ahora es: {self.saldo}€.')
    
    def agregar_dinero_al_saldo(self, cantidad):
        """Añade dinero al saldo de su cuenta"""
        self.saldo += cantidad
        print(f'{self.nombre} has añadido a tu saldo {cantidad}€. Tu saldo total es: {self.saldo}€.')

    def info_cuenta(self):
        """Muestra si el usuario tiene cuenta corriente o no."""
        if self.cuenta_corriente == True:
            print(f'Información General: {self.nombre}, tienes {self.saldo}€ de saldo y tienes una cuenta corriente con nosotros.')
        else:
            print(f'Información General: {self.nombre}, tienes {self.saldo}€ de saldo pero no dispones de una cuenta corriente con nosotros.')



# Instanciar un objeto Arbol
usuarioBanco_1 = UsuarioBanco('Alicia', 100, True)
usuarioBanco_2 = UsuarioBanco('Bob', 50, True)


usuarioBanco_2.agregar_dinero_al_saldo(20)
usuarioBanco_1.transferir_dinero_desde_otro_usuario(80, usuarioBanco_2)
usuarioBanco_1.retirar_dinero(50) 

usuarioBanco_1.info_cuenta()
usuarioBanco_2.info_cuenta()






#37. Crea una función llamada procesar_texto que procesa un texto según la opción especificada:
# contar_palabras, reemplazar_palabras, eliminar_palabra. 
# Estas opciones son otras funciones que tenemos que definir primero y llamar dentro de la función procesar_texto.

#Código a seguir:
#1.Crear una función contar_palabras para contar el número de veces que aparece cada palabra en el texto.
#Tiene que devolver un diccionario.

#2.Crear una función reemplazar_palabras para remplazar una palabra_original del texto por una palabra_nueva.
#Tiene que devolver el texto con el reemplazo de palabras.

#3.Crear una función eliminar_palabra para eliminar una palabra del texto.
#Tiene que devolver el texto con la palabra eliminada.

#4.Crear la función procesor_texto que tome un texto, una opción (entre 'contar','reemplazar',eliminar')
# y un número de argumentos variable según la opción indicada.

#CASO DE USO:
#Comprueba el funcionamiento completo de la función procesar_texto. 


def contar_palabras(texto):
    """Cuenta el número de veces que aparece cada palabra en el texto."""
    palabras = texto.split()
    diccionario_palabras = {}
    for palabra in palabras:
        diccionario_palabras[palabra] = diccionario_palabras.get(palabra, 0) + 1
    return diccionario_palabras

def reemplazar_palabras(texto, palabra_original, palabra_nueva):
    """Reemplaza una palabra específica en el texto por otra."""
    return texto.replace(palabra_original, palabra_nueva)

def eliminar_palabra(texto, palabra_a_eliminar):
    """Elimina una palabra específica del texto."""
    palabras = texto.split()
    palabras = [palabra for palabra in palabras if palabra != palabra_a_eliminar]
    return ' '.join(palabras)

def procesar_texto(texto, opcion, *args):
    """Procesa el texto según la opción dada: contar, reemplazar o eliminar."""
    if opcion == "contar":
        return contar_palabras(texto)
    elif opcion == "reemplazar" and len(args) == 2:
        return reemplazar_palabras(texto, args[0], args[1])
    elif opcion == "eliminar" and len(args) == 1:
        return eliminar_palabra(texto, args[0])
    else:
        return "Opción no válida o argumentos incorrectos"

# Caso de uso
texto_ejemplo = "hola mundo hola programación hola Python"

# Contar palabras
print(procesar_texto(texto_ejemplo, "contar"))

# Reemplazar palabra
print(procesar_texto(texto_ejemplo, "reemplazar", "hola", "saludos"))

# Eliminar palabra
print(procesar_texto(texto_ejemplo, "eliminar", "hola"))







#38.Genera un programa que nos diga si es de noche, de día o tarde según la hora proporcionada por el usuario.

#Importamos el módulo datetime
import datetime

def informar_horario_del_dia(hora):
    """En funcion de l ahora que meta el usuario de 0 a 23, dice si es de di,a tarde o de noche

    Args:
        hora (int): hora del día de 0 a 23

    Returns:
        str: _respuesta de si es de dia, tarde o noche
    """
    if hora >= 6 and hora < 12:
        return 'Son las {}.00 de la mañana, ¡Es de día!'.format(hora)
    elif hora >= 12 and hora < 18:
        return 'Son las {}.00 ¡Es la tarde!'.format(hora)
    elif hora >= 18 and hora <= 23 or hora >= 0 and hora < 6:
        return 'Son las {}.00...Es de noche...'.format(hora)
    else: 
        return ValueError('No es un valor válido para la hora, pon de 0 a 23')


try:
    hora = int(input('Dime una hora del día de 0 a 23'))
    resultado = informar_horario_del_dia(hora)
    print(resultado)
except ValueError:
    print('No es un valor válido para la hora, pon de 0 a 23')






#39.Escribe un programa que determine qué calificación en texto tiene un alumno en base a su calificación numérica. 
# Las reglas de calificación son: 
# - 0 - 69 insuficiente
# - 70 - 79 bien 
# - 80 - 89 muy bien 
# - 90 - 100 excelente

def calificar_nota(nota):
    """Devuelve que calificacion tiene un estudiante segun su nota

    Args:
        nota (int): nota numerica de 0 a 100

    Raises:
        ValueError: da error si la nota no se comprende entre 0 y 100

    Returns:
        str: respuesta de la calificacion del estudiante
    """
    if nota >= 0 and nota <= 69:
        return 'Tu nota es {}: Insuficiente.'.format(nota)
    elif nota >= 70 and nota <= 79:
        return 'Tu nota es {}: Bien.'.format(nota)
    elif nota >= 80 and nota <= 89:
        return 'Tu nota es {}: Muy bien'.format(nota)
    elif nota >= 90 and nota <= 100:
        return 'Tu nota es {}: ¡Excelente!'.format(nota)
    else: 
        raise ValueError('La nota no es válida, debe de ser de 0 a 100')
    
nota_alumno = 75

resultado = calificar_nota(nota_alumno)
print(resultado)





#40. Escribe una función que tome dos parámetros: figura (una cadena que puede ser "rectangulo" , "circulo" o "triangulo" )
#  y datos (una tupla con los datos necesarios para calcular el área de la figura)

#Importamos math para que podamos hacer unas operaciones matemáticas de manera mas eficiente
import math

def calcular_area_figuras(figura, datos):
    """Calcula el area de tres posibles figuras: rectangulo, circulo y triangulo.
    Segun el tipo de figura el area se calcula de una manera distinta. 


    Args:
        figura (str): Figura a elegir, pudiendo ser rectangulo, circulo y triangulo.
        datos (int or float): los datos numericos integer o float para calcular el area de la figura deseada.

    Raises:
        ValueError: lanza error si el usuairo no pone una de las tres figuras: rectangulo, circulo y triangulo.

    Returns:
        str: Respuesta del area de la figura deseada. 
    """
    if figura.lower() == 'rectangulo':
        # En un rectangulo el área se calcula el largo * el ancho. Debemos decir aquí al parámetro datos,
        # que pase los argumentos de largo y ancho. Se generará un aquí tupla (largo, ancho) donde
        # el primer valor de la tupla lo asigna a largo, y el segundo valor lo asigna a ancho.
        largo, ancho = datos
        return largo * ancho
    
    elif figura.lower() == 'circulo':
        # Aquí en cambio, metemos el argumento radio como parámetro en datos para calcular el área del círculo.
        # Con el módulo math sacamos directamente la variable pi. 
        radio = datos
        resultado_redondeado = math.pi * radio **2
        return round(resultado_redondeado,2)
    elif figura.lower() == 'triangulo':
        #Los parámetros del a´rea dle triangulo serán base * altura
        base, altura = datos
        return (base * altura) / 2
    else:
        raise ValueError('Error, debes de introducir rectangulo, circulo o triangulo como figuras validas ')
    

print(f'El resultado del área del rectángulo es: {calcular_area_figuras('rectangulo',(5, 3))}')
print(f'El área del circulo es: {calcular_area_figuras('circulo',(4))}')
print(f'El área del circulo es: {calcular_area_figuras('triangulo',(6,4))}')





#41.En este ejercicio, se te pedirá que escribas un programa en Python que utilice condicionales para determinar el 
# monto final de una compra en una tienda en línea, después de aplicar un descuento. El programa debe hacer lo siguiente: 
# 1. Solicita al usuario que ingrese el precio original de un artículo. 
# 2. Pregunta al usuario si tiene un cupón de descuento (respuesta sí o no). 
# 3. Si el usuario responde que sí, solicita que ingrese el valor del cupón de descuento. 
# 4. Aplica el descuento al precio original del artículo, siempre y cuando el valor del cupón
# sea válido (es decir, mayor a cero). Por ejemplo, descuento de 15€.  
# 5. Muestra el precio final de la compra, teniendo en cuenta el descuento aplicado o sin él. 
# 6. Recuerda utilizar estructuras de control de flujo como if, elif y else para llevar a cabo estas acciones
# en tu programa de Python.


def monto_final():
    """Calcula el mont total de la compra de un articulo en funcion de si tiene el usuario descuento o no.
    Así mismo, se calcula de manera que si el resultado va a ser negativo porque el descuento es mayor que el precio_original
    entonces el monton_final sería 0, y no un númeor negativo. 

    Raises:
        ValueError: lanza error en caso de que el usuari no ponda 'si' o 'no' a la pregunta de si tiene descuento o no.

    Returns:
        str: respuesta de cual es el monto final del articulo
    """

    precio_original = float(input('Dime el precio original del artículo'))
    cupon_descuento = input('¿Tienes algún cupón descuento? (si/no):').strip().lower()

    if cupon_descuento == 'si':
        valor_cupon = float(input('Dime el valor del cupon de descuento:'))
        if valor_cupon > 0:
            precio_final = precio_original - valor_cupon
            if precio_final < 0:
                precio_final = 0 #Pondremos valor 0 a aquellos precios que dan negativos
                
            print(f'El precio final del artículo con descuento es de {precio_final}€')
            return precio_final
        else:
            print(f'El cupón de descuento no es válido, debe ser mayor que 0')
            return precio_final 
    elif cupon_descuento == 'no':
            print(f'El precio final del artículo con es de {precio_original}€')
            return precio_original
    else:
         raise ValueError('Error, la respuesta debe ser si o no.')


r = monto_final()

print(r)


