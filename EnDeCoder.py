import random




#TODO change this data to individual characters instead of a=m, b=n, etc.
char_data = {
    # a-z
    'a': 'm', 'b': 'n', 'c': 'b', 'd': 'v', 'e': 'c', 'f': 'x',
    'g': 'z', 'h': 'l', 'i': 'k', 'j': 'j', 'k': 'h', 'l': 'g',
    'm': 'f', 'n': 'd', 'o': 's', 'p': 'a', 'q': 'p', 'r': 'o',
    's': 'i', 't': 'u', 'u': 'y', 'v': 't', 'w': 'r', 'x': 'e',
    'y': 'w', 'z': 'q',
    
    # A-Z
    'A': 'M', 'B': 'N', 'C': 'B', 'D': 'V', 'E': 'C', 'F': 'X',
    'G': 'Z', 'H': 'L', 'I': 'K', 'J': 'J', 'K': 'H', 'L': 'G',
    'M': 'F', 'N': 'D', 'O': 'S', 'P': 'A', 'Q': 'P', 'R': 'O',
    'S': 'I', 'T': 'U', 'U': 'Y', 'V': 'T', 'W': 'R', 'X': 'E',
    'Y': 'W', 'Z': 'Q',

    # 0-9
    '1': '0', '2': '9', '3': '8', '4': '7', '5': '6', '6': '5',
    '7': '4', '8': '3', '9': '2', '0': '1'
}


class EnDeCoder:
    def __init__(self):
        pass


    def generate_key(self, length=32):
        return ''.join(random.choices(list(char_data.keys()), k=length))


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




# Example
if __name__ == "__main__":
    endecoder = EnDeCoder()

    data = "example_data"

    key = endecoder.generate_key()
    encoded_data = endecoder.encode(data, key)
    decoded_data = endecoder.decode(encoded_data, key)

    print(f"Data: {data}")
    print(f"Key: {key}")
    print(f"Encoded Data: {encoded_data}")
    print(f"Decoded Data: {decoded_data}")