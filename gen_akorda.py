'''U zasebnom repozitoriju generator akorda (ili proizvoljnog naziva) kreirajte aplikaciju
koja ce omoguciti korisniku da unese pocetni ton akorda za koji mu treba vratiti tri tona 
od kojih se sastoji durski i molski akord. 
Oktavu cine tonovi (po njemackoj notaciji)>

0, 1,  2, 3,  4, 5, 6,  7, 8,  9, 10, 11
C, C#, D, D#, E, F, F#, G, G#, A, A#, H
Durski akordi se sastoje od pocetnog tona, cetvrtog i sedmog

Primjer:
D
D dur (0, 4, 7) ili se pise samo D -> D, F#, A
D mol (0, 3, 7) ili se pise samo d -> D, F, A

H -> H, D#, F#
h -> H, D, F#'''

import os

tones = ['C', 'C#', 'D', 'D#', 'E','F', 'F#', 'G', 'G#', 'A', 'A#', 'H']

low_tones = []
while True:

    os.system('cls')
    print()
    print('# '*20)
    print()
    print('\tGenerator akorda')
    print()
    print('Ljestvica: ', end="")
    for tone in range(len(tones)):
        print(tones[tone], end=" ")
    print()
    print()

    start_tone = input('Upisite ton iz ljestvice za koji zelite saznati tonove durskog i molskog akorda: ')
    start_tone = start_tone.lower()
    for tone in tones:
        tone = tone.lower()
        
        low_tones.append(tone)

    if low_tones.count(start_tone) == 0:
        print('Niste unijeli odgovarajući ton. Molimo ponovite unos.')
        input('Za nastavak pritisnite ENTER.')
        continue
    else:
        tone_index = low_tones.index(start_tone,0,12)
    if tone_index + 4 > len(tones):
        major_1 = tones[tone_index + 4 - len(tones)]
        major_2 = tones[tone_index + 7 - len(tones)]
        minor_1 = tones[tone_index + 3 - len(tones)]
            
    elif tone_index + 7 >=len(tones):
        major_1 = tones[tone_index + 4]
        major_2 = tones[tone_index + 7 - len(tones)]
        minor_1 = tones[tone_index + 3]

    elif tone_index < 5:
        major_1 = tones[tone_index + 4]
        major_2 = tones[tone_index + 7]
        minor_1 = tones[tone_index + 3]
        
    print()
    print(f'{tones[tone_index].upper()} -> {tones[tone_index].upper()}, {major_1}, {major_2}')
    print(f'{tones[tone_index].lower()} -> {tones[tone_index].upper()}, {minor_1}, {major_2}')
    print()
        
    new_chord = input('Zelite li ispis novog akorda? (Da/Ne): ')
    if new_chord.lower() != 'da':
        break
print()
print('Pozdrav, ugodno muziciranje!')
print()
