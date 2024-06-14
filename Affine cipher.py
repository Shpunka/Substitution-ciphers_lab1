import math


def encode(target, alphabet, a, b):
    target = target.lower()
    alphabet = alphabet.lower()
    if math.gcd(len(alphabet), a) == 1:
        encode_message = ''
        for i in range(len(target)):
            for j in range(len(alphabet)):
                if target[i] not in alphabet:
                    encode_message += target[i]
                    break
                if target[i] == alphabet[j]:
                    char = (a * j + b) % len(alphabet)
                    encode_message += alphabet[char]
                    break
        return encode_message
    else:
        return None

message = 'crypto'
message = encode(message, 'abcdefghijklmnopqrstuvwxyz', 7, 3)
print(message)


def decode(target, alphabet, a, b):
    # найдем a^-1
    for i in range(len(alphabet)):
        if (a * i) % len(alphabet) == 1:
            a1 = i
    target = target.lower()
    alphabet = alphabet.lower()
    decode_message = ''
    if math.gcd(len(alphabet), a) == 1:
        for i in range(len(target)):
            for j in range(len(alphabet)):
                if target[i] not in alphabet:
                    decode_message += target[i]
                    break
                if target[i] == alphabet[j]:
                    char = ((j - b) * a1) % len(alphabet)
                    decode_message += alphabet[char]
                    break
        return decode_message


message = decode('rspegx', 'abcdefghijklmnopqrstuvwxyz', 7, 3)
print(message)
