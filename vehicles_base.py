vehicles = []

vehicle_1 = {
    'id': 1,
    'type': 'osobno',
    'manufacturer': 'Toyota',
    'registration': 'RR 1234 AA',
    'first_registration': 2023,
    'price_.000_EUR': 25,
}

vehicle_2 = {
   'id': 2,
    'type': 'pick up',
    'manufacturer': 'Toyota',
    'vehicle_registration': 'RR 2345 AB',
    'first_registration': 2025,
    'price_.000_EUR': 75,
}

vehicle_3 = {
    'id': 3,
    'type': 'kombi',
    'manufacturer': 'Mercedes',
    'registration': 'RR 3456 AC',
    'first_registration': 2022,
    'price_.000_EUR': 100,
}

vehicle_4 = {
    'id': 4,
    'type': 'SUV',
    'manufacturer': 'Volvo',
    'registration': 'RR 4567 AD',
    'first_registration': 2024,
    'price_.000_EUR': 120,
}

vehicles.append(vehicle_1)
vehicles.append(vehicle_2)
vehicles.append(vehicle_3)
vehicles.append(vehicle_4)
    
print()
print(f'{'*'*20} Vozni park drustva Tvrtka d.o.o. {'*'*20}')
print()
for index, key in enumerate(vehicle_1):
    if index == 0:
        print(f'{key.upper()}', end="")
    elif index == 1:
        print(f'\t{key.upper():<10}', end="")
    else:
        print(f'{key.upper():^20}', end="")
print()

for vehicle in vehicles:
    for i, value in enumerate(vehicle):
        if i == 0:
            print(f'{vehicle[value]}', end="")
        elif i == 1:
            print(f'\t{vehicle[value]:<10}', end="")
        elif i > 1:
            print(f'{vehicle[value]:^20}', end="")
        elif i == len(vehicle):
            print(f'{vehicle[value]:^20}')
    print()
print()

    



