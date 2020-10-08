# Test script to test pyXLIGHT

from numpy import linspace,real
import pyXLIGHT

airfoil = pyXLIGHT.xfoilAnalysis('naca2412.dat')
airfoil.re = 100000
airfoil.mach = 0.0
airfoil.iter = 100

print ('----------------- Real Results ----------------')
print ('Angle      Cl         Cd         Cm')
for angle in linspace(0,10,11):
    cl,cd,cm,lexitflag = airfoil.solveAlpha(angle)
    print ('{0:8f}   {1:8f}   {2:8f}   {3:8f}'.format(angle,cl,cd,cm))

print ('----------------- Complex Results ----------------')
print ('Angle      Cl         Cd         Cm')
for angle in linspace(0,10,11):
    cl,cd,cm,lexitflag = airfoil.solveAlphaComplex(angle)
    print ('{0:8f}   {1:8f}   {2:8f}   {3:8f}'.format(angle,real(cl),real(cd),real(cm)))
