""" 
====================================
Sin decoradores
====================================
"""

from datetime import datetime

def get_hora():
    print(datetime.now().strftime('%H:%M:%S'))


def get_date():
    print(datetime.now().strftime('%Y-%m-%d'))

def funcionExterna(funcionInterna): #recibe una fc como parametro
    def funcionEnvoltorio(): #contiene a la fc interna y la ejecuta
        print('Inicio de funcion envoltorio') # codigo comun a todas las fc
        funcionInterna() # modifica el comportamiento de la fc envoltorio
        print('Fin de funcion envoltorio')
    return funcionEnvoltorio

# Importante: Una función es un OBJETO  (es un tipo de dato)
# mostar_hora = funcionExterna(get_hora) # asigna la fc envoltorio a una variable (objeto)
# mostrar_fecha = funcionExterna(get_date)
# mostar_hora() # ejecuta la fc envoltorio
# mostrar_fecha()

"""  
====================================
Con decoradores (azúcar sintáctico) 
====================================
"""

def funcionDecoradora(funcionInterna): #recibe una fc como parametro
    def funcionEnvoltorio(): #contiene a la fc interna y la ejecuta
        print('Inicio de funcion envoltorio') # codigo comun a todas las fc
        funcionInterna() # modifica el comportamiento de la fc envoltorio
        print('Fin de funcion envoltorio')
    return funcionEnvoltorio # retorna la fc envoltorio vitaminada con mas funcionalidades

@funcionDecoradora # decorador se aplica a la fc que sigue
def saludar(): # fc a decorar. Se pasa como parámetro a la fc decoradora
    print('Hola Genia !')


def despedir():
    print('Chau Genia !')

# saludar()
# despedir()

"""
====================================
Decoradores con parámetros
====================================
"""

# para pasar un nro indeterminado de argumentos uso *args



def operarConPares(operacion): # fc externa->recibe una fc como parametro
    def wrapper(*args, **kwargs): # fc envoltorio->contiene a la fc interna y la ejecuta
        soloPares = list(filter(lambda numero: numero % 2 == 0, args))
        #agregar el numero 20 a los argumentos
        soloPares.append(20)
        resultado = operacion(*soloPares, **kwargs)

        #egregar key 'edad' al diccionario kwargs
        kwargs['edad'] = 30
        
        print(f"Resultado de la operacion: {resultado}")
        print(f"mi info es: {kwargs}")
    return wrapper # retorna la fc envoltorio vitaminada con mas funcionalidades

@operarConPares
def sumar_numeros(*args, **kwargs):
    resultado = 0
    for numero in args:
        resultado += numero
    return resultado

# No se ejecuta la funcion sumar_numeros, sino la funcion envoltorio (wrapper) con mas funcionalidades.
mi_info_dict = {'nombre': 'Juan', 'apellido': 'Perez'}
sumar_numeros(1,2,3,4,5,6,7,8,9,10, **mi_info_dict)

