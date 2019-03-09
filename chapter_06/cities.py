chongqing = {'name':'chongqing',
            'country' : 'china',
            'population':30751600,
            'fact':'''
            The only municipality under direct controll of the government
            but not on the east cost of China.'''
            }

lagos =     {'name':'lagos',
            'country' : 'nigeria',
            'population':16060303,
            'fact':'''
            The average temperature is 26.3°C throughout the year.
            '''
            }
dhaka =     {'name':'dhaka',
            'country' : 'bangladesh',
            'population':14399000,
            'fact':'''Exists since the first millenium.
            '''
            }
cities = [chongqing,lagos,dhaka]
for city in cities:
    print("Name: " + city['name'])
    print("Country: " + city['country'])
    print("Population: " + str(city['population']))
    print("Random Fact: " + city['fact'])