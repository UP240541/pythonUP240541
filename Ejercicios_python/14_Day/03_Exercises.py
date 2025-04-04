#1.- Use the countries_data.py (https://github.com/Asabeneh/30-Days-Of-Python/blob/master/data/countries-data.py) file and follow the tasks below:
#Sort countries by name, by capital, by population
from paises import aaa
print("Ejercicio 1.1")
def sort_by_name(countries):
    return sorted(countries, key=lambda x: x["name"])

def sort_by_capital(countries):
    return sorted(countries, key=lambda x: x["capital"])

def sort_by_population(countries, descending=False):
    return sorted(countries, key=lambda x: x["population"], reverse=descending)

if __name__ == "__main__":
    by_name = sort_by_name(aaa)
    by_capital = sort_by_capital(aaa)
    by_population = sort_by_population(aaa, descending=True)

    print("-------------------Acomodados por Nombre------------------- ")
    for country in by_name[:50]:
        print(country["name"], "-", country["capital"])

    print("\n-------------------Acomodados por capital-------------------")
    for country in by_capital[:50]:
        print(country["capital"], "-", country["name"])

    print("\n-------------------Poblacion-------------------")
    for country in by_population[:50]:
        print(f'{country["name"]}: {country["population"]:,}')

#Sort out the ten most spoken languages by location.
print("Ejercicio 1.2")
from collections import Counter
language_counter = Counter()
for country in aaa:
    languages = set(country.get("languages", [])) 
    for lang in languages:
        language_counter[lang] += 1
top_10_languages = language_counter.most_common(10)

print("\nTop 10 lenguages más hablados por ubicacion:")
for i, (language, count) in enumerate(top_10_languages, start=1):
    print(f"{i}. {language}: {count} countries")
#Sort out the ten most populated countries.
print("Ejercicio 1.3")
print("\nTop 10 paises más poblados segun el countries-data.py")
for country in by_population[:10]:
        print(f'{country["name"]}: {country["population"]:,}')



