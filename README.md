PAV - P4: reconocimiento y verificación del locutor
===================================================

Obtenga su copia del repositorio de la práctica accediendo a [Práctica 4](https://github.com/albino-pav/P4)
y pulsando sobre el botón `Fork` situado en la esquina superior derecha. A continuación, siga las
instrucciones de la [Práctica 3](https://github.com/albino-pav/P3) para crear una rama con el apellido de
los integrantes del grupo de prácticas, dar de alta al resto de integrantes como colaboradores del proyecto
y crear la copias locales del repositorio.

También debe descomprimir, en el directorio `PAV/P4`, el fichero [db_spk.tgz](https://atenea.upc.edu/pluginfile.php/3008277/mod_assign/introattachment/0/db_spk.tgz?forcedownload=1)
con la base de datos oral que se utilizará en la parte experimental de la práctica.

Como entrega deberá realizar un *pull request* con el contenido de su copia del repositorio. Recuerde
que los ficheros entregados deberán estar en condiciones de ser ejecutados con sólo ejecutar:

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~.sh
  make release
  run_spkid mfcc train test classerr verify verifyerr
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

A modo de memoria de la práctica, complete, en este mismo documento y usando el formato *markdown*, los
ejercicios indicados.

## Ejercicios.

### Extracción de características.

- Escriba el *pipeline* principal usado para calcular los coeficientes cepstrales de predicción lineal
  (LPCC), en su fichero <code>scripts/wav2lpcc.sh</code>:

sox $inputfile -t raw - dither -p 12 | $X2X +sf | $FRAME -l 200 -p 40 | $WINDOW -l 200 -L 200 |
	$LPC -l 200 | $LPC2C -M $lpcc_order > $base.lpcc


- Escriba el *pipeline* principal usado para calcular los coeficientes cepstrales en escala Mel (MFCC), en
  su fichero <code>scripts/wav2mfcc.sh</code>:

sox $inputfile -t raw - | $X2X +sf| $FRAME -l 200 -p 40 | $WINDOW -l 200 -L 200 | $MFCC -l 200 -m $mfcc_order -s 8 -w 1 > $base.mfcc


- Indique qué parámetros considera adecuados para el cálculo de los coeficientes LPCC y MFCC.

Para los coeficientes LPCC tenemos en cuenta:
	- Número de coeficientes de la predicción lineal
	- Número de coeficiente de la predicción cepstral

Para los coeficiente MFCC tenemos en cuenta:
	- Valor de la frecuencia de muestreo.
	- Número de filtros
	- Número de coeficientes a calcular.

- Inserte una imagen mostrando la dependencia entre los coeficientes 2 y 3 de las tres parametrizaciones
  para una señal de prueba.
  
  *La imagen siguiente es un ejemplo de cómo insertar imágenes en markdown*
    
+ ¿Cuál de ellas le parece que contiene más información?

- Usando el programa <code>pearson</code>, obtenga los coeficientes de correlación normalizada entre los
  parámetros 2 y 3, y rellene la tabla siguiente con los valores obtenidos.

  |                        | LP   | LPCC | MFCC |
  |------------------------|:----:|:----:|:----:|
  | &rho;<sub>x</sub>[2,3] |      |      |      |
  
  + Compare los resultados de <code>pearson</code> con los obtenidos gráficamente.
  
### Entrenamiento y visualización de los GMM.

- Inserte una gráfica que muestre la función de densidad de probabilidad modelada por el GMM de un locutor
  para sus dos primeros coeficientes de MFCC.
  
- Inserte una gráfica que permita comparar los modelos y poblaciones de dos locutores distintos. Comente el
  resultado obtenido y discuta si el modelado mediante GMM permite diferenciar las señales de uno y otro.

### Reconocimiento del locutor.

- Inserte una tabla con la tasa de error obtenida en el reconocimiento de los locutores de la base de datos
  SPEECON usando su mejor sistema de reconocimiento para los parámetros LP, LPCC y MFCC.

### Verificación del locutor.

- Inserte una tabla con el *score* obtenido con su mejor sistema de verificación del locutor en la tarea
  de verificación de SPEECON. La tabla debe incluir el umbral óptimo, el número de falsas alarmas y de
  pérdidas, y el score obtenido usando la parametrización que mejor resultado le hubiera dado en la tarea
  de reconocimiento.

LP (Train: N = 40, m = 15; Trainworld: N = 20, m = 30)
Núm. de coeficientes: 8

Error rate: 3,69%

Cost detection: 76,2

LPCC (Train: N = 40, m = 15; Trainworld: N = 20, m = 30)
Núm. de coeficientes: 12

Error rate: 1,27 %

Cost detection: 23,6

MFCC (Train: N = 50, m = 15; Trainworld: N = 50, m = 15)
Núm. de coeficientes: 16

Núm. de filtros: 25

Error rate: 63,97%

Cost detection: 86
 
### Test final y trabajo de ampliación.

En Cuanto a la ampliación de optimizar los costes del sistema, nos centramos en mejorar el sistema basado en MFCC pues consideramos que era el más desafiante.
Modificamos el script wav2mfcc especificando el número de filtros (40) y utilizamos las indicaciones del profesor (numero de gaussianas, iteraciones, num de coeficientes)
A pesar de mejorar considerablemente el sistema MFCC no fuimos capaces de mejorar los costes obtenidos con lpcc:

MFCC (Train: N = 10000000, m = 50; Trainworld: N = 10000000, m = 30)
Núm. de coeficientes: 15

Núm. de filtros: 40

Error rate: 5.54%

Cost detection: 25.6

Los ficheros .log de ampliación se han hecho con esta configuración.

