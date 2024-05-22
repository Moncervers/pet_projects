alphabet = [chr(i) for i in range(97, 123)]  # TODO add capitals, commas, etc
cyphered_message = []

# Encrypter
message = list(input('Введите сообщение: ').lower().split())
key = int(input('Введите шаг: '))

for word in message:
    cyphered_word = ''

    for letter in word:
        index = alphabet.index(letter)
        cyphered_word += alphabet[(index + key) % len(alphabet)]

    cyphered_message.append(cyphered_word)

print(' '.join(cyphered_message))
print('\n\n\n')

# Decrypter
message = list(input('Введите зашифрованное сообщение: ').lower().split())

for key in range(1, 26):
    deciphered_message = []

    for word in message:
        deciphered_word = ''

        for letter in word:
            index = alphabet.index(letter)
            deciphered_word += alphabet[(index - key) % len(alphabet)]

        deciphered_message.append(deciphered_word)

    deciphered_message = ' '.join(deciphered_message)
    print(f'{deciphered_message}  шаг: {key}')
