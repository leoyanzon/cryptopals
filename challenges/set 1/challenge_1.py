import base64

def hex_to_base64(input):
    input_bytes = bytes.fromhex(input)
    output_base64 = base64.b64encode(input_bytes).decode()
    return output_base64

hex_string = "49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d"

if __name__ == "__main__":
    print(hex_to_base64(hex_string))