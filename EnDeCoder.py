import random




characters = [
    # a-z
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
    'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',

    # A-Z
    'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
    'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z',

    # 0-9
    '0', '1', '2', '3', '4', '5', '6', '7', '8', '9'
]


class EnDeCoder:
    def __init__(self):
        pass


    def generate_key(self, length=32):
        return ''.join(random.choices(characters, k=length))


    def encode(self, data, key):
        encoded_chars = []
        for i in range(len(data)):
            key_c = key[i % len(key)]
            encoded_c = chr((ord(data[i]) + ord(key_c)) % 256)
            encoded_chars.append(encoded_c)
        encoded_string = ''.join(encoded_chars)
        return encoded_string


    def decode(self, encoded_data, key):
        decoded_chars = []
        for i in range(len(encoded_data)):
            key_c = key[i % len(key)]
            decoded_c = chr((ord(encoded_data[i]) - ord(key_c)) % 256)
            decoded_chars.append(decoded_c)
        decoded_string = ''.join(decoded_chars)
        return decoded_string




if __name__ == "__main__":
    print("This is not an executable file. Please import this file in your project.")
