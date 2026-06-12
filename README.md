# UPY-PROGRAMMING-MELANY-VILCHIS_BAZALDUA-Q2-2026
# Git/GitHub Repository

This repository contains Python-based implementations, developed as part of Unit 2 for the Programming course (Q2-2026). 

The objective of this assignment is to establish a professional development environment using Git for version control and GitHub for remote collaboration.
Project Description.

# Calculadora de integración numérica

Su objetivo principal es aproximar el área bajo la curva de una función matemática f(x) en un intervalo definido [a, b].

Dado que las computadoras no integran de forma analítica (como se haría en papel con reglas de integración), el programa utiliza aproximaciones geométricas. Para lograrlo, divide el área total en 1000 pequeños segmentos (n = 1000) y suma el área de cada uno de ellos.

# 1. Preparación y Captura de Datos (Inputs)

-El código solicita al usuario los límites de integración (a y b), la función y el método deseado.

-Acierto destacado: Se implementó una validación muy útil para procesar la constante pi. Si el usuario escribe "pi", el código utiliza la función .replace() para sustituir el texto por el valor numérico exacto proveniente de la librería math.

-Posteriormente, se calcula h, que representa el "ancho" o la base de cada rectangulo, utilizando la fórmula h = (b - a) / n.

# 2. Optimización de los Métodos Rectangulares (LRM, RRM, MRM)

En lugar de programar tres ciclos for independientes para cada método rectangular, el desarrollo unificó la lógica mediante el uso de las variables shift y constant.

LRM (Izquierda): El ciclo inicia sin alteraciones (shift = 0), evaluando la altura del rectángulo en el borde izquierdo del subintervalo.

RRM (Derecha): El ciclo se desplaza un espacio (shift = 1), evaluando la altura a partir del siguiente punto.

MRM (Punto Medio): Se suma el valor de constant (h/2) a la variable de posición. Esto traslada el punto de evaluación exactamente al centro del subintervalo antes de calcular su altura.

# 3. Implementación del Método del Trapecio (TRAP)

Para este método, la lógica se manejó por separado debido a que su fórmula difiere de las anteriores. En lugar de sumar áreas rectangulares planas, este método requiere promediar los lados:

Primero, el código calcula y evalúa los extremos de la curva de manera aislada.

Luego, utiliza un ciclo for para sumar el doble de todas las alturas intermedias, respetando la estructura matemática del método del trapecio.

# Ambiente y herramientas

    Idioma: Python 3.x
    Control de versiones: Git
    Plataforma de alojamiento: GitHub

# Como ejecutar el programa

Asegúrese de tener Python instalado en su sistema.
Clone este repositorio o descargue el archivo fuente:

    https://github.com/MelanyCeleste/UPY-PROGRAMMING-MELANY-VILCHIS_BAZALDUA-Q2-2026/blob/7a92a4d6bbb8f4f7e80f83011d28b25ca0d9ad54/C0W8/CW08.py

# Declaración de uso de IA

Se utilizaron herramientas de IA exclusivamente para ayudar en la redacción de este archivo README y explicar el proceso de desarrollo. No se utilizó IA en la programación, lógica del código ni en la configuración del control de versiones.