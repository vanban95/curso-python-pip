import random # importamos l libreria random

mi_tupla_opc = ('piedra', 'papel', 'tijeras') # declaramos la tupla

opc_compu = random.choice(mi_tupla_opc) # choice es para elegir un indice de la tupla

"""print(mi_tupla_opc[opc_compu])"""

user_option = str(input('¿piedra, papel o tijeras?: ')) # transforma este input en minusculas

user_option = user_option.lower() # convierte input en minusculas

if user_option in mi_tupla_opc: # "in" es para                  verificar si nuestro input está en la tupla
  print('tu opción es válida,', 'la computadora eligió: ',  opc_compu)
else:
  print('tu opcion no es válida')

# Para piedra
if opc_compu == 'piedra' and user_option == 'papel':
  print('¡Ganaste tú!')
elif opc_compu == 'piedra' and user_option == 'piedra':
  print('¡Es un empate!')
elif opc_compu == 'piedra' and user_option == 'tijeras':
  print('Ganó la PC :(')

# Para papel
if opc_compu == 'papel' and user_option == 'papel':
  print('¡Es un empate!')
elif opc_compu == 'papel' and user_option == 'piedra':
  print('Ganó la PC :(')
elif opc_compu == 'papel' and user_option == 'tijeras':
  print('¡Ganas tú!')

# Para tijeras
if opc_compu == 'tijeras' and user_option == 'papel':
  print('Ganó la PC :(')
elif opc_compu == 'tijeras' and user_option == 'piedra':
  print('¡Ganas tú!')
elif opc_compu == 'tijeras' and user_option == 'tijeras':
  print('¡Es un empate')