rivers = {'Nile':'Egypt','Amazon':'Brazil','Yangtze':'China',
        'Mississippi':'United States','Yenisei':'Russia','Huang He':'China'}

for river,country in rivers.items():
    print("The",river,"runs through",country)
print()
[print(river) for river in rivers.keys()]
print()
[print(country) for country in set(rivers.values())]

