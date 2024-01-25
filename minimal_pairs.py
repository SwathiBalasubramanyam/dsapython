



def minimalOperations(words):
    # Write your code here
    
    res_arr = []
    for word in words:

        last_char = word[0]
        changes = 0
        idx = 1

        while idx < len(word):
            if word[idx] == last_char:
                changes += 1
                while idx < len(word) and word[idx] == last_char:
                    idx += 1
            else:
                last_char = word[idx]
                idx += 1

        res_arr.append(changes)

    return res_arr

print(minimalOperations(["abaaaba"]))