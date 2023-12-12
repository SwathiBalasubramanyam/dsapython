def double_letter_count(string):
    # your code here
    cnt = 0

    for word in string.split(" "):

        for idx, char in enumerate(word):
            if idx == len(word)-1:
                continue
            
            if char == word[idx+1]:
                cnt += 1

    return cnt            


print(double_letter_count("the jeep rolled down the hill")) # 3
print(double_letter_count("bootcamp")) # 1