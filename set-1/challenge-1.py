from binascii import unhexlify
import base64

def hex_to_base64(string):
    # print(string)
    # Convert from hexadecimal (2 digit values) to ASCII
    ascii_byte_str = unhexlify(string)
    
    # print(ascii_byte_str)
    # Convert from ASCII to 64-bit byte string, return
    return base64.b64encode(ascii_byte_str)
    
    # If needed to convert byte string to ASCII string
    # return byte_str.decode('ASCII')


print(hex_to_base64('49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d'))
