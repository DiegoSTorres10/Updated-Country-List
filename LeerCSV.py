import csv

#se crea una funcion para leer los municipios 
def lectura ():
    Country = {}
    with open('paises.csv', 'r') as countries:
        lector = csv.reader(countries)
        next(lector)

        for fila in lector:
            nombre, _, _, _, Nomeclatura, _ =fila
            nombre.strip, Nomeclatura.strip()
            Country[nombre] = Nomeclatura
        
    return Country





if __name__ == '__main__':
    Dict_Countries = lectura ()
  
