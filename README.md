
# Gramaticas en ANTLR: Python

En este proyecto se encuentran 3 ejemplos de gramaticas en ANTLR que dan solución a distintos problemas:
- Diseñar una gramática que permita hacer operaciones entre numeros racionales.
- Diseñar una gramática que permita implementar un **MAP** y un **FILTER**.
- Diseñar una grámatica que permita calcular la transformada de **Laplace** para una función dada.




## Requisitos
- Contar con un [**JDK**](https://www.oracle.com/java/technologies/downloads/) instalado, ya sea oficial o de openjdk.
- Tener descargada la version 3.11.0 de [**Python**.](https://www.python.org/downloads/release/python-3110/)
- Tener instalado y correctamente configurado [**Complete ANTLR 4.13.2 Java binaries jar**](https://www.antlr.org/download.html)






## Estructura del Proyecto
El proyecto esta compuesto de tres carpetas, cada una contiene las gramaticas que solucionan cada uno de los problemas mencionados al inicio.
- primer_punto -> operaciones entre numeros racionales.
- segundo_punto -> map y filter
- tercer_punto -> trasformadas de Laplace




## Getting started
Cuando se clone el proyecto se recomienda crear un entorno virtual con el comando:
```python
$ virtualenv venv
```
En dado caso de no tener virtualenv se puede instalar con el comando:
```bash
$ pip install virtualenv
```
Una vez creado el entorno virtual, debemos activarlo:
- Linux:
```bash
$ source venv/bin/activate
```
- Windows:
```powershell
.\venv\Scripts\Activate
```
Por ultimo, teniendo el entorno activado, instalamos los paquetes que se encuentran en el archivo `requirements.txt`.
```python
$ pip install -r requirements.txt
```






## Ejecutando el primer_punto
Estando en la carpeta contenedora del proyecto, debemos entrar en la carpeta del primer_punto:

```bash
$ cd primer_punto
```

Para ejecutar el primer punto basta con escribir el siguiente comando
```bash
$ python fraction_calc.py
```

Posteriormente, se debe introducir una operacion aritmetica entre numeros racionales en formato de fraccion, ejemplo:

Ejemplo:

```bash
$ python fraction_calc.py
Introduce una expresión: 1/3 + 2/3
Resultado: 9/9
Resultado simplificado: 1/1
```

python -m unittest discover -s tercer_punto/tests      

## Ejecutando el segundo_punto
Estando en la carpeta contenedora del proyecto, debemos entrar en la carpeta del segundo_punto:

```bash
$ cd segundo_punto
```

Para ejecutar el primer punto basta con escribir el siguiente comando
```bash
$ python fraction_calc.py
```

Posteriormente, se pueden introducir las siguientes entradas:
- MAP(funcion_a_aplicar, iterable)
- FILTER(condicion_a_aplicar, iterable)

Dentro de las funciones a aplicar para el MAP tenemos:
- **second_power**: Esta función eleva cada elemento del iterable al cuadrado

Dentro de las condicion a aplicar para el FILTER tenemos:
- **is_even**: Va recorriendo y verificando si el numero es par, en dado caso de que no sea lo elimina del iterable
Ejemplo de uso para el **MAP**:

```bash
$ python iterables.py
Introduce una expresión: MAP(second_power,[2,6,7,20,10,5])
Resultado de MAP: [4, 12, 14, 40, 20, 10]
```

Ejemplo de uso para el **FILTER**:

```bash
$ python iterables.py
Introduce una expresión: FILTER(is_even,[2,4,5,9,13,24,6])
Resultado de FILTER: [2, 4, 24, 6]
```  
## Ejecutando el tercer_punto
Estando en la carpeta contenedora del proyecto, debemos entrar en la carpeta del tercer_punto:

```bash
$ cd tercer_punto
```

Para ejecutar el primer punto basta con escribir el siguiente comando
```bash
$ python laplace.py
```
Una vez ejecutado el comando, debemos ingresar una expresión a la cual queremos calcularle la transformada de Laplace.

Ejemplo:
```bash
$ python laplace.py
Ingresa una función para calcular la transformada de Laplace (L[funcion]): L[e^2t]
Transformada de Laplace: 1/(s - 2.0)
```

### Corriendo los tests del tercer_punto

Adicionalmente, con ayuda de `unittest` se añadieron unas pruebas para verificar que las transformadas de Laplace fueran correctas. Estos tests se pueden encontrar en `tercer_punto/tests/test_laplace_transformation.py`. 

Para ejecutar los tests debemos estar en la carpeta contenedora del proyecto y ejecutar: 
```bash
$ python -m unittest discover -s tercer_punto/tests
```






