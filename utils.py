def gen_table():
    table = {}
    count = 0
    for i in range(26):
        table[count] = chr(i + 65)
        count += 1
    for i in range(26):
        table[count] = chr(i + 97)
        count += 1
    for i in range(10):
        table[count] = str(i)
        count += 1
    table[count] = "+"
    table[count+1] = "/"
    return table


def gen_revtable(table):
    rev = {}
    for key in table:
        rev[table[key]] = key
    return rev

TABLE = gen_table()
revTABLE = gen_revtable(TABLE)
# print(TABLE)
# print(revTABLE)

