import string

# http://www.data-compression.com/english.html
CHARACTER_FREQ = {
    'a': 0.0651738, 'b': 0.0124248, 'c': 0.0217339, 'd': 0.0349835, 'e': 0.1041442, 'f': 0.0197881, 'g': 0.0158610,
    'h': 0.0492888, 'i': 0.0558094, 'j': 0.0009033, 'k': 0.0050529, 'l': 0.0331490, 'm': 0.0202124, 'n': 0.0564513,
    'o': 0.0596302, 'p': 0.0137645, 'q': 0.0008606, 'r': 0.0497563, 's': 0.0515760, 't': 0.0729357, 'u': 0.0225134,
    'v': 0.0082903, 'w': 0.0171272, 'x': 0.0013692, 'y': 0.0145984, 'z': 0.0007836, ' ': 0.1918182
}

def get_score(plaintext):
    score = 0
    for char in plaintext:
        score += CHARACTER_FREQ.get(char.lower(), 0)
    return score


def simple_xor(input1, input2):
    input1_bytes = bytes.fromhex(input1)
    input2_bytes = bytes.fromhex(input2)
    xor_output = (x ^ y for x,y in zip(input1_bytes, input2_bytes))
    output = bytes(xor_output).hex()
    return output

def xor_plaintext_with_hex(input, hex):
    plaintext = ""
    for i in range(0, len(input), 2):
        xored = simple_xor(input[i:i+2], hex)
        ascii = chr(int(xored, 16))
        plaintext += ascii
    return plaintext

def brute_force(hex_literal):
    matrix = []
    for x in range(0,255):
        hex_iterator = format(x, '02X')
        xored_plaintext = xor_plaintext_with_hex(hex_literal, hex_iterator)
        matrix.append({
            'key': x,
            'plaintext': xored_plaintext,
            'score': get_score(xored_plaintext)
        })
    
    result = sorted(matrix, key=lambda c: c['score'], reverse=True)[0]
    return result

def main():
    input = "1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736"
    output = brute_force(input)
    print(output['plaintext'])

if __name__ == "__main__":
    main()
