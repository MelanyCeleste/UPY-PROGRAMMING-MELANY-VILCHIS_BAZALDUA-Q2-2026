# UPY-PROGRAMMING-MELANY-VILCHIS_BAZALDUA-Q2-2026
Git/GitHub Repository
This repository contains Python-based implementations, developed as part of Unit 2 for the Programming course (Q2-2026). The objective of this assignment is to establish a professional development environment using Git for version control and GitHub for remote collaboration.
Project Description.
Dígito verificador
Desarrolle un programa que calcule el dígito verificador de un rol UTFSM.
Para calcular el dígito verificador, se deben realizar los siguientes pasos:
Obtener el rol sin guión ni dígito verificador.
Invertir el número. (e.g: de 201012341 a 143210102).

    Multiplicar los dígitos por la secuencia 2, 3, 4, 5, 6, 7, si es que se acaban los números, se debe comenzar denuevo, por ejemplo, con 143210102:
    1 x 2 + 4 x 3 + 3 x 4 + 2 x 5 + 1 x 6 + 0 x 7 + 1 x 2 + 0 x 3 + 2 x 4 = 52
    Al resultado obtenido, es decir, 52, debemos sacarle el módulo 11, es decir:

    52 % 11 = 8
    Con el resultado obtenido en el paso anterior, debemos restarlo de 11:  
    11 - 8 = 3  
Finalmente, el dígito verificador será el obtenido en la resta: 201012341-3.
Environment & Tools
    Language: Python 3.x
    Version Control: Git
    Hosting Platform: GitHub

