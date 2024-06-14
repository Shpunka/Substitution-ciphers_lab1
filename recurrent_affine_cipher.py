alphabet = 'abcdefghijklmnopqrstuvwxyz'


def encode(alphabet, message, a1, a2, b1, b2):
    encode_message = ''
    message.lower()
    encode_message += alphabet[(alphabet.index(message[0]) * a1 + b1) % len(alphabet)]
    encode_message += alphabet[(alphabet.index(message[1]) * a2 + b2) % len(alphabet)]
    a = [a1, a2]
    b = [b1, b2]
    for i in range(2, len(message)):
        if message[i] in alphabet:
            a.append((a[-1] * a[-2]) % len(alphabet))
            b.append((b[-1] + b[-2]) % len(alphabet))
            encode_message += alphabet[(alphabet.index(message[i]) * a[-1] + b[-1]) % len(alphabet)]
        else:
            encode_message += message[i]
    return encode_message


message = 'cyrptography'

print(encode(alphabet, message, 3, 5, 8, 9))


def custom_decrypt(message, key, alphabet):
    original_message = ''
    multiplier = [int(key[0]), int(key[2])]
    shift = [int(key[1]), int(key[3])]

    for i in range(2):
        num = 1
        while num % multiplier[i] != 0:
            num += 26
        multiplier[i] = num // multiplier[i]

    original_message += alphabet[((alphabet.index(message[0]) - shift[0]) * multiplier[0]) % 26]
    original_message += alphabet[((alphabet.index(message[1]) - shift[1]) * multiplier[1]) % 26]

    for i in range(2, len(message)):
        if message[i] in alphabet:
            multiplier.append((multiplier[-1] * multiplier[-2]) % 26)
            shift.append((shift[-1] + shift[-2]) % 26)
            char_index = ((alphabet.index(message[i]) - shift[-1]) * multiplier[-1]) % 26
            original_message += alphabet[char_index]
        else:
            original_message += message[i]
    return original_message


def brute_force_decrypt(ciphertext, alphabet):
    decrypted_messages = []
    for a1 in range(26):
        for a2 in range(26):
            for b1 in range(26):
                for b2 in range(26):
                    key = [a1, b1, a2, b2]
                    decrypted_message = custom_decrypt(ciphertext, key, alphabet)
                    decrypted_messages.append((decrypted_message, key))
    return decrypted_messages


print(custom_decrypt('oqnhujkkhrmp', [3, 8, 5, 9], alphabet))
