import os


#region INIT

company = {
    'id': 1,
    'name': 'Pajdo und Jaranen GmbH',
    'tax_id': '01234567891',
    'vehicles': [
        {
            'id': 1,
            'type': 'Kamion',
            'manufacturer': 'MAN',
            'licence_plate': 'ZP1998MAN',
            'year_of_licence': 1919,
            'price': 300_000.00,
            'used_by': 'Pero'
        },
        {
            'id': 2,
            'type': 'Kamion',
            'manufacturer': 'MAN',
            'licence_plate': 'ZP1999MAN',
            'year_of_licence': 1919,
            'price': 300_000.00,
            'used_by': 'Ivo'
        },
        {
            'id': 3,
            'type': 'Kamion',
            'manufacturer': 'MAN',
            'licence_plate': 'ZP2000MAN',
            'year_of_licence': 1919,
            'price': 300_000.00,
            'used_by': 'Ana'
        }
    ],
    'employees': [
        {
            'id': 1,
            'first_name': 'Pero',
            'last_name': 'Peric',
            'user': 'korisnik_1',
            'password': 'korisnik_1'
        },
        {
            'id': 2,
            'first_name': 'Ana',
            'last_name': 'Anic',
            'user': 'korisnik_2',
            'password': 'korisnik_2'
        },
        {
            'id': 3,
            'first_name': 'Ivo',
            'last_name': 'Ivic',
            'user': 'korisnik_3',
            'password': 'korisnik_3'
        }
    ]
}

#endregion

while True:
    print()
    print('Prijava korisnika u aplikaciju')
    print()
    user_name = input('Upisite korisnicko ime: ')
    user_pasw = input('Upisite lozinku: ')

    user_num = company['employees'][-1]['id']
    for employee in range(user_num):

        if user_name == company['employees'][employee]['user'] and user_pasw == company['employees'][employee]['password']:
            message = f'Dobro dosli {company['employees'][employee]['first_name']} {company['employees'][employee]['last_name']}!'
            print(f'{message}')
            input('Za nastavak pritisnite tipku ENTER')
            #continue
        #else:
            # print('Pogresan unos.')
            # next_login = input('')
    

