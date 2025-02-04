{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# 1.Escribe una función que reciba una cadena de texto como parámetro y\n",
    "# devuelva un diccionario con las frecuencias\n",
    "\n",
    "def diccionario_frecuencias(cadena):\n",
    "    \"\"\"Devuelve el número de veces que se repite cada palabra de una cadena de texto\n",
    "\n",
    "    Args:\n",
    "        cadena (str): cadena de texto, como una frase\n",
    "\n",
    "    Returns:\n",
    "        dict: Devuelve un diccionario donde las claves son cada palabra o string de la cadena\n",
    "        y el numero de veces que parece como valor\n",
    "    \"\"\"\n",
    "    palabras_sueltas = cadena.split()\n",
    "    diccionario_palabras = {}\n",
    "\n",
    "    for palabra in palabras_sueltas:\n",
    "        # Por cada palabra de la variable palabras_sueltas la añado al diccionario_palabras \n",
    "        # Con el get selecciono el elemento palabra y que tenga como valor inicial 0 y sume 1.\n",
    "        # Algunas palabras pueden repetirse.\n",
    "        diccionario_palabras[palabra] = diccionario_palabras.get(palabra, 0) + 1\n",
    "    return diccionario_palabras\n",
    "\n",
    "\n",
    "# Ejemplo de la función, se repiten varias palabras\n",
    "texto_prueba = 'Hola de nuevo, esto es el primer ejercicio de python y es el ejercicio más sencillo'\n",
    "# Invocamos la función con la variable texto_prueba\n",
    "diccionario_frecuencias(texto_prueba)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "El resultado del doble de [2, 21, 14, 53, 5] es [4, 42, 28, 106, 10]\n"
     ]
    }
   ],
   "source": [
    "#2.Dada una lista de números, obtén una nueva lista con el doble de cada valor.\n",
    "# Usa la función map()\n",
    "\n",
    "lista_num = [2,21,14,53,5]\n",
    "\n",
    "def doblar_el_valor(num):\n",
    "    \"\"\"funcion para que devuelva de un o unos numeros el doble\n",
    "\n",
    "    Args:\n",
    "        num (list): Coge los números de la lista que pongamos\n",
    "\n",
    "    Returns:\n",
    "        list: Devuelve lista de numeros por dos\n",
    "    \"\"\"\n",
    "    return num * 2\n",
    "\n",
    "resultado_dobles = map(doblar_el_valor,lista_num)\n",
    "#En el print he de convertir el objeto de devuelve map a una lista list()\n",
    "# para que pueda hacer el print correctamente\n",
    "print(f'El resultado del doble de {lista_num} es {list(resultado_dobles)}')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 19,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "['chocolate', 'chorizo']\n"
     ]
    }
   ],
   "source": [
    "# 3.Escribe una función que tome una lista de palabras y una palabra objetivo\n",
    "# como parámetros. La función debe devolver una lista con todas las palabras\n",
    "# de la lista original que contengan la palabra objetivo.\n",
    "\n",
    "def lista_con_palabra_objetivo(lista_palabras, palabra_objetivo):\n",
    "    \"\"\"Devuelve una lista con todas las palabras que contengan la palabra deseada.\n",
    "\n",
    "    Args:\n",
    "        lista_palabras (list): Lista de palabras\n",
    "        palabra_objetivo (str): Palabra deseada\n",
    "\n",
    "    Returns:\n",
    "        list: Lista de palabras que contienen la palabra deseada\n",
    "    \"\"\"\n",
    "    # lista de palabras filtradas por el objetivo\n",
    "    palabras_filtradas = []\n",
    "\n",
    "    for palabra in lista_palabras:\n",
    "        if palabra_objetivo in palabra:\n",
    "            palabras_filtradas.append(palabra)\n",
    "\n",
    "    return palabras_filtradas\n",
    "\n",
    "# Ejemplo de la función, se repiten varias palabras\n",
    "lista1 = [\"brocoli\",\"chocolate\",\"maiz\",\"chorizo\",\"coco\"]\n",
    "objetivo = \"cho\"\n",
    "\n",
    "resultado = lista_con_palabra_objetivo(lista1,objetivo)\n",
    "print(resultado)\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "La diferencia de [27, 11, 3, 78, 30, 5] y [4, 15, 37, 41, 8] es  [23, -4, -34, 37, 22]\n"
     ]
    }
   ],
   "source": [
    "# 4.Genera una función que calcule la diferencia entre los valores de dos listas.\n",
    "# Usa la función map()\n",
    "\n",
    "from itertools import zip_longest\n",
    "\n",
    "lista1 = [27, 11, 3, 78, 30, 5] \n",
    "lista2 = [4, 15, 37, 41, 8]\n",
    "\n",
    "def calcular_resta(lista_a, lista_b):\n",
    "    \"\"\"\n",
    "    Calcula la resta entre los elementos de dos listas posición a posición.\n",
    "\n",
    "    Args:\n",
    "        lista_a (list[int | float]): Lista de números.\n",
    "        lista_b (list[int | float]): Lista de números.\n",
    "\n",
    "    Returns:\n",
    "        list: Lista con las diferencias entre los elementos de ambas listas.\n",
    "    \"\"\"\n",
    "    return list(map(lambda x, y: x - y, lista_a, lista_b))\n",
    "    # podemos hacer todo en una función lambda directamente\n",
    "\n",
    "\n",
    "resultado_diferencia = calcular_resta(lista1, lista2)\n",
    "\n",
    "print(f'La diferencia de {lista1} y {lista2} es ', resultado_diferencia)\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 21,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Suspenso... :(\n",
      "4.88\n"
     ]
    }
   ],
   "source": [
    "# 5.Escribe una función que tome una lista de números como parámetro y un valor opcional\n",
    "# nota_aprobado, que por defecto es 5.\n",
    "# La función debe calcular la media de los números en la lista y determinar si la media\n",
    "# es mayor o igual que nota aprobado.\n",
    "# Si es así, el estado será \"aprobado\", de lo contrario, será \"suspenso\".\n",
    "# La función debe devolver una tupla que contenga la media y el estado.\n",
    "\n",
    "lista_notas = [2,6,3,9,5,5,7,2]\n",
    "\n",
    "def calcular_media(lista, nota_aprobado = 5):\n",
    "    \"\"\"\n",
    "    Calcula la media de una lista de números y verifica si la media es mayor o igual\n",
    "    a la nota de aprobado.\n",
    "\n",
    "    Args:\n",
    "        lista (list): Lista de números.\n",
    "        nota_aprobado (int, opcional): Nota mínima para aprobar por defecto es 5.\n",
    "\n",
    "    Returns:\n",
    "        tuple: Media calculada y un mensaje indicando si se ha aprobado o no.\n",
    "    \"\"\"\n",
    "    # calculo la media de las notas d ela lista\n",
    "    media =  round(sum(lista) / len(lista),2)\n",
    "    if media >= nota_aprobado:\n",
    "        print('¡Aprobado!')\n",
    "        return media\n",
    "    else:\n",
    "        print('Suspenso... :(')\n",
    "        return media\n",
    "    \n",
    "# Ejemplo de prueba:\n",
    "resultado_notas = calcular_media(lista_notas)\n",
    "print(resultado_notas)\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 26,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "El factorial de 5 es 120\n"
     ]
    }
   ],
   "source": [
    "# 6.Escribe una función que calcule el factorial de un número de manera recursiva.\n",
    "\n",
    "def calcular_factorial_recursivo(num):\n",
    "    \"\"\"Calcula el factorial de un numero que toma como argumento\n",
    "\n",
    "    Returns:\n",
    "        int: devuelve el factorial\n",
    "    \"\"\"\n",
    "    # En este if else hace que cuando el numero sea 0 o 1 la función devuelve 1 y no hace más cálculos\n",
    "    if num == 0 or num == 1:\n",
    "        return 1 \n",
    "    # Else recursivo \n",
    "    else: \n",
    "        return num * calcular_factorial_recursivo(num - 1)\n",
    "\n",
    "# Ejemplo de uso:\n",
    "numero = 5\n",
    "print(f\"El factorial de {numero} es {calcular_factorial_recursivo(numero)}\")\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 40,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "El resultado final es: ['3', 'ojo', '-2.35', 'nariz', '12', 'mano', 'True']\n"
     ]
    }
   ],
   "source": [
    "# 7.Genera una función que convierta una lista de tuplas a una lista de strings.\n",
    "# Usa la función map()\n",
    "\n",
    "def convertir_a_lista_strings(lista_tupla):\n",
    "    \"\"\"Devuelve una tupla en una lista de strings\n",
    "\n",
    "    Args:\n",
    "        lista_tupla (tuple): Una tupla de diferentes tipos de valores\n",
    "\n",
    "    Returns:\n",
    "        list: Devuelve una lista de strings con cada valor de la tupla\n",
    "    \"\"\"\n",
    "    return list(map(str,lista_tupla))\n",
    "\n",
    "tupla = (3,'ojo',-2.35,'nariz',12,'mano',True)\n",
    "\n",
    "resultado_lista = convertir_a_lista_strings(tupla)\n",
    "print(f'El resultado final es: {resultado_lista}')\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "¡Bravo! El resultado de la división 8 entre 4 es, 2.0\n"
     ]
    }
   ],
   "source": [
    "# 8.Escribe un programa que pida al usuario dos números e intente dividirlos.\n",
    "# Si el usuario ingresa un valor no numérico o intenta dividir por cero,\n",
    "# maneja esas excepciones de manera adecuada. Asegúrate de mostrar un mensaje \n",
    "# indicando si la división fue exitosa o no.\n",
    "\n",
    "try:\n",
    "    num1 = int(input('Dame un primer número'))\n",
    "    num2 = int(input('Dame un segundo número'))\n",
    "    resultado_division = num1 / num2\n",
    "# Comprobamos que los valores input sean del tipo correcto (int)\n",
    "except ValueError:\n",
    "    print('Lo sentimos, los valores deben de ser sólo números')\n",
    "# Comprobamos que ninguno de los valores input no sean el número 0\n",
    "except ZeroDivisionError:\n",
    "    print('Vaya...lo sentimos, pero no podemos hacer una división con el número 0')\n",
    "else: \n",
    "    print(f'¡Bravo! El resultado de la división {num1} entre {num2} es,',round(resultado_division, 2))\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Estos son los animales permitidos en España:['ratón', 'pitón', 'agapornis', 'ajolote', 'gato', 'cocodrilo', 'serpiente', 'tigre', 'erizo', 'cerdo vietnamita']\n"
     ]
    }
   ],
   "source": [
    "# 9.Escribe una función que tome una lista de nombres de mascotas como parámetro y\n",
    "# devuelva una nueva lista excluyendo ciertas mascotas prohibidas en España.\n",
    "# La lista de mascotas a excluir es\n",
    "# [\"Mapache\", \"Tigre\", \"Serpiente Pitón\", \"Cocodrilo\", \"Oso\"].Usa la función filter()\n",
    "\n",
    "def mascotas_permitidas(mascotas):\n",
    "    \"\"\"Devuelve una lista de los animales permitidos en España.\n",
    "    Filtra la lista dada de animales para comprobar si cada animal es prohibido o no en España (True o False)\n",
    "\n",
    "    Args:\n",
    "        mascotas (list): lista de animales\n",
    "\n",
    "    Returns:\n",
    "        (list): lista de animales con los animales prohibidos exluidos \n",
    "    \"\"\"\n",
    "    mascotas_prohibidas = [\"Mapache\", \"Tigre\", \"Serpiente Pitón\", \"Cocodrilo\", \"Oso\"]\n",
    "\n",
    "    # Convertimos a minúsculas para comparar sin problemas\n",
    "    mascotas_prohibidas = [elem.lower() for elem in mascotas_prohibidas]\n",
    "    mascotas = [elem.lower() for elem in mascotas]\n",
    "\n",
    "    def es_permitida(mascota):\n",
    "        # Excluimos la mascota si alguna palabra prohibida está en su nombre\n",
    "        return not any(prohibida in mascota for prohibida in mascotas_prohibidas)\n",
    "    \n",
    "    animales_legales = list(filter(es_permitida, mascotas))\n",
    "    return animales_legales\n",
    "\n",
    "\n",
    "# Lista de animales\n",
    "animales_obtenidos = [' Ratón', 'Serpiente Pitón', 'Agapornis', 'Ajolote', 'Gato', 'Cocodrilo',\n",
    "                      'Tigre', 'Erizo', 'Cerdo vietnamita']\n",
    "\n",
    "resultado = mascotas_permitidas(animales_obtenidos)\n",
    "\n",
    "print(f'Estos son los animales permitidos en España: {resultado}')\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "He aquí el promedio de la lista numérica 8.89\n"
     ]
    }
   ],
   "source": [
    "# 10.Escribe una función que reciba una lista de números y calcule su promedio.\n",
    "# Si la lista está vacía, lanza una excepción personalizada y maneja el error adecuadamente\n",
    "\n",
    "def calcular_promedio(lista_num):\n",
    "    \"\"\"Calcula el promedio de una lista d enumeros\n",
    "\n",
    "    Args:\n",
    "        lista_num (lits): Lista de numeros\n",
    "\n",
    "    Raises:\n",
    "        ValueError: Da error si la lista está vacía\n",
    "\n",
    "    Returns:\n",
    "        float: Devuelve el resultado del promedio\n",
    "    \"\"\"\n",
    "\n",
    "    #Si la lista esta vacía ponme este mensaje de error.\n",
    "    # not lista_num significa \"si la lista está vacía\".\n",
    "    if not lista_num:\n",
    "        # raise para lanzar el error manualmente\n",
    "        raise ValueError(\"Error....la lista está vacía y no se puede calcular el promedio.\")\n",
    "    #Si la lista está con contenido, hazme el promedio\n",
    "    return sum(lista_num) / len(lista_num)\n",
    "\n",
    "lista_numerica = [9,2,5,7,23,17,1,4,12]\n",
    "\n",
    "resultado = calcular_promedio(lista_numerica)\n",
    "\n",
    "print(f'He aquí el promedio de la lista numérica', round(resultado,2))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 20,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Gracias, tu edad es: 120\n"
     ]
    }
   ],
   "source": [
    "#11.Escribe un programa que pida al usuario que introduzca su edad. Si el usuario ingresa un valor no numérico\n",
    "# o un valor fuera del rango esperado (por ejemplo, menor que 0 o mayor que 120, maneja las excepciones adecuadamente\n",
    "\n",
    "try: \n",
    "    edad = int(input('Dime tu edad'))\n",
    "    \n",
    "    #Compruebo que la edad esta dentro del rango esperado\n",
    "    if edad <= 0 or edad > 120:\n",
    "        raise ValueError('Lo siento pero no puedes tener esa edad')\n",
    "    else: \n",
    "        print(f'Gracias, tu edad es: {edad}')\n",
    "except ValueError:\n",
    "    print('Necesitamos que ingreses un valor numérico para saber tu edad')\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 39,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "El resultado de la longitud de las palabras de la frase... Esto es una prueba de python ... es [4, 2, 3, 6, 2, 6]\n"
     ]
    }
   ],
   "source": [
    "#12.Genera una función que al recibir una frase devuelva una lista con la longitud de cada palabra. Usa la función map()\n",
    "\n",
    "def longitud_de_cada_palabra(frase):\n",
    "    \"\"\"Devuelve la longitud de las palabras de una frase\n",
    "\n",
    "    Args:\n",
    "        frase (str): La frase que se va a dividir por palabras\n",
    "\n",
    "    Returns:\n",
    "        list: Lista de longitud por palabra\n",
    "    \"\"\"\n",
    "    palabras_frase = frase.split()\n",
    "    longitud_palabras = list(map(len, palabras_frase)) \n",
    "    return longitud_palabras\n",
    "\n",
    "\n",
    "frase_ejem = 'Esto es una prueba de python'\n",
    "resultado = longitud_de_cada_palabra(frase_ejem)\n",
    "\n",
    "print(f'El resultado de la longitud de las palabras de la frase... {frase_ejem} ... es {resultado}')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "El resultado de la lista es, [('E', 'e'), ('C', 'c'), ('D', 'd'), ('A', 'a'), ('B', 'b')]\n"
     ]
    }
   ],
   "source": [
    "#13.Genera una función la cual, para un conjunto de caracteres, devuelva una lista de tuplas\n",
    "# con cada letra en mayúsculas y minúsculas. Las letras no pueden estar repetidas. Usa la función map()\n",
    "\n",
    "def devolver_lista_tuplas(caracteres):\n",
    "    \"\"\"Devuelve una lista de tuplas con los caracteres en minúsucla y mayúscula\n",
    "    de una lista de carácteres. La letras no se repiten, ya que ponemos la función set().\n",
    "\n",
    "    Args:\n",
    "        caracteres (list): Lista de carácteres\n",
    "\n",
    "    Returns:\n",
    "        List: Devuelve una única lista con una tupla por caracter en minúscula y mayúscula\n",
    "    \"\"\"\n",
    "\n",
    "    #Asegurarse que convertimos a un set el conjunto de caraceteres\n",
    "    # y ademas verificamos que son strings\n",
    "    # str.isalpha devuelve True si todos los caracteres de la lista caracteres son letras \n",
    "    set_caracteres =  set(filter(str.isalpha, caracteres))\n",
    "\n",
    "    # Convertir cada caracter en minuscula y mayuscula\n",
    "    def convertir_minus_mayus(elem):\n",
    "        return (elem.upper(), elem.lower())\n",
    "    \n",
    "    # Con la variable set_caracteres y la funcion de converir a minus y mayus\n",
    "    # lo metemos en una variable resultado que ademas convierte el resultado final\n",
    "    # en una lista y hace map() a todos los elementos de set_caraceteres\n",
    "    resultado_caracteres = list(map(convertir_minus_mayus,set_caracteres))\n",
    "    return resultado_caracteres\n",
    "\n",
    "\n",
    "lista_caracteres = {'D', 'e', 'A', 'b', 'C'}\n",
    "\n",
    "r = devolver_lista_tuplas(lista_caracteres)\n",
    "\n",
    "print(f'El resultado de la lista es, {r}')\n",
    "    \n",
    "\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 18,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Las palabras dadas son estas: ['comida', 'cubertería']\n"
     ]
    }
   ],
   "source": [
    "#14. Crea una función que retorne las palabras de una lista de palabras que comience con una letra en especifico.\n",
    "# Usa la función filter()\n",
    "\n",
    "def devolver_palabras_por_letra(lista, letra):\n",
    "    \"\"\"Devuelve las palabras de una lista que empiezan por una letra concreta\n",
    "\n",
    "    Args:\n",
    "        lista (list): lista depalabras dadas\n",
    "        letra (str): caracter por el que vamos a filtrar las palabras\n",
    "\n",
    "    Returns:\n",
    "        list: Devuelve una lista de palabras que empiezan por la letra deseada que pongamos\n",
    "    \"\"\"\n",
    "    #Ponemos el parámetro letra a minúscula para hacerlo después con el primer caracter de cada palabra e igualarlas\n",
    "    letra = letra.lower()\n",
    "\n",
    "    # funcion interna que comprueba la primera letra, empezando por comprobar que la palabra no esta vacia,\n",
    "    # despues la pasamos a minuscula y ponemos que sea igual que la letra dada. Devovlemos esa primera letra\n",
    "    def comienza_con_letra(palabra):\n",
    "        primera_letra = palabra and palabra[0].lower() == letra\n",
    "        return primera_letra\n",
    "    # debvolvemos la lista filtrada por aquellas palabras cuya primera letra y la letra deseada coinciden\n",
    "    return list(filter(comienza_con_letra, lista))\n",
    "\n",
    "lista_palabras = ['comida','atuendo','bricolaje','astronomía','facturación','cubertería',\n",
    "                  'forraje','artillería','botánica','britocerámica','armamento']\n",
    "letra_objetivo = 'c'\n",
    "r = devolver_palabras_por_letra(lista_palabras, letra_objetivo)\n",
    "print(f'Las palabras dadas son estas: {r}')\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[4, 5, 6, 7, 8]\n"
     ]
    }
   ],
   "source": [
    "#15. Crea a una función lambda que sume 3 a cada número de una lista dada.\n",
    "\n",
    "lista_numeros = [1,2,3,4,5]\n",
    "\n",
    "#Hago esa suma con map() para que lo hago en cada uno de los elementos de la 'lista_numeros'\n",
    "sumar_valores = list(map(lambda x: x + 3, lista_numeros))\n",
    "\n",
    "print(sumar_valores)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "#16 Escribe una función que tome una cadena de texto y un número entero n como parámetros y\n",
    "# devuelva una lista de todas las palabras que sean más largas que n. Usa la función filter()\n",
    "\n",
    "def devolver_palabras_mas_largas(cadena, n):\n",
    "    \"\"\"Devuelve aquellas palabras de una lista donde su longitud sea más larga que el número que\n",
    "    metemos como argumento.\n",
    "\n",
    "    Args:\n",
    "        cadena (str): Cadena de texto\n",
    "        n (int): Número por el que vamos a filtrar las palabras\n",
    "\n",
    "    Returns:\n",
    "        list: Devuelve lista de las palabras que sean más largas que el número deseado\n",
    "    \"\"\"\n",
    "    # Separamos las palabras de la cadena de texto\n",
    "    palabras = cadena.split()\n",
    "\n",
    "    # Usamos filter con lambda para filtrar las palabras\n",
    "    return list(filter(lambda palabra: len(palabra) > n, palabras))\n",
    "\n",
    "cadena_texto = 'Hola mundo, esto es un ejercicio de python'\n",
    "num = 4\n",
    "\n",
    "r = devolver_palabras_mas_largas(cadena_texto, num)\n",
    "print(f'Estas son las palabras más largas que {num}: {r}')\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "#17. Crea una función que tome una lista de dígitos y devuelva el número correspondiente.\n",
    "# Por ejemplo, 5,7,2 corresponde al número quinientos setenta y dos 572. Usa la función reduce()\n",
    "\n",
    "# Primero importamos la función reduce\n",
    "from functools import reduce\n",
    "\n",
    "def unir_digitos(digitos):\n",
    "    \"\"\"Devolvemos de una lista de dígitos separados el número completo sin comas ni espacios.\n",
    "\n",
    "    Args:\n",
    "        digitos (list): Lista de dígitos\n",
    "    \"\"\"\n",
    "    # Usamos reduce con lambda para combinar los dígitos\n",
    "    return reduce(lambda x, y: x * 10 + y, digitos)\n",
    "\n",
    "# Ejemplo de uso\n",
    "lista_digitos = [5, 7, 2]\n",
    "numero_resultante = unir_digitos(lista_digitos)\n",
    "print(numero_resultante)  # Salida: 572\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 18,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Aquí la lista de diccionarios con los estudiantes aprobados:\n",
      " [{'nombre': 'Maria', 'edad': 31, 'calificacion': 90}, {'nombre': 'Juan', 'edad': 29, 'calificacion': 95}, {'nombre': 'Pedro', 'edad': 23, 'calificacion': 93}, {'nombre': 'Miguel', 'edad': 36, 'calificacion': 95}]\n"
     ]
    }
   ],
   "source": [
    "#18.Escribe un programa en Python que cree una lista de diccionarios que contenga información de estudiantes\n",
    "# (nombre, edad, calificación) y use la función filter para extraer a los estudiantes\n",
    "# con una calificación mayor o igual a 90. Usa la función filter()\n",
    "\n",
    "estudiantes = [{'nombre':'Maria','edad':31,'calificacion':90},\n",
    "                {'nombre':'Juan','edad':29,'calificacion':95},\n",
    "                {'nombre':'Alberto','edad':26,'calificacion':80},\n",
    "                {'nombre':'Celia','edad':27,'calificacion':75},\n",
    "                {'nombre':'Pedro','edad':23,'calificacion':93},\n",
    "                {'nombre':'Sara','edad':22,'calificacion':72},\n",
    "                {'nombre':'Sergio','edad':32,'calificacion':82},\n",
    "                {'nombre':'Miguel','edad':36,'calificacion':95}]\n",
    "\n",
    "def calificacion_alta(estudiante):\n",
    "\n",
    "    \"\"\"Devuelve el nombre, edad y calificacoin de aquellos estudiantes cuya nota es de 90 o superior\n",
    "\n",
    "    Returns:\n",
    "        dic: Devuelve un diccionario con los datos del estudiante con muy buena nota.\n",
    "        Pueden salir varias líneas, es decir, varios diccionarios\n",
    "    \"\"\"\n",
    "\n",
    "    return estudiante['calificacion'] >= 90\n",
    "    \n",
    "#Aplicamos el filtro de la funcion calificacion_alta a la lista de estudiantes que tenemos.\n",
    "#Aquí solo se filtrarán/ aparecerán aquellos estudiantes con nota 90 o mayor\n",
    "estudiantes_matricula = list(filter(calificacion_alta, estudiantes))\n",
    "\n",
    "#for estudiante in estudiantes_matricula:\n",
    " #print(f'Estos son los estudiantes con una nota de 90 o más: {estudiante}')\n",
    "\n",
    "print(f'Aquí la lista de diccionarios con los estudiantes aprobados:\\n {resultado}')\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[2, 8, 6, 4, 10]\n"
     ]
    }
   ],
   "source": [
    "#19.Crea una función lambda que filtre los números impares de una lista dada.\n",
    "\n",
    "#Creamos la lista de numeros\n",
    "numeros = [1,2,5,3,8,6,4,7,9,10]\n",
    "\n",
    "# Generamos la funcion lambda donde va a generar una lista \n",
    "# que filtre aquellos elementos (numeros) de la lista 'numeros' \n",
    "# que sean impares\n",
    "impares = list(filter(lambda x: x % 2 != 0, numeros))\n",
    "print(impares)\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[2, 7, 3, 138]\n",
      "['fresa', 'lechuga', 'pan', 'huevos', 'parmesano']\n"
     ]
    }
   ],
   "source": [
    "#20.Crea una lista con elementos tipo integer y string obtén una nueva lista sólo con los valores int. Usa la función filter()\n",
    "\n",
    "elementos = [2,'fresa','lechuga',7,'pan',3,'huevos',138,'parmesano']\n",
    "\n",
    "solo_int = list(filter(lambda x: isinstance(x, int), elementos))\n",
    "#isinstance(objeto, tipo) para verificar si el objeto 'x' pertenece al tipo de datos integer.\n",
    "\n",
    "\n",
    "#Pintamos por pantalla la funcion \n",
    "print(solo_int)\n",
    "\n",
    "#pequeña prueba con str\n",
    "#solo_str = list(filter(lambda x: isinstance(x, str), elementos))\n",
    "#print(solo_str)\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "27\n"
     ]
    }
   ],
   "source": [
    "#21.Crea una función que calcule el cubo de un número dado mediante una función lambda\n",
    "\n",
    "num = 3\n",
    "\n",
    "calcular_cubo_num = lambda x: x **3\n",
    "\n",
    "print(calcular_cubo_num(num))\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 19,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "El producto toal de [2, 3, 4] es 24\n"
     ]
    }
   ],
   "source": [
    "#22.Dada una lista numérica, obtén el producto total de los valores de dicha lista.Usa la función reduce().\n",
    "\n",
    "numeros = [2,3,4]\n",
    "\n",
    "producto_total = reduce(lambda x, y: x * y, numeros)\n",
    "\n",
    "print(f'El producto toal de {numeros} es {producto_total}')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 26,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "La abeja reina está en la colmena\n"
     ]
    }
   ],
   "source": [
    "#23.Concatena una lista de palabras.Usa la función reduce() \n",
    "\n",
    "lista_palabras = ['La','abeja', 'reina', 'está', 'en', 'la', 'colmena']\n",
    "\n",
    "concatenacion = reduce(lambda x, y: x + ' ' + y, lista_palabras)\n",
    "\n",
    "print(concatenacion)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "#24.Calcula la diferencia total en los valores de una lista. Usa la función reduce().\n",
    "\n",
    "def diferencia_total(lista_num):\n",
    "    \"\"\"Devuelve la diferencia total de los numeros de una lista\n",
    "\n",
    "    Args:\n",
    "        lista_num (list): Lista de numeros\n",
    "\n",
    "    Raises:\n",
    "        ValueError: Devuelve el error en caso de la lista esté vacía\n",
    "\n",
    "    Returns:\n",
    "        int: Devuelve un integer de la diferencia total de todos lo números\n",
    "    \"\"\"\n",
    "    #Si la lista esta vacía...\n",
    "    if not lista_num:\n",
    "        raise ValueError('La lista no puede estar vacía')\n",
    "    \n",
    "    return reduce(lambda x, y: x - y, lista_num)\n",
    "\n",
    "\n",
    "\n",
    "numeros = [23,7,3,11,72,28]\n",
    "numeros_vacio = []\n",
    "resultado = diferencia_total(numeros)\n",
    "\n",
    "print(f'La diferencia total de la lista {numeros} es {resultado}')\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "#25.Crea una función que cuente el número de caracteres en una cadena de texto dada.\n",
    "\n",
    "def contar_num_caracteres(cadena):\n",
    "    \"\"\"Devuelve el número de caracteres de una cadena de texto dada\n",
    "\n",
    "    Args:\n",
    "        cadena (str): cadena de texto\n",
    "\n",
    "    Returns:\n",
    "        int: Devuelve el número de caracteres\n",
    "    \"\"\"\n",
    "    return len(cadena)\n",
    "\n",
    "mi_cadena = 'Hola mundo'\n",
    "\n",
    "r = contar_num_caracteres(mi_cadena)\n",
    "print(r)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 39,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "El resto de la divisón da 2\n"
     ]
    }
   ],
   "source": [
    "#26.Crea una función lambda que calcule el resto de la división entre dos números dados.\n",
    "\n",
    "num1 = 2\n",
    "num2 = 4\n",
    "\n",
    "resto_division = lambda x, y: x % y\n",
    "\n",
    "r = resto_division(num1, num2)\n",
    "print(f'El resto de la divisón da {r}')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 41,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "El promedio de la listade numeros [8, 2, 5, 9, 3] es 5.4\n"
     ]
    }
   ],
   "source": [
    "#27.Crea una función que calcule el promedio de una lista de números\n",
    "\n",
    "def promedio(numeros):\n",
    "    \"\"\"Sacar el promedio de una lista de números\n",
    "\n",
    "    Args:\n",
    "        numeros (lis): Lista de numeros\n",
    "\n",
    "    Returns:\n",
    "        int: promedio de los numeros\n",
    "    \"\"\"\n",
    "    return sum(numeros) / len(numeros)\n",
    "\n",
    "numeros_varios = [8,2,5,9,3]\n",
    "r = promedio(numeros_varios)\n",
    "print(f'El promedio de la listade numeros {numeros_varios} es {r}')\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 61,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "El primer elemento en repetirse en la lista de elementos es... 3\n"
     ]
    }
   ],
   "source": [
    "#28.Crea una función que busque y devuelva el primer elemento duplicado en una lista dada\n",
    "\n",
    "\n",
    "def primer_duplicado(list):\n",
    "    \"\"\"Devuelve el primer elemento que se repite de una lista de elementos \n",
    "\n",
    "    Args:\n",
    "        list (list): Lista de elementos de diferentes tipos, int, str, boolean\n",
    "\n",
    "    Returns:\n",
    "        int, str o boolean: Devuelve el primer valor que se repite en la lista de elementos\n",
    "    \"\"\"\n",
    "    #generamos una variable donde los elementos va a pasar a un set() por lo que no podrán repetirse \n",
    "    # Cuando uno se repita en el lo pintaremos por pantalla\n",
    "    vistos = set()\n",
    "\n",
    "    for elem in list:\n",
    "        if elem in vistos:\n",
    "            #Devolvemos el elemento que ya esta en vistos\n",
    "            return elem\n",
    "            #Añadimos la funcion add a vistos porque es un set, en este caso append no valdría\n",
    "        else:\n",
    "            vistos.add(elem)\n",
    "    \n",
    "\n",
    "lista_dada = [3,'octogono',4,'cuadrado',3,'hexagono','circulo',4, 3, 'cuadrado',2,\n",
    "              'rectángulo','cuadrado', 4,3,8,'triángulo', True]\n",
    "r = primer_duplicado(lista_dada)\n",
    "print(f'El primer elemento en repetirse en la lista de elementos es... {r}')\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "#29.Crea una función que convierta una variable en una cadena de texto y enmascare todos los caracteres \n",
    "# con el carácter '#', excepto los últimos cuatro\n",
    "\n",
    "def convertir_a_str(variable):\n",
    "    \"\"\"Devuelve una cadena de texto que proviene de una variable y además\n",
    "    sustituye los caracteres por '#' menos los ultimos 4 caracteres que los mantiene igual\n",
    "\n",
    "    Args:\n",
    "        variable (int,str): peueden ser variables de tipo int o str\n",
    "\n",
    "    Returns:\n",
    "        str: Devuelve un string \n",
    "    \"\"\"\n",
    "    cadena = str(variable)\n",
    "   \n",
    "    if len(cadena) > 4:\n",
    "        # Vamos a usar aquí el slice de Python (start:stop[:step])\n",
    "        # Decimos que nos ponga '#' en la cadena menos en los ultimos 4 caracteres y que nos concatene con\n",
    "        # los ultimos 4 caracteres de la cadena empezando desde atrás (-4) y que no haga ni stop ni step porque no hacen falta\n",
    "        caracteres_enmascarados = \"#\" * (len(cadena)- 4) + cadena[-4::]\n",
    "    else:\n",
    "        caracteres_enmascarados = cadena\n",
    "    \n",
    "    return caracteres_enmascarados\n",
    "\n",
    "\n",
    "\n",
    "mi_variable = 12345678910\n",
    "mi_variable2 = 'cadena de texto'\n",
    "\n",
    "\n",
    "r = convertir_a_str(mi_variable2)\n",
    "print(r)\n",
    "type(r)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 88,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "¡Bravo! Las palabras \"nave\" y \"vena\" son anagramas\n"
     ]
    }
   ],
   "source": [
    "#30.Crea una función que determine si dos palabras son anagramas, es decir,\n",
    "# si están formadas por las mismas letras pero en diferente orden.\n",
    "\n",
    "def son_anagramas(palabra1, palabra2):\n",
    "    \"\"\"Devuelve un mensaje de si dos palabras como argumentos son anagramas entre si o no.\n",
    "\n",
    "    Args:\n",
    "        palabra1 (str): Palabra 1 a comprar\n",
    "        palabra2 (str): Palabra 2 a comprar\n",
    "\n",
    "    Returns:\n",
    "        str: Devuelve un print donde se declare si es true o false \n",
    "    \"\"\"\n",
    "    #Igualamos las palabras a minusculas y sin espacios\n",
    "    palabra1 = palabra1.replace(\" \",\"\").lower()\n",
    "    palabra2 = palabra2.replace(\" \",\"\").lower()\n",
    "\n",
    "\n",
    "    if sorted(palabra1) == sorted(palabra2):\n",
    "        resultado_anagrama = f'¡Bravo! Las palabras \"{palabra1}\" y \"{palabra2}\" son anagramas'\n",
    "    else:\n",
    "        resultado_anagrama = f'Error...Las palabras \"{palabra1}\" y \"{palabra2}\" NO son anagramas'\n",
    "    \n",
    "    return resultado_anagrama\n",
    "\n",
    "# Ejemplo de uso\n",
    "pal1 = \"nave\"\n",
    "pal2 = \"vena\"\n",
    "\n",
    "r = son_anagramas(pal1,pal2)\n",
    "\n",
    "print(r)\n",
    "\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Bravo, el nombre Jose está en la lista\n"
     ]
    }
   ],
   "source": [
    "#31.Crea una función que solicite al usuario ingresar una lista de nombres y\n",
    "# luego solicite un nombre para buscar en esa lista. Si el nombre está en la lista,\n",
    "# se imprime un mensaje indicando que fue encontrado, de lo contrario, se lanza una excepción.\n",
    "\n",
    "def buscar_nombre():\n",
    "    try: \n",
    "        solicitud = input('Dame una lista de nombres separados por comas')\n",
    "        #Convertimos el contenido metido por el usuario como un alista, pues separamos por comas\n",
    "        lista_nombres = solicitud.split(\",\")\n",
    "        #Quitamos los espacios en blanco al principio y al final, por si acaso,\n",
    "        # y en cada uno de los elementos (nombres) de la lista de nombres. Igualamos a minusculas\n",
    "        lista_nombres = [nombre.strip().lower() for nombre in lista_nombres]\n",
    "\n",
    "        #Preguntamos el nombre deseado y le quitamos de nuevo los espacios en blanco\n",
    "        # al inicio y al final para igualarlo a los nombres de la lista. Igualamos también a minusculas\n",
    "        nombre = input('Dime un nombre de la lista que quieras encontrar').strip().lower()\n",
    "\n",
    "        #Verificar el nomnre en la lista\n",
    "        if nombre in lista_nombres:\n",
    "                                    #.title() es para poner la primera letra de la palabra en mayuscula\n",
    "            print(f'Bravo, el nombre {nombre.title()} está en la lista')\n",
    "        else:\n",
    "            raise ValueError(f'El nombre {nombre.title()} no se encuentra en esta lista')\n",
    "    except ValueError:\n",
    "        print('error')\n",
    "    \n",
    "\n",
    "lista_nom = \"María,Alberto,Esther,Marcela,Enric,Jose,Juan,Elisa,Lucía,Javier\"\n",
    "buscar_nombre()\n",
    "    "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Laura Macho no está en la lista\n"
     ]
    }
   ],
   "source": [
    "#32.Crea una función que tome un nombre completo y una lista de empleados, busque el nombre completo en la lista y\n",
    "# devuelve el puesto del empleado si está en la lista, de lo contrario, devuelve un mensaje indicando que la persona \n",
    "# no trabaja aquí.\n",
    "\n",
    "empleados = [\n",
    "    {'nombre': 'Juan', 'apellido': 'Pascual', 'puesto': 'Gerente'},\n",
    "    {'nombre': 'Ana', 'apellido': 'García', 'puesto': 'Diseñadora'},\n",
    "    {'nombre': 'Luis', 'apellido': 'Corral', 'puesto': 'Desarrollador'},\n",
    "    {'nombre': 'Marta', 'apellido': 'López', 'puesto': 'Analista'},\n",
    "    {'nombre': 'Carlos', 'apellido': 'Velasco', 'puesto': 'Marketing'},\n",
    "    {'nombre': 'Laura', 'apellido': 'Pineda', 'puesto': 'Recursos Humanos'}\n",
    "]\n",
    "\n",
    "def buscar_empleados(nombre_completo, lista_empleados):\n",
    "    \"\"\"Devuelve si al introducir el nombre y apellido de un empleado aparece en la lista y te dice de que trabaja,\n",
    "    sino, devuelve un mensaje diciendo que ese empelado no existe en la lista\n",
    "\n",
    "    Args:\n",
    "        nombre_completo (str): nombre y apellido juntos\n",
    "        lista_empleados (dicc): diccionario de empleados\n",
    "\n",
    "    Returns:\n",
    "        str: Frase con el resultado\n",
    "    \"\"\"\n",
    "\n",
    "    for empleado in lista_empleados:\n",
    "        # Ponemos aqui que compare el nombre y apellido con el nombre completo.\n",
    "        # Igualamos todo quitando espacios al inicio y final y lo adaptamos a lower case.\n",
    "        if f\"{empleado['nombre']} {empleado['apellido']}\".strip().lower() == nombre_completo.strip().lower():\n",
    "       #if f\"{empleado['nombre']} {empleado['apellido']}\".lower() == nombre_completo.lower():\n",
    "            return f'{nombre_completo.title()} está en la lista y trabaja como {empleado[\"puesto\"]}'\n",
    "       \n",
    "    return  f'{nombre_completo.title()} no está en la lista'\n",
    "\n",
    "\n",
    "\n",
    "nombre = input('Dame un nombre de empleado para poder buscarlo').lower()\n",
    "\n",
    "resultado = buscar_empleados(nombre, empleados)\n",
    "print(resultado)\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 100,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[10, 13, 9, 10, 10]\n"
     ]
    }
   ],
   "source": [
    "#33.Crea una función lambda que sume elementos correspondientes de dos listas dadas.\n",
    "\n",
    "lista1 = [2,4,6,8,5]\n",
    "lista2 = [8,9,3,2,5]\n",
    "\n",
    "\n",
    "sumar_listas = lambda lista1, lista2: list(map(lambda x, y: x + y, lista1, lista2))\n",
    "\n",
    "r = sumar_listas(lista1, lista2)\n",
    "print(r)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Una rama ha sido retirada. El árbol tiene 1 ramas ahora.\n",
      "Tronco: 2, Número de ramas: 1, Longitudes de las ramas: [2]\n"
     ]
    }
   ],
   "source": [
    "#34.Crea la clase Arbol , define un árbol genérico con un tronco y ramas como atributos. Los métodos disponibles son: \n",
    "# crecer_tronco,\n",
    "# nueva_rama ,\n",
    "# crecer_ramas ,\n",
    "# quitar_rama\n",
    "# info_arbol\n",
    "# El objetivo es implementar estos métodos para manipular la estructura del árbol.\n",
    "\n",
    "#Código a seguir:\n",
    "#1. Inicializar un árbol con un tronco de longitud 1 y una lista vacía de ramas.\n",
    "#2. Implementar el método crecer_tronco para aumentar la longitud del tronco en una unidad.\n",
    "#3. Implementar el método nueva_rama para agregar una nueva rama de longitud 1 a la lista de ramas.\n",
    "#4. Implementar el método crecer_ramas para aumentar en una unidad la longitud de todas las ramas existentes.\n",
    "#5. Implementar el método quitar_rama para eliminar una rama en una posición específica.\n",
    "#6. Implementar el método info_arbol para devolver información sobre la longitud del tronco, el número de ramas \n",
    "# y las longitudes de las mismas.\n",
    "\n",
    "# Caso de uso: \n",
    "# 1. Crear un árbol.\n",
    "# 2. Hacer crecer el tronco del árbol una unidad.\n",
    "# 3. Añadir una nueva rama al árbol.\n",
    "# 4. Hacer crecer todas las ramas del árbol una unidad.\n",
    "# 5. Añadir dos nuevas ramas al árbol.\n",
    "# 6. Retirar la rama situada en la posición 2.\n",
    "# 7. Obtener información sobre el árbol.\n",
    "\n",
    "class Arbol:\n",
    "\n",
    "    def __init__(self, tronco, ramas):\n",
    "        \"\"\"Constructor de la clase Arbol\n",
    "\n",
    "        Args:\n",
    "            tronco (int): Longitud del troncos \n",
    "            ramas (list): Lista de las ramas que tiene\n",
    "        \"\"\"\n",
    "        # Creamos los atributos y los asignamos al método constructor\n",
    "        self.tronco = tronco\n",
    "        self.ramas = ramas\n",
    "\n",
    "    # Métodos de la clase Arbol\n",
    "\n",
    "    def crecer_tronco(self):\n",
    "        \"\"\"Aumenta la longitud del tronco\"\"\"\n",
    "        self.tronco += 1\n",
    "\n",
    "    def nueva_rama(self):\n",
    "        \"\"\"Añade una nueva rama\"\"\"\n",
    "        self.ramas.append(1)\n",
    "            \n",
    "    def crecer_ramas(self):\n",
    "        \"\"\"Aumenta la longitud de las ramas\"\"\"\n",
    "        self.ramas = [rama + 1 for rama in self.ramas]  # Aumenta todas las ramas en 1\n",
    " \n",
    "    def quitar_rama(self):\n",
    "        \"\"\"Eliminar una rama\"\"\"\n",
    "        if self.ramas:\n",
    "            self.ramas.pop()\n",
    "            print(f\"Una rama ha sido retirada. El árbol tiene {len(self.ramas)} ramas ahora.\")\n",
    "        else:\n",
    "            print(\"El árbol no tiene ramas para quitar.\")\n",
    "\n",
    "    def info_arbol(self):\n",
    "        \"\"\"Devuelve la información sobre el árbol: tronco y las ramas.\"\"\"\n",
    "        return f\"Tronco: {self.tronco}, Número de ramas: {len(self.ramas)}, Longitudes de las ramas: {self.ramas}\"\n",
    "\n",
    "# Instanciar un objeto Arbol\n",
    "arbol_1 = Arbol(1, [])\n",
    "\n",
    "# Métodos árbol\n",
    "arbol_1.crecer_tronco()  # El tronco crece 1 unidad\n",
    "arbol_1.nueva_rama()  # Añadir una rama\n",
    "arbol_1.crecer_ramas()  # Las ramas crecen en una unidad (+1)\n",
    "arbol_1.nueva_rama()  # Añadir otra nueva rama\n",
    "arbol_1.quitar_rama()  # Quitar una rama\n",
    "info = arbol_1.info_arbol()  # Muestra la información final\n",
    "\n",
    "print(info)  # Imprimir la información final\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Bob has añadido a tu saldo 20€. Tu saldo total es: 70€.\n",
      "Alicia el usuario Bob te ha transferido a tu saldo 80€. Tu saldo total ahora es: 180€.\n",
      "Alicia has retirado 50€. Tu saldo restante es: 130€\n",
      "Información General: Alicia, tienes 130€ de saldo y tienes una cuenta corriente con nosotros.\n",
      "Información General: Bob, tienes 70€ de saldo y tienes una cuenta corriente con nosotros.\n"
     ]
    }
   ],
   "source": [
    "# 36.Crea la clase UsuarioBanco ,representa a un usuario de un banco con su nombre, saldo y si tiene o no cuenta corriente.\n",
    "# Proporciona métodos para realizar operaciones como retirar dinero, transferir dinero desde otro usuario y agregar dinero\n",
    "# al saldo.\n",
    "\n",
    "#Código a seguir:\n",
    "# 1.Inicializar un usuario con su nombre, saldo y si tiene o no cuenta corriente mediante True y False .\n",
    "# 2.Implementar el método retirar_dinero para retirar dinero del saldo del usuario. Lanzará un error en caso de no poder hacerse.\n",
    "# 3.Implementar el método transferir_dinero para realizar una transferencia desde otro usuario al usuario actual. Lanzará un error en caso de no poder hacerse.\n",
    "# 4. Implementar el método agregar_dinero para agregar dinero al saldo del usuario.\n",
    "# CASO DE USO:\n",
    "# 1. Crear dos usuarios: \"Alicia\" con saldo inicial de 100 y \"Bob\" con saldo inicial de 50, ambos con cuenta corriente.\n",
    "# 2. Agregar 20 unidades de saldo de \"Bob\".\n",
    "# 3. Hacer una transferencia de 80 unidades desde \"Bob\" a \"Alicia\".\n",
    "# 4. Retirar 50 unidades de saldo a \"Alicia\".\n",
    "\n",
    "\n",
    "class UsuarioBanco: \n",
    "\n",
    "    def __init__(self, nombre, saldo, cuenta_corriente):\n",
    "        \"\"\"Constructor de la clase UsuarioBanco.\n",
    "        \n",
    "        Args:\n",
    "            nombre (str): Nombre del usuario del banco.\n",
    "            saldo (float): Saldo en la cuenta del usuario.\n",
    "            cuenta_corriente (bool): Indica si el usuario tiene cuenta corriente.\n",
    "        \"\"\"\n",
    "        \n",
    "    \n",
    "        # Creamos los atributos y los asignamos al método constructor\n",
    "        self.nombre = nombre\n",
    "        self.saldo = saldo\n",
    "        self.cuenta_corriente = cuenta_corriente\n",
    "    \n",
    "    #Métodos de la clase\n",
    "    def retirar_dinero(self, cantidad):\n",
    "        \"\"\"Retira una cantidad de dinero al saldo si hay suficiente\"\"\"\n",
    "        if cantidad > self.saldo:\n",
    "            raise ValueError(f'{self.nombre} saldo insuficiente para retirar {cantidad}€.')\n",
    "        else:\n",
    "            self.saldo -= cantidad\n",
    "            print(f'{self.nombre} has retirado {cantidad}€. Tu saldo restante es: {self.saldo}€')\n",
    "    \n",
    "\n",
    "    def transferir_dinero_desde_otro_usuario(self, cantidad, receptor):\n",
    "        \"\"\"Se transfiere dinero desde otra cuenta de usuario a la del usuario actual\"\"\"\n",
    "        self.saldo += cantidad\n",
    "        print(f'{self.nombre} el usuario {receptor.nombre} te ha transferido a tu saldo {cantidad}€. Tu saldo total ahora es: {self.saldo}€.')\n",
    "    \n",
    "    def agregar_dinero_al_saldo(self, cantidad):\n",
    "        \"\"\"Añade dinero al saldo de su cuenta\"\"\"\n",
    "        self.saldo += cantidad\n",
    "        print(f'{self.nombre} has añadido a tu saldo {cantidad}€. Tu saldo total es: {self.saldo}€.')\n",
    "\n",
    "    def info_cuenta(self):\n",
    "        \"\"\"Muestra si el usuario tiene cuenta corriente o no.\"\"\"\n",
    "        if self.cuenta_corriente == True:\n",
    "            print(f'Información General: {self.nombre}, tienes {self.saldo}€ de saldo y tienes una cuenta corriente con nosotros.')\n",
    "        else:\n",
    "            print(f'Información General: {self.nombre}, tienes {self.saldo}€ de saldo pero no dispones de una cuenta corriente con nosotros.')\n",
    "\n",
    "\n",
    "\n",
    "# Instanciar un objeto Arbol\n",
    "usuarioBanco_1 = UsuarioBanco('Alicia', 100, True)\n",
    "usuarioBanco_2 = UsuarioBanco('Bob', 50, True)\n",
    "\n",
    "\n",
    "usuarioBanco_2.agregar_dinero_al_saldo(20)\n",
    "usuarioBanco_1.transferir_dinero_desde_otro_usuario(80, usuarioBanco_2)\n",
    "usuarioBanco_1.retirar_dinero(50) \n",
    "\n",
    "usuarioBanco_1.info_cuenta()\n",
    "usuarioBanco_2.info_cuenta()\n",
    "\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "{'hola': 3, 'mundo': 1, 'programación': 1, 'Python': 1}\n",
      "saludos mundo saludos programación saludos Python\n",
      "mundo programación Python\n"
     ]
    }
   ],
   "source": [
    "#37. Crea una función llamada procesar_texto que procesa un texto según la opción especificada:\n",
    "# contar_palabras, reemplazar_palabras, eliminar_palabra. \n",
    "# Estas opciones son otras funciones que tenemos que definir primero y llamar dentro de la función procesar_texto.\n",
    "\n",
    "#Código a seguir:\n",
    "#1.Crear una función contar_palabras para contar el número de veces que aparece cada palabra en el texto.\n",
    "#Tiene que devolver un diccionario.\n",
    "\n",
    "#2.Crear una función reemplazar_palabras para remplazar una palabra_original del texto por una palabra_nueva.\n",
    "#Tiene que devolver el texto con el reemplazo de palabras.\n",
    "\n",
    "#3.Crear una función eliminar_palabra para eliminar una palabra del texto.\n",
    "#Tiene que devolver el texto con la palabra eliminada.\n",
    "\n",
    "#4.Crear la función procesor_texto que tome un texto, una opción (entre 'contar','reemplazar',eliminar')\n",
    "# y un número de argumentos variable según la opción indicada.\n",
    "\n",
    "#CASO DE USO:\n",
    "#Comprueba el funcionamiento completo de la función procesar_texto. \n",
    "\n",
    "\n",
    "def contar_palabras(texto):\n",
    "    \"\"\"Cuenta el número de veces que aparece cada palabra en el texto.\"\"\"\n",
    "    palabras = texto.split()\n",
    "    diccionario_palabras = {}\n",
    "    for palabra in palabras:\n",
    "        diccionario_palabras[palabra] = diccionario_palabras.get(palabra, 0) + 1\n",
    "    return diccionario_palabras\n",
    "\n",
    "def reemplazar_palabras(texto, palabra_original, palabra_nueva):\n",
    "    \"\"\"Reemplaza una palabra específica en el texto por otra.\"\"\"\n",
    "    return texto.replace(palabra_original, palabra_nueva)\n",
    "\n",
    "def eliminar_palabra(texto, palabra_a_eliminar):\n",
    "    \"\"\"Elimina una palabra específica del texto.\"\"\"\n",
    "    palabras = texto.split()\n",
    "    palabras = [palabra for palabra in palabras if palabra != palabra_a_eliminar]\n",
    "    return ' '.join(palabras)\n",
    "\n",
    "def procesar_texto(texto, opcion, *args):\n",
    "    \"\"\"Procesa el texto según la opción dada: contar, reemplazar o eliminar.\"\"\"\n",
    "    if opcion == \"contar\":\n",
    "        return contar_palabras(texto)\n",
    "    elif opcion == \"reemplazar\" and len(args) == 2:\n",
    "        return reemplazar_palabras(texto, args[0], args[1])\n",
    "    elif opcion == \"eliminar\" and len(args) == 1:\n",
    "        return eliminar_palabra(texto, args[0])\n",
    "    else:\n",
    "        return \"Opción no válida o argumentos incorrectos\"\n",
    "\n",
    "# Caso de uso\n",
    "texto_ejemplo = \"hola mundo hola programación hola Python\"\n",
    "\n",
    "# Contar palabras\n",
    "print(procesar_texto(texto_ejemplo, \"contar\"))\n",
    "\n",
    "# Reemplazar palabra\n",
    "print(procesar_texto(texto_ejemplo, \"reemplazar\", \"hola\", \"saludos\"))\n",
    "\n",
    "# Eliminar palabra\n",
    "print(procesar_texto(texto_ejemplo, \"eliminar\", \"hola\"))\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 27,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Son las 22.00...Es de noche...\n"
     ]
    }
   ],
   "source": [
    "#38.Genera un programa que nos diga si es de noche, de día o tarde según la hora proporcionada por el usuario.\n",
    "\n",
    "#Importamos el módulo datetime\n",
    "import datetime\n",
    "\n",
    "def informar_horario_del_dia(hora):\n",
    "    \"\"\"En funcion de l ahora que meta el usuario de 0 a 23, dice si es de di,a tarde o de noche\n",
    "\n",
    "    Args:\n",
    "        hora (int): hora del día de 0 a 23\n",
    "\n",
    "    Returns:\n",
    "        str: _respuesta de si es de dia, tarde o noche\n",
    "    \"\"\"\n",
    "    if hora >= 6 and hora < 12:\n",
    "        return 'Son las {}.00 de la mañana, ¡Es de día!'.format(hora)\n",
    "    elif hora >= 12 and hora < 18:\n",
    "        return 'Son las {}.00 ¡Es la tarde!'.format(hora)\n",
    "    elif hora >= 18 and hora <= 23 or hora >= 0 and hora < 6:\n",
    "        return 'Son las {}.00...Es de noche...'.format(hora)\n",
    "    else: \n",
    "        return ValueError('No es un valor válido para la hora, pon de 0 a 23')\n",
    "\n",
    "\n",
    "try:\n",
    "    hora = int(input('Dime una hora del día de 0 a 23'))\n",
    "    resultado = informar_horario_del_dia(hora)\n",
    "    print(resultado)\n",
    "except ValueError:\n",
    "    print('No es un valor válido para la hora, pon de 0 a 23')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 53,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Tu nota es 75: Bien.\n"
     ]
    }
   ],
   "source": [
    "#39.Escribe un programa que determine qué calificación en texto tiene un alumno en base a su calificación numérica. \n",
    "# Las reglas de calificación son: \n",
    "# - 0 - 69 insuficiente\n",
    "# - 70 - 79 bien \n",
    "# - 80 - 89 muy bien \n",
    "# - 90 - 100 excelente\n",
    "\n",
    "def calificar_nota(nota):\n",
    "    \"\"\"Devuelve que calificacion tiene un estudiante segun su nota\n",
    "\n",
    "    Args:\n",
    "        nota (int): nota numerica de 0 a 100\n",
    "\n",
    "    Raises:\n",
    "        ValueError: da error si la nota no se comprende entre 0 y 100\n",
    "\n",
    "    Returns:\n",
    "        str: respuesta de la calificacion del estudiante\n",
    "    \"\"\"\n",
    "    if nota >= 0 and nota <= 69:\n",
    "        return 'Tu nota es {}: Insuficiente.'.format(nota)\n",
    "    elif nota >= 70 and nota <= 79:\n",
    "        return 'Tu nota es {}: Bien.'.format(nota)\n",
    "    elif nota >= 80 and nota <= 89:\n",
    "        return 'Tu nota es {}: Muy bien'.format(nota)\n",
    "    elif nota >= 90 and nota <= 100:\n",
    "        return 'Tu nota es {}: ¡Excelente!'.format(nota)\n",
    "    else: \n",
    "        raise ValueError('La nota no es válida, debe de ser de 0 a 100')\n",
    "    \n",
    "nota_alumno = 75\n",
    "\n",
    "resultado = calificar_nota(nota_alumno)\n",
    "print(resultado)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 72,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "El resultado del área del rectángulo es: 15\n",
      "El área del circulo es: 50.27\n",
      "El área del circulo es: 12.0\n"
     ]
    }
   ],
   "source": [
    "#40. Escribe una función que tome dos parámetros: figura (una cadena que puede ser \"rectangulo\" , \"circulo\" o \"triangulo\" )\n",
    "#  y datos (una tupla con los datos necesarios para calcular el área de la figura)\n",
    "\n",
    "#Importamos math para que podamos hacer unas operaciones matemáticas de manera mas eficiente\n",
    "import math\n",
    "\n",
    "def calcular_area_figuras(figura, datos):\n",
    "    \"\"\"Calcula el area de tres posibles figuras: rectangulo, circulo y triangulo.\n",
    "    Segun el tipo de figura el area se calcula de una manera distinta. \n",
    "\n",
    "\n",
    "    Args:\n",
    "        figura (str): Figura a elegir, pudiendo ser rectangulo, circulo y triangulo.\n",
    "        datos (int or float): los datos numericos integer o float para calcular el area de la figura deseada.\n",
    "\n",
    "    Raises:\n",
    "        ValueError: lanza error si el usuairo no pone una de las tres figuras: rectangulo, circulo y triangulo.\n",
    "\n",
    "    Returns:\n",
    "        str: Respuesta del area de la figura deseada. \n",
    "    \"\"\"\n",
    "    if figura.lower() == 'rectangulo':\n",
    "        # En un rectangulo el área se calcula el largo * el ancho. Debemos decir aquí al parámetro datos,\n",
    "        # que pase los argumentos de largo y ancho. Se generará un aquí tupla (largo, ancho) donde\n",
    "        # el primer valor de la tupla lo asigna a largo, y el segundo valor lo asigna a ancho.\n",
    "        largo, ancho = datos\n",
    "        return largo * ancho\n",
    "    \n",
    "    elif figura.lower() == 'circulo':\n",
    "        # Aquí en cambio, metemos el argumento radio como parámetro en datos para calcular el área del círculo.\n",
    "        # Con el módulo math sacamos directamente la variable pi. \n",
    "        radio = datos\n",
    "        resultado_redondeado = math.pi * radio **2\n",
    "        return round(resultado_redondeado,2)\n",
    "    elif figura.lower() == 'triangulo':\n",
    "        #Los parámetros del a´rea dle triangulo serán base * altura\n",
    "        base, altura = datos\n",
    "        return (base * altura) / 2\n",
    "    else:\n",
    "        raise ValueError('Error, debes de introducir rectangulo, circulo o triangulo como figuras validas ')\n",
    "    \n",
    "\n",
    "print(f'El resultado del área del rectángulo es: {calcular_area_figuras('rectangulo',(5, 3))}')\n",
    "print(f'El área del circulo es: {calcular_area_figuras('circulo',(4))}')\n",
    "print(f'El área del circulo es: {calcular_area_figuras('triangulo',(6,4))}')\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "El precio final del artículo con descuento es de 0€\n",
      "0\n"
     ]
    }
   ],
   "source": [
    "#41.En este ejercicio, se te pedirá que escribas un programa en Python que utilice condicionales para determinar el \n",
    "# monto final de una compra en una tienda en línea, después de aplicar un descuento. El programa debe hacer lo siguiente: \n",
    "# 1. Solicita al usuario que ingrese el precio original de un artículo. \n",
    "# 2. Pregunta al usuario si tiene un cupón de descuento (respuesta sí o no). \n",
    "# 3. Si el usuario responde que sí, solicita que ingrese el valor del cupón de descuento. \n",
    "# 4. Aplica el descuento al precio original del artículo, siempre y cuando el valor del cupón\n",
    "# sea válido (es decir, mayor a cero). Por ejemplo, descuento de 15€.  \n",
    "# 5. Muestra el precio final de la compra, teniendo en cuenta el descuento aplicado o sin él. \n",
    "# 6. Recuerda utilizar estructuras de control de flujo como if, elif y else para llevar a cabo estas acciones\n",
    "# en tu programa de Python.\n",
    "\n",
    "\n",
    "\n",
    "def monto_final():\n",
    "    \"\"\"Calcula el mont total de la compra de un articulo en funcion de si tiene el usuario descuento o no.\n",
    "    Así mismo, se calcula de manera que si el resultado va a ser negativo porque el descuento es mayor que el precio_original\n",
    "    entonces el monton_final sería 0, y no un númeor negativo. \n",
    "\n",
    "    Raises:\n",
    "        ValueError: lanza error en caso de que el usuari no ponda 'si' o 'no' a la pregunta de si tiene descuento o no.\n",
    "\n",
    "    Returns:\n",
    "        str: respuesta de cual es el monto final del articulo\n",
    "    \"\"\"\n",
    "\n",
    "    precio_original = float(input('Dime el precio original del artículo'))\n",
    "    cupon_descuento = input('¿Tienes algún cupón descuento? (si/no):').strip().lower()\n",
    "\n",
    "    if cupon_descuento == 'si':\n",
    "        valor_cupon = float(input('Dime el valor del cupon de descuento:'))\n",
    "        if valor_cupon > 0:\n",
    "            precio_final = precio_original - valor_cupon\n",
    "            if precio_final < 0:\n",
    "                precio_final = 0 #Pondremos valor 0 a aquellos precios que dan negativos\n",
    "                \n",
    "            print(f'El precio final del artículo con descuento es de {precio_final}€')\n",
    "            return precio_final\n",
    "        else:\n",
    "            print(f'El cupón de descuento no es válido, debe ser mayor que 0')\n",
    "            return precio_final \n",
    "    elif cupon_descuento == 'no':\n",
    "            print(f'El precio final del artículo con es de {precio_original}€')\n",
    "            return precio_original\n",
    "    else:\n",
    "         raise ValueError('Error, la respuesta debe ser si o no.')\n",
    "\n",
    "\n",
    "r = monto_final()\n",
    "\n",
    "print(r)\n",
    "\n",
    "\n"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.13.1"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
