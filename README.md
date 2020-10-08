pyXLIGHT
========

pyXLIGHT is a version of Mark Drela's XFOIL code with the GUI features removed.
Gradient computation is implemented with the complex-step method.


Two configurations have been tested:

    Intel Fortran Compiler
    Gfortan compiler

To compile the code type:

    make intel  OR
    make gfortran

Note: make script not working with gcc/8.3, use gcc/4.9.
