# 💻 Programación 1  
**Tecnicatura Universitaria en Programación**  
📍 *Universidad Tecnológica Nacional*  

## ✨ Estudiantes  
- **Nombre:** Martin Gomez  
- **Nombre:** Marianela Guerrero  
- **Nombre:** Matias Farfan  
- **Nombre:** Emilia Gomez Juarez  
- **Nombre:** Lucas Desiderio Silva  
- **Comisión:** M2025-7   

## Convertidor de Números: Decimal <-> Binario
Este proyecto incluye dos funciones principales para convertir números entre los sistemas decimal y binario. Es una herramienta educativa diseñada para comprender los procesos de conversión paso a paso.
### Funciones Principales

## 1. decimal_a_binario()
Convierte un número decimal (base 10) ingresado por el usuario a su representación binaria (base 2).
Proceso:
- **Validación:** Solicita al usuario un número decimal válido.
- **Determinación de Exponentes:** Calcula el mayor exponente de 2 aplicable al número ingresado.
- **Construcción del Binario:** A través de un bucle, determina los bits binarios (1 o 0) para cada exponente.
- **Formato:** Elimina ceros irrelevantes y genera la salida binaria.

**Caso especial:**
- Si el número ingresado es 0, el resultado binario será simplemente "0".

Ejemplo de uso:
Entrada: 13
Salida: 1101

## 2. binario_a_decimal()
Convierte un número binario (base 2) ingresado por el usuario a su representación decimal (base 10).
Proceso:
- **Validación:** Solicita al usuario un número binario válido (compuesto solo por 0 y 1).
- **Recorrido del Binario:** Recorre cada dígito del número binario desde derecha a izquierda.
- **Cálculo Decimal:** Multiplica cada dígito 1 por su posición correspondiente en potencias de 2 y suma los resultados.
- **Salida:** Imprime el número decimal resultante.

**Caso especial:**
- Si el número ingresado es 0, el resultado decimal será 0.

Ejemplo de uso:
Entrada: 1101
Salida: 13

## Cómo Usar Este Programa
- Ejecute el archivo Python en un intérprete de Python 3.x.
- Siga las instrucciones en pantalla para elegir la conversión:
- Opción 1: Decimal a Binario.
- Opción 2: Binario a Decimal.
- Opción 3: Salir del programa.

- Ingrese los números de acuerdo con las reglas de cada conversión.

## Notas Técnicas
- Robustez: El código valida entradas para evitar errores, pero asegúrate de seguir las instrucciones de ingreso.
- Personalización: Puedes personalizar los mensajes de entrada o formato de salida.
- Depuración: Usa mensajes print() para comprobar el estado de las variables durante la ejecución.


## Ejecución
Ejecuta el código en cualquier intérprete de Python 3.x. Asegúrate de seguir los pasos para ingresar valores válidos según la conversión que desees realizar.
