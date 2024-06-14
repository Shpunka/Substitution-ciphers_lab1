def encrypt(message, key):
    message = message.lower()
    encrypted_message = ''
    for char in message:
        if char in key:
            encrypted_message += key[char]
        else:
            encrypted_message += char
    return encrypted_message


def decrypt(encrypted_message, key):
    decryption_key = {value: key for key, value in key.items()}
    decrypted_message = ''
    for char in encrypted_message:
        if char in decryption_key:
            decrypted_message += decryption_key[char]
        else:
            decrypted_message += char
    return decrypted_message


encryption_key = {'a': 'q', 'b': 'w', 'c': 'e', 'd': 'r', 'e': 't',
                  'f': 'y', 'g': 'u', 'h': 'i', 'i': 'o', 'j': 'p',
                  'k': 'a', 'l': 's', 'm': 'd', 'n': 'f', 'o': 'g',
                  'p': 'h', 'q': 'j', 'r': 'k', 's': 'l', 't': 'z',
                  'u': 'x', 'v': 'c', 'w': 'v', 'x': 'b', 'y': 'n', 'z': 'm'}

message = 'cryptography'




encrypted_message = encrypt(message, encryption_key)
print("Encrypted message:\n ", encrypted_message)

decrypted_message = decrypt(encrypted_message, encryption_key)
print("\nDecrypted message:\n ", decrypted_message)
