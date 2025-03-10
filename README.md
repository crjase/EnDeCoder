# Functions
EnDeCoder().generate_key(length=32)
<br>
EnDeCoder().encode(data, key)
<br>
EnDeCoder().decode(encoded_data, key)

# Usage
```py
from EnDeCoder import EnDeCoder




# Initialize EnDeCoder
endecoder = EnDeCoder()


data = "example data" # Example data string

key = endecoder.generate_key(length=64) # Generate a random key with 64 characters

encoded_data = endecoder.encode(data, key) # Encode the data using the key above

decoded_data = endecoder.decode(encoded_data, key) # Decode the above encoded data using the same key above
```
This should come without saying; You should always hide the key from view, treat is like a password, because that's what's used to decode the encoded data.
