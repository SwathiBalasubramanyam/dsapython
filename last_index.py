def last_index(str, char):
    # your code here
    lIdx = len(str) - 1
    return lIdx - str[::-1].index(char)


print(last_index("abca", "a"))        # 3
print(last_index("mississipi", "i"))  # 9
print(last_index("octagon", "o"))     # 5
print(last_index("programming", "m")) # 7
