#1.- Use the countries_data.py (https://github.com/Asabeneh/30-Days-Of-Python/blob/master/data/countries-data.py) file and follow the tasks below:
#Sort countries by name, by capital, by population
import paises as datos
def nombre(pais):
    return pais["name"]
def capital(pais):
    return pais["capital"]
def populus(pais):
    return pais["population"]
def sortNombre(paises):
    return sorted(paises, key=nombre)
def sortCapital(paises):
    return sorted(paises, key=capital)
def sortPoupulus(paises, reverse=False):
    return sorted(paises, key=populus, reverse=reverse)
lstpaises = datos

sortedNombre = sortNombre(lstpaises)
print("\n Ordenado por nombre:")
for pais in sortedNombre:
    print(pais["name"])
sortedCapital = sortCapital(lstpaises)
print("\n Ordenado por capital:")
for pais in sortedCapital:
    print(pais["capital"])
sortedPoupulus = sortPoupulus(lstpaises, reverse=True)
print("\n Ordenado por población (de mayor a menor):")
for pais in sortedPoupulus:
    print(f"{pais['name']} - {pais['population']}")

#Sort out the ten most spoken languages by location.
#Sort out the ten most populated countries.



#2
from collections import Counter

def contarTop10Idiomas():
    idiomas = []
    for pais in paises.paises:  
        if "languages" in pais:  
            idiomas.extend(pais["languages"]) 
    top10Idiomas = Counter(idiomas).most_common(10)
    return top10Idiomas
def mostrarTop10Idiomas():
    top10Idiomas = contarTop10Idiomas()
    print("Los 10 idiomas más hablados globalmente son:")
    for idioma, count in top10Idiomas:
        print(f"{idioma}: {count}")
mostrarTop10Idiomas()
#3
def clasificarPaisesMasPoblados():
    paisesOrdenados = sorted(paises.paises, key=lambda pais: pais["population"], reverse=True)
    return paisesOrdenados[:10]
def mostrarTop10PaisesMasPoblados():
    top10Paises = clasificarPaisesMasPoblados()
    print("Los 10 países más poblados son:")
    for pais in top10Paises:
        print(f"{pais['name']}: {pais['population']}")
mostrarTop10PaisesMasPoblados()