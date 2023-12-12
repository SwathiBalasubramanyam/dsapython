#HINT: use a dictionary
def frequent_letters(string):
    # your code here
    from collections import defaultdict
    char_cnt = defaultdict(int)
    lst = []

    for char in string:
        char_cnt[char] += 1
        if char_cnt[char] > 2 and char not in lst:
            lst.append(char)

    return lst
    
print(frequent_letters("mississippi")) #["i", "s"]
print(frequent_letters("bootcamp")) #[]