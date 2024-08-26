# Tehdään ohjelma joka kysyy ympyrän säteen ja tulostaa sitten ympyrän pinta-alan.
import math

r = float(input("Mikä on ympyrän säde metreinä?:  "))
area = math.pi * r * r
print(f"Jos ympyrän säde on {r}, pinta-ala on tällöin {area:.1f} neliömetriä.")

