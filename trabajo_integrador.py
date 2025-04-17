#   ===========================================
#   Convertidor de números decimales a binarios
#   ===========================================

def decimal_a_binario():
  # Se solicita y valida el número decimal para su conversion
  while True:
    decimal = input("Ingrese el número decimal que desea convertir: ")
    if not decimal.isdigit():
        print("Formato incorrecto. Ingrese un número válido.")
        continue

    decimal_int_op = int(decimal)
    break

  # Se definen las demas variables que vamos a utilizar
  binary = []
  exp = -1
  num_while = 0

  # Buscamos el valor del maximo exponente posible
  while num_while < decimal_int_op:
    exp += 1
    num_while = 2**exp

  # Utilizamos el valor del maximo exponente para construir, de izquierda a derecha, el número decimal en binario
  for i in range(exp, -1, -1):
    if decimal_int_op >= 2**i:
        decimal_int_op -= 2**i
        binary += "1"
    else:
        binary += "0"


  # Si el número decimal a convertir es 0, se agrega un unico cero
  if int(decimal) == 0:
    binary += "0"


  # Si el número empezo con un 0 a la izquierda, y no el número ingresado no es 0, se le saca ese primer 0 irrelevante a la izquierda
  if binary[0] == "0" and int(decimal) != 0:
    binary.pop(0)


  # Unimos el array de los caracteres binarios e imprimimos en pantalla
  print(f"El número {decimal} en binario es: ", "".join(binary))



#   ===========================================
#   Convertidor de números binarios a decimales
#   ===========================================

def binario_a_decimal ():
  # Se solicita al usuario el número binario a convertir
  numero_binario = input("Ingrese el número binario que desea convertir a decimal: ")

  # Variable valor_posicional, utilizada para calcular las potencias de 2.
  valor_posicional = 1

  # Variable acumulador, numero_decimal, para llegar al número decimal.
  numero_decimal = 0

  # Variable contador, cifra_contador, para recorrer cada cifra del binario y para generar la condición de salida del bucle while.
  # Se inicializa con el valor correspondiente al indice de la ultima cifra, para recorrer el número binario de izquierda a derecha
  cifra_contador = len(numero_binario) - 1

  # Bucle while para recorrer cada cifra del número binario
  while cifra_contador >= 0:
    # Se comprueba si la cifra es el dígito 1
    if (int(numero_binario[(cifra_contador)]) == 1):
            # Si es 1, se suma al número decimal el valor posicional correspondiente
            numero_decimal += valor_posicional

    # Se múltiplica por 2 el valor posicional y se resta 1 al contador
    valor_posicional *= 2
    cifra_contador -= 1

  # Se imprime el resultado
  print (f"El número {numero_binario} en decimal es: {numero_decimal}")

def main():
    print("Seleccione una opción:")
    print("1: Convertir de decimal a binario")
    print("2: Convertir de binario a decimal")
    opcion = input("Ingrese su opción (1 o 2): ")

    if opcion == "1":
        decimal_a_binario()
    elif opcion == "2":
        binario_a_decimal()
    else:
        print("Opción inválida.")
main()