
class Solution:
    def replaceWords(self, dictionary, sentence):
        new_words = []

        for word in sentence.split(" "):
            root = None 
            for possible_root in dictionary:
                if word.startswith(possible_root):
                    if not root:
                        root = possible_root
                    elif len(possible_root) < len(root):
                        root = possible_root

            if not root:
                root = word
            new_words.append(root)

        return " ".join(new_words)


        

print(Solution().replaceWords(["cat","bat","rat"], "the cattle was rattled by the battery"))
# the cat was rat by the bat