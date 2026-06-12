# UPY-PROGRAMMING-MELANY-VILCHIS_BAZALDUA-Q2-2026
# Git/GitHub Repository

This repository contains Python-based implementations, developed as part of Unit 2 for the Programming course (Q2-2026). 

The objective of this assignment is to establish a professional development environment using Git for version control and GitHub for remote collaboration.
Project Description.

# Numerical Integration Calculator

Its main objective is to approximate the area under the curve of a mathematical function f(x) within a defined interval [a, b].

Since computers do not integrate analytically (as one would do on paper using integration rules), the program uses geometric approximations. To achieve this, it divides the total area into 1000 small segments (n = 1000) and sums the area of each one.

# 1. Preparation and Data Capture (Inputs)
The code prompts the user for the integration limits (a and b), the function, and the desired method.

Highlight: A very useful validation was implemented to process the constant pi. If the user types "pi", the code uses the .replace() function to substitute the text with the exact numerical value from the math library.

Subsequently, h is calculated, which represents the "width" or base of each rectangle, using the formula h = (b - a) / n.

# 2. Optimization of the Rectangular Methods (LRM, RRM, MRM)
Instead of programming three independent for loops for each rectangular method, the development unified the logic through the use of the shift and constant variables.

-LRM (Left): The loop starts without alterations (shift = 0), evaluating the height of the rectangle at the left edge of the subinterval.

-RRM (Right): The loop shifts one space (shift = 1), evaluating the height starting from the next point.

-MRM (Midpoint): The value of constant (h/2) is added to the position variable. This moves the evaluation point exactly to the center of the subinterval before calculating its height.

# 3. Trapezoid Method Implementation (TRAP)
For this method, the logic was handled separately because its formula differs from the previous ones. Instead of summing flat rectangular areas, this method requires averaging the sides:

First, the code calculates and evaluates the endpoints of the curve in isolation.

Then, it uses a for loop to sum double all the intermediate heights, respecting the mathematical structure of the trapezoid method.

# Environment and Tools

Language: Python 3.x

Version Control: Git

Hosting Platform: GitHub

# How to run the program
Ensure you have Python installed on your system.
Clone this repository or download the source file:

    https://github.com/MelanyCeleste/UPY-PROGRAMMING-MELANY-VILCHIS_BAZALDUA-Q2-2026/blob/7a92a4d6bbb8f4f7e80f83011d28b25ca0d9ad54/C0W8/CW08.py

# AI Use Declaration

AI tools were used exclusively to assist in drafting this README file to explain the code development process. No AI was used during the actual programming, logic design, or version control setup of this assignment.