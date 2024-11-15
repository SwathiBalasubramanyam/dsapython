
def split_str(input_str):
    res_arr = []
    curr_str = ""
    while input_str:

        if input_str[0] == "'":
            idx  = input_str[1:].index("'")
            curr_str = input_str[:idx+2]
            input_str = input_str[idx+3:]
        else:
            idx = input_str.index(",") if "," in input_str else len(input_str)
            curr_str = input_str[:idx]
            input_str = input_str[idx+1:]

        res_arr.append(curr_str)
        curr_str = ""

    print(res_arr)


split_str("ab,b,c") # op-> a b c
split_str("a,'b,1',c") # op --> a b,1 c
