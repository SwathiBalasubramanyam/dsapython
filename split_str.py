def split_str(input_str):
    res_arr = []
    i = 0

    curr_str = ""

    while i < len(input_str):
        if input_str[i] != "'":
            while i < len(input_str) and input_str[i] != ",":
                curr_str += input_str[i]
                i += 1
        else:
            curr_str += input_str[i]
            i += 1
            while i < len(input_str) and input_str[i] != "'":
                curr_str += input_str[i]
                i += 1
            curr_str += input_str[i]
            i += 1


        res_arr.append(curr_str)
        curr_str = ""
        i += 1

    print(res_arr)

    

