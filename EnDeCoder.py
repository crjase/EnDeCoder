class Operation:
    def __init__(self):

        # Define the encoding dictionary
        self.encode_map = {
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
        # Create reverse map for decoding
        self.decode_map = {value: key for key, value in self.encode_map.items()}


    def encode(self, text: str) -> str:
        encoded_text = ""
        for char in text.lower():  # Convert all characters to lowercase for encoding
            if char in self.encode_map:
                encoded_text += self.encode_map[char]
            else:
                # Foreign symbols can be left as-is
                encoded_text += char

        return encoded_text


    def decode(self, text: str) -> str:
        decoded_text = ""
        for char in text:
            if char in self.decode_map:
                decoded_text += self.decode_map[char]
            else:
                # Foreign symbols can be left as-is
                decoded_text += char

        return decoded_text
