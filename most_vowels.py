from collections import defaultdict

def most_vowels(sentence):
    # your code here
    word_char_cnt = defaultdict(int)

    for word in sentence.split(" "):
        vowel_cnt = len([char for char in word if char in "aeiou"])
        word_char_cnt[word] = vowel_cnt

    return sorted(word_char_cnt.items(), key=lambda item: item[1], reverse=True)[0][0]

print(most_vowels("what a wonderful life")) # "wonderful"