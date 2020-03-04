from utils import revTABLE


def base642binary(c):
    o = revTABLE[c]
    # print(o)
    b = format(o, "06b")
    # print(b)
    return b


def base64decoder(s):
    bin_s = ""
    for elem in s:
        if elem == "=":
            break
        bin_s += str(base642binary(elem))
    num_s = len(bin_s) // 8
    res = ""
    for i in range(num_s):
        c = chr(int(bin_s[i * 8: i * 8 + 8], 2))
        # print(c)
        res += c
    return res




if __name__ == "__main__":
    base64decoder("QUJDREVGRw==")

    
