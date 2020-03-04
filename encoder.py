from utils import TABLE


def hex2binary(h):
    """
    convet hex to binary
    """
    # print(h)
    # print(format(int(h, 0), '08b'))
    return format(int(h, 0), '08b') 
    

def int2base64(n):
    assert n < 64 and n >= 0, "n must be 0 to 64"
    return TABLE[n]

def base64encoder(s):
    if (s == ""):
        return ""
    bit_s = ""
    for elem in s:
        ascii_c = hex(ord(elem))
        #print(ascii_c)
        bit_s += str(hex2binary(ascii_c))
        
    res = ""
    for i in range(0, len(bit_s), 6):
        bit_cur = bit_s[i:i+6]
        if (len(bit_cur) < 6):
            bit_cur = bit_cur + "0" * (6 - len(bit_cur))
        ascii_r = int2base64(int(bit_cur, 2))
        res += ascii_r
    res = res + "=" * (4 - len(res) % 4)
    # print(res)
    return res
    
        



if __name__ == "__main__":
    base64encoder("ABCDEFG")
