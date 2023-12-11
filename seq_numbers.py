# Write your function, here.
# There are hints after the print statements

def seq_of_numbers(str):

    current_char = str[0]
    current_count = 1

    count_to_word = {
        1: "one",
        2: "two",
        3: "three"
    }

    ans_seq = ""

    for idx in range(1, len(str)):
        if str[idx] == current_char:
            current_count += 1
            continue
        
        ans_seq += f'{count_to_word[current_count]} {current_char}, '

        current_char = str[idx]
        current_count = 1

    ans_seq += f'{count_to_word[current_count]} {current_char}'

    return ans_seq


print(seq_of_numbers("1211"))
# This is "one 1, one 2, two 1s"
# Prints "111221"

print(seq_of_numbers("111221"))
# This is "three 1s, two 2s, and one 1"
# Prints "312211"

print(seq_of_numbers("31131211131221"))
# This is "one 3, two 1s, one 3, one 1, one 2, three 1s,
#    one 3, one 1, two 2s, and one 1"
# Prints "13211311123113112211"





###########################################################
# AN ALGORITHM
# An algorithm for performing this without a data structure
# means you have to think about what you're trying to look
# for.
#
# If you scan the string two characters at a time, when they
# change, you know that you have started a new sequence of
# numbers. You can add the current number of characters that
# you've scanned to a result.
#
# For example, say you had "111221". You would start the
# count at 1 and compare the characters at indices 0 and 1.
# Since they are the same, you would increment the current
# count to two, because you will have found two 1s. Then,
# you would compare the characters at indices 1 and 2.
# Again, they are both 1s, so you would increment the count
# to 3. The next comparison, the one at indices 2 and 3
# yields the characters "1" and "2". At this point, the
# characters have changed. The current count is 3, and the
# current character is "1", so you would concatenate those
# onto a result "31". Then, you would set the current count
# back to 1 (because you have found one 2), and continue
# with the same process.


############################################################
# PSEUDOCODE
#
# Concatenate an empty space to the end of the value passed
#    into the function. This will let you compare the entire
#    length of the original string with a guarantee that the
#    two last characters do not match.
# Create an empty string to which you will append the
#    counts and digits
# Initialize an index to 0 for looping over the string
# Initialize a counter variable to record the count of the
#    current character
# Using the index variable, loop from 0 to the length of the
#    string minus 1 (because you don't want to examine the
#    last character, the space that you added)
#   If the current character is not equal to the next
#      character, then concatenate the current count and the
#      current character to the result string and set the
#      current count back to 1
#   Otherwise, just increment the current character count by
#      1
#   Increment the index by 1
# Return the result