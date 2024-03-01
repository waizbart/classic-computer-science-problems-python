notes_values = {
    'B#': 0, # 'C'
    'C': 0,
    'C#': 1,
    'Db': 1, # 'C#'
    'D': 2,
    'D#': 3,
    'Eb': 3, # 'D#'
    'E': 4,
    'Fb': 4, # 'E'
    'E#': 5, # 'F'
    'F': 5,
    'F#': 6,
    'Gb': 6, # 'F#'
    'G': 7,
    'G#': 8,
    'Ab': 8, # 'G#
    'A': 9,
    'A#': 10,
    'Bb': 10, # 'A#'
    'B': 11,
    'Cb': 11 # 'B
}

while True:
    n_original, n_suspicious = map(int, input().split())
    
    if n_original == 0 and n_suspicious == 0:
        break
    
    original_song = input().split()
    suspicious_song = input().split()
    
    original_intervals = []
    suspicious_intervals = []
    
    for i in range(n_original - 1):
        note = original_song[i]
        next_note = original_song[i + 1]
            
        note_value = notes_values[note]
        next_value = notes_values[next_note]
        
        if note_value > next_value:
            value = note_value - (note_value - next_value) + 1
        else:
            value = next_value - note_value     
        
        original_intervals.append(value)
    
    for j in range(n_suspicious - 1):
        note = suspicious_song[j]
        next_note = suspicious_song[j + 1]
            
        note_value = notes_values[note]
        next_value = notes_values[next_note]
        
        if note_value > next_value:
            value = note_value - (note_value - next_value) + 1
        else:
            value = next_value - note_value    
            
        suspicious_intervals.append(value)
    
    str_original = "".join(map(str, original_intervals))
    str_suspicious = "".join(map(str, suspicious_intervals))
    
    print(original_intervals)
    print(suspicious_intervals)
        
    if str_suspicious in str_original:
        print('S')
    else:
        print('N')
        
