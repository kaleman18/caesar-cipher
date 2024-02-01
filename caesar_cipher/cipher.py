import nltk

def encrypt(plain, shift):
    encrypted_text = ""

    number_of_characters = 26

    for char in plain:
        if char.isalpha():
            base_code = ord('A') if char.isupper() else ord('a')
            current_code = ord(char)
            current_position = current_code - base_code
            shifted_position = (current_position + shift) % number_of_characters
            shifted_char = base_code + shifted_position
            encrypted_text += chr(shifted_char)
        else:
            encrypted_text += char

    return encrypted_text

def decrypt(encoded, shift):
    return encrypt(encoded, -shift)


if __name__ == "__main__":
    pins = [
        "AAAA",
        "BBBB",
        "ABCD",
        "ABAB",
    ]

    for i, pin in enumerate(pins):
        shift = i + 1
        print("plain pin", pin)
        print("shift by", shift)
        encrypted_pin = encrypt(pin, shift)
        print("encrypted_pin", encrypted_pin)
        decrypted_pin = decrypt(encrypted_pin, shift)
        print("decrypted_pin", decrypted_pin)
        print()

def crack():
