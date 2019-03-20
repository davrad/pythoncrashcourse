def format_city(city, country, population=0):
    formated = city +', ' +country  
    if population:
        return formated + ' - population ' + str(population)
    return formated 