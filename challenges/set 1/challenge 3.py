import string

def scoring(plaintext):
    allowed = string.ascii_letters + string.digits + ' '
    score = sum(char in allowed for char in plaintext)
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
        ascii = chr(int(xored,16))
        plaintext += ascii
    return plaintext

def __main__(input):
    score_matrix = [] 
    for x in range(0,255):
        hex_iterator = format(x, '02X')
        xored_plaintext = xor_plaintext_with_hex(input, hex_iterator)
        score = scoring(xored_plaintext)
        score_matrix.append(score)
    solution_index = score_matrix.index(max(score_matrix))
    return xor_plaintext_with_hex(input, format(solution_index, '02X'))

print(__main__("1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736"))