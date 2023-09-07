def xor(input1, input2):
    input1_bytes = bytes.fromhex(input1)
    input2_bytes = bytes.fromhex(input2)
    xor_output = (x ^ y for x,y in zip(input1_bytes, input2_bytes))
    output = bytes(xor_output).hex()
    return output

if __name__ == "__main__":
    i1 = "1c0111001f010100061a024b53535009181c"
    i2 = "686974207468652062756c6c277320657965"
    print(xor(i1, i2))