def same_char_collapse(str):
    # your code here
    collapsable = True

    while collapsable:
        collapsable = False

        for idx in range(len(str)-1):
            if str[idx] != str[idx+1]:
                continue
            str = str[:idx] + str[idx+2:]
            collapsable = True
            break
    
    return str


print(same_char_collapse("zzzxaaxy"))   # "zy"
# because zzzxaaxy -> zxaaxy -> zxxy -> zy
print(same_char_collapse("uqrssrqvtt")) # "uv"
# because uqrssrqvtt -> uqrrqvtt -> uqqvtt -> uvtt -> uv