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

tones = ['C', 'C#', 'D', 'D#', 'E','F', 'F#', 'G', 'G#', 'A', 'A#', 'H']

print()
print('********')
start_tone = input('Upisite ton za koji zelite saznati sasatv durskog i molskog akorda: ')
#for i in tones:
tone_index = tones.index(start_tone,0,12)
if tone_index + 4 >= len(tones):
    dur_1 = tones[tone_index + 4 - len(tones)]
    dur_2 = tones[tone_index + 7 - len(tones)]
    mol_1 = tones[tone_index + 3 - len(tones)]
    mol_2 = tones[tone_index + 7 - len(tones)]
elif tone_index + 7 >= len(tones):
    dur_1 = tones[tone_index + 4]
    dur_2 = tones[tone_index + 7 - len(tones)]
    mol_1 = tones[tone_index + 3]
else:
    dur_1 = tones[tone_index + 4]
    dur_2 = tones[tone_index + 7]
    mol_1 = tones[tone_index + 3]

print()
print(f'{tones[tone_index].upper()} -> {tones[tone_index].upper()}, {dur_1}, {dur_2}')
print(f'{tones[tone_index].lower()} -> {tones[tone_index].upper()}, {mol_1}, {dur_2}')

print()

#print(dur_1, dur_2)
#print(mol_1, mol_2)
#print(index)
#if len(tones)-tones[index]