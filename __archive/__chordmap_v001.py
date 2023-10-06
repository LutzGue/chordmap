import json

# Define a mapping for A Major scale
roman_mapping = {
    'A': 'I',
    'B': 'ii',
    'C#': 'iii',
    'D': 'IV',
    'E': 'V',
    'F#': 'vi',
    'G#': 'vii°'
}

# Define a mapping for all Major keys
"""
roman_mapping = {
    'Cb': [{'Cb': 'I'}, {'Dbm': 'ii'}, {'Ebm': 'iii'}, {'Fb': 'IV'}, {'Gb': 'V'}, {'Abm': 'vi'}, {'Bbdim': 'vii°'}, 
           {'CbMaj7': 'IMaj7'}, {'Dbm7': 'ii7'}, {'Ebm7': 'iii7'}, {'FbMaj7': 'IVMaj7'}, {'Gb7': 'V7'}, {'Abm7': 'vi7'}, {'Bbdim7': 'vii°7'}],
    'Gb': [{'Gb': 'I'}, {'Abm': 'ii'}, {'Bbm': 'iii'}, {'Cb': 'IV'}, {'Db': 'V'}, {'Ebm': 'vi'}, {'Fdim': 'vii°'},
           {'GbMaj7': 'IMaj7'}, {'Abm7': 'ii7'}, {'Bbm7': 'iii7'}, {'CbMaj7': 'IVMaj7'}, {'Db7': 'V7'}, {'Ebm7': 'vi7'}, {'Fdim7': 'vii°7'}],
    'Db': [{'Db': 'I'}, {'Ebm': 'ii'}, {'Fm': 'iii'}, {'Gb': 'IV'}, {'Ab': 'V'}, {'Bbm': 'vi'}, {'Cdim': 'vii°'}],
    'Ab': [{'Ab': 'I'}, {'Bbm': 'ii'}, {'Cm': 'iii'}, {'Db': 'IV'}, {'Eb': 'V'}, {'Fm': 'vi'}, {'Gdim': 'vii°'}],
    'Eb': [{'Eb': 'I'}, {'Fm': 'ii'}, {'Gm': 'iii'}, {'Ab': 'IV'}, {'Bb': 'V'}, {'Cm': 'vi'}, {'Ddim': 'vii°'}],
    'Bb': [{'Bb': 'I'}, {'Cm': 'ii'}, {'Dm': 'iii'}, {'Eb': 'IV'}, {'F': 'V'}, {'Gm': 'vi'}, {'Adim': 'vii°'}],
    'F': [{'F': 'I'}, {'Gm': 'ii'}, {'Am': 'iii'}, {'Bb': 'IV'}, {'C': 'V'}, {'Dm': 'vi'}, {'Edim': 'vii°'}],
    'C': [{'C': 'I'}, {'Dm': 'ii'}, {'Em': 'iii'}, {'F': 'IV'}, {'G': 'V'}, {'Am': 'vi'}, {'Bdim': 'vii°'}],
    'G': [{'G': 'I'}, {'Am': 'ii'}, {'Bm': 'iii'}, {'C': 'IV'}, {'D': 'V'}, {'Em': 'vi'}, {'F#dim': 'vii°'}],
    'D': [{'D': 'I'}, {'Em': 'ii'}, {'F#m': 'iii'}, {'G': 'IV'}, {'A': 'V'}, {'Bm': 'vi'}, {'C#dim': 'vii°'}],
    'A': [{'A': 'I'}, {'Bm': 'ii'}, {'C#m': 'iii'}, {'D': 'IV'}, {'E': 'V'}, {'F#m': 'vi'}, {'G#dim': 'vii°'},
          {'AMaj7': 'IMaj7'}, {'Bm7': 'ii7'}, {'C#m7': 'iii7'}, {'DMaj7': 'IVMaj7'}, {'E7': 'V7'}, {'F#m7': 'vi7'}, {'G#dim7': 'vii°7'}],
    'E': [{'E': 'I'}, {'F#m': 'ii'}, {'G#m': 'iii'}, {'A': 'IV'}, {'B': 'V'}, {'C#m': 'vi'}, {'D#dim': 'vii°'}],
    'B': [{'B': 'I'}, {'C#m': 'ii'}, {'D#m': 'iii'}, {'E': 'IV'}, {'F#': 'V'}, {'G#m': 'vi'}, {'A#dim': 'vii°'}],
    'F#': [{'F#': 'I'}, {'G#m': 'ii'}, {'A#m': 'iii'}, {'B': 'IV'}, {'C#': 'V'}, {'D#m': 'vi'}, {'E#dim': 'vii°'}],
    'C#': [{'C#': 'I'}, {'D#m': 'ii'}, {'E#m': 'iii'}, {'F#': 'IV'}, {'G#': 'V'}, {'A#m': 'vi'}, {'B#dim': 'vii°'}]
}
"""

roman_numerals = ['I', 'II', 'III', 'IV', 'V', 'VI', 'VII']
scale_notes = {
    'Cb': ['Cb', 'Db', 'Eb', 'Fb', 'Gb', 'Ab', 'Bb'],
    'Gb': ['Gb', 'Ab', 'Bb', 'Cb', 'Db', 'Eb', 'F'],
    'A': ['A', 'B', 'C#', 'D', 'E', 'F#', 'G#']}
diatonic_triad = ['', 'm', 'm', '', '', 'm', 'dim']
diatonic_seventh = ['Maj7','m7','m7','Maj7','7','m7','dim7']
diatonic_ninth = ['Maj9','m9','m9','Maj9','9','m9','dim9']

roman_mapping = {}

for key, scales in scale_notes.items():
    roman_mapping[key] = []
    for i in range(len(scales)):
        roman_mapping[key].append({scales[i] + diatonic_triad[i]: roman_numerals[i] + diatonic_triad[i]})
        roman_mapping[key].append({scales[i] + diatonic_seventh[i]: roman_numerals[i] + diatonic_seventh[i] })
        roman_mapping[key].append({scales[i] + diatonic_ninth[i]: roman_numerals[i] + diatonic_ninth[i] })

print(roman_mapping)

# Load JSON data from a file
with open('json\\song1.json', 'r') as f:
    data = json.load(f)

# Iterate over each section
for section in data[0]['data']['section']:
    # Check if the key is in the mapping
    if section['key']['note'] in roman_mapping and section['key']['mode'] == "Major":
        # Iterate over each chord
        for chord in section['chord']:
            # Map the note to roman numeral
            for mapping in roman_mapping[section['key']['note']]:
                if chord['note'] in mapping:
                    chord['map'] = mapping[chord['note']]

print(json.dumps(data, indent=4))