# glavni dio programa
            while True:
            # DZ - simulirati prijavu korisnika u sustav HINT: nekako, negdje cuvati password svakog korisnika
            # DZ - promijeniti podatke o vozilu tako da umjesto is_operational imate used_by i povezati s korisnikom
            #       HINT: Osmislite prikaz punog imena korisnika -> full_name

                os.system('cls')
            # MAIN MENU
                print()
                print('\tPy Fleet Management')
                print()
                print(f'Firma: {company['name']}')
                print(f'Korisnik: {company["employees"][0]['last_name']}')
                print()
                print('1. Ispis svih vozila')
                print('2. Unos novog vozila')
                # DZ
                print('3. Ispis svih djelatnika')
                print('4. Unos novog djelatnika')

                print('0. Izlaz')
                print()

                menu_item = int(input('Izberite jednu opciju iz izbornika: '))

                if menu_item == 0:
                    break
                elif menu_item == 1:
                    #region DISPLAY ALL VEHICLES
                    print(f"|{'ID':<4}|", end='')
                    print(f"{'Tip':<15}|", end='')
                    print(f"{'Proizvodac':<25}|", end='')
                    print(f"{'Reg. oznaka':<20}|", end='')
                    print(f"{'Godina reg.':<20}|", end='')
                    print(f"{'Korisnik':<12}|", end='')
                    print(f"{'Cijena (EUR)':>22}|")
                    print('-'*126)
                    
                    for vehicle in company['vehicles']:
                        print(f"|{vehicle['id']:<4}|", end='')
                        print(f"{vehicle['type']:<15}|", end='')
                        print(f"{vehicle['manufacturer']:<25}|", end='')
                        print(f"{vehicle['licence_plate']:<20}|", end='')
                        print(f"{vehicle['year_of_licence']:<20}|", end='')
                        vehicle_num = company['vehicles'][-1]['id']
                        #for vehicle in range(vehicle_num):
                        user = company['employees'][-1]['id']
                        for employee in range(user):
                            if vehicle['used_by'] == company['employees'][employee]['first_name']:
                                message_used = f'{company['employees'][employee]['first_name']} {company['employees'][employee]['last_name']}'
                                print(message_used)
                            
                        print(f"{vehicle['price']:>20.3f} €|")
                    
                    print('-'*126)
                    print()
                    # Privremeno zaustavi izvrsavanje programa dok god korisnike ne pritisne tipku ENTER
                    # Moze biti proivoljno vrijeme cekanja, dok time.spleep(sec=) zahtijeva fiksni broj sekundi
                    input('Za nastavak pritisnite tipku ENTER')
                    #endregion
                elif menu_item == 2:
                    #region ADD NEW VEHICLE
                    while True:
                        #region OPIS
                        # vehicles = company['vehicles']
                        # next_vehicle_id = len(vehicles) + 1
                        # next_vehicle_id = len(company['vehicles']) + 1
                        
                        # company['vehicles'][1]['id'] opis:
                        # iz rjecnika company pod kljucem 'vehicles' dohvati mi tu vrijednost -> lista
                        # iz tako dobivene liste uzmem element pod indexom 1 -> dobit cu opet rjecnik
                        # is ovog novog rjecnika dohvati vrijednost pod kljucem 'id' -> int (2)
                        # next_vehicle_id = company['vehicles'][1]['id'] + 1
                        # pokriva sve slucajeve jer dohvaca ZADNJI element liste
                        #endregion
                        vehicle = {}

                        # next_vehicle_id = company['vehicles'][-1]['id'] + 1
                        # vehicle['id'] = next_vehicle_id
                        # ili
                        vehicle['id'] = company['vehicles'][-1]['id'] + 1
                        vehicle['type'] = input('Upisite tip vozila: ')
                        vehicle['manufacturer'] = input('Upisite proizvodaca vozila: ')
                        vehicle['licence_plate'] = input('Upisite reg. oznaku vozila: ')
                        vehicle['year_of_licence'] = input('Upisite godinu 1. registracije vozila: ')
                        vehicle['price'] = float(input('Upisite cijenu vozila u EUR: '))
                        # vehicle['is_operational'] = input('Upisite moze li se vozilo koristiti? (Da/Ne): ')
                        vehicle['used_by'] = input('Upisite ime korisnika vozila: ')
                        #if is_operational.lower() == 'da':
                        #    vehicle['is_operational'] = True
                        #else:
                            #vehicle['is_operational'] = False

                        company['vehicles'].append(vehicle)

                        
                        next_entry = input('Novi unos? (Da/Ne): ')
                        if next_entry.lower() != 'da':
                            break
                    #endregion
                elif menu_item == 3:
                    #region Ispis svih djelatnika
                    print()
                    print(f"|{'ID':<4}|", end='')
                    print(f"{'IME':<15}|", end='')
                    print(f"{'PREZIME':<15}|")
                    print('-'*40)

                    for employee in company['employees']:
                        print(f"|{employee['id']:<4}|", end='')
                        print(f"{employee['first_name']:<15}|", end='')
                        print(f"{employee['last_name']:<15}|")
                    
                    print('-'*40)
                    print()
                    input('Za nastavak pritisnite tipku ENTER')
                    #endregion
                elif menu_item == 4:
                    #region Unos novog korisnika
                    while True:
                        employee = {}

                        # next_vehicle_id = company['vehicles'][-1]['id'] + 1
                        # vehicle['id'] = next_vehicle_id
                        # ili
                        employee['id'] = company['employees'][-1]['id'] + 1
                        employee['first_name'] = input('Upisite ime korisnika: ')
                        employee['last_name'] = input('Upisite prezime korisnika: ')
                        employee['user'] = input('Upisite korisnicko ime: ')
                        employee['pasword'] = input('Upisite lozinku korisnika: ')
                        
                        company['employees'].append(employee)

                        next_entry = input('Novi unos? (Da/Ne): ')
                        if next_entry.lower() != 'da':
                            break
                    #endregion

        #else:
            #print('Pogresan unos.')
            #break
    break       
# Zavrsetak izvrsavanja programa
print()
print('Pozdrav!')
print()