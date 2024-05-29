morse_encode_dict = {
    'A': '.-', 'B': '-...', 'C': '-.-.',
    'D': '-..', 'E': '.', 'F': '..-.',
    'G': '--.', 'H': '....', 'I': '..',
    'J': '.---', 'K': '-.-', 'L': '.-..',
    'M': '--', 'N': '-.', 'O': '---',
    'P': '.--.', 'Q': '--.-', 'R': '.-.',
    'S': '...', 'T': '-', 'U': '..-',
    'V': '...-', 'W': '.--', 'X': '-..-',
    'Y': '-.--', 'Z': '--..',
    '0': '-----', '1': '.----', '2': '..---',
    '3': '...--', '4': '....-', '5': '.....',
    '6': '-....', '7': '--...', '8': '---..',
    '9': '----.'
}
morse_decode_dict = {".-": "A", "-...": "B", "-.-.": "C",
                     "-..": "D", ".": "E", "..-.": "F",
                     "--.": "G", "....": "H", "..": "I",
                     ".---": "J", "-.-": "K", ".-..": "L",
                     "--": "M", "-.": "N", "---": "O",
                     ".--.": "P", "--.-": "Q", ".-.": "R",
                     "...": "S", "-": "T", "..-": "U",
                     "...-": "V", ".--": "W", "-..-": "X",
                     "-.--": "Y", "--..": "Z",
                     "-----": "0", ".----": "1", "..---": "2",
                     "...--": "3", "....-": "4", ".....": "5",
                     "-....": "6", "--...": "7", "---..": "8",
                     "----.": "9"}

encrypted_message = []
decrypted_message = []
text = input('Enter message to encrypt: ').upper().split()

for word in text:
    for letter in word:
        if letter in morse_encode_dict.keys():
            encrypted_message.append(morse_encode_dict[letter])

print(encrypted_message)

for letter in encrypted_message:
    decrypted_message.append(morse_decode_dict[letter])

print(decrypted_message)
