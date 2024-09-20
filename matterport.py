# Your previous Plain Text content is preserved below:

# This is just a simple shared plaintext pad, with no execution capabilities.

# When you know what language you'd like to use for your interview,
# simply choose it from the dots menu on the tab, or add a new language
# tab using the Languages button on the left.

# You can also change the default language your pads are created with
# in your account settings: https://app.coderpad.io/settings

# Enjoy your interview!
#         1
#       2 3 2
#     3 4 5 4 3
# ___ 4_ 5 6 7 6 5 4
# _5_6_7_8_9_8_7_6_5_

# _________1________ ---> 9 space
# _______2_3_2______ ---> 7 space
# _____3_4_5_4_3_____---> 5 space
# ___4_5_6_7_6_5_4___ ---> 3 space
# _5_6_7_8_9_8_7_6_5_ ---> 1 space


# Enjoy your interview!
#         1
#       2 3 2
#     3 4 5 4 3
#   4 5 6 7 6 5 4
# 5 6 7 8 9 8 7 6 5

def print_nums(len_op):
    for i in range(len_op):
        start_num = i
        res_arr = []
        total_nums_row = 2*i+1
        mid_len = total_nums_row // 2

        for j in range(total_nums_row):
            if j > mid_len:
                start_num -= 1
            else:
                start_num += 1

            res_arr.append(str(start_num))

        spaces =((len_op-(i+1))*2) + 1
        print(" " * spaces + " ".join(res_arr) + " " * spaces)

print_nums(5)


# result= [
#  {
#             "name": "three",
#             "Value": "3",

#         },
#         {
#             "name": "six",
#             "Value": "6",
#         },
#         {
#             "name": "twelve",
#             "Value": "12",

#         },
#         {
#             "name": "one",
#             "Value": "1",

#         },
#            {
#             "name": "five",
#             "Value": "5",

#         },
#            {
#             "name": "eight",
#             "Value": "8",

#         }
# ]


# evens = []
# odds = []

# for item in result:

#     if int(item["Value"])%2 == 0:
#         evens.append(item)
#     else:
#         odds.append(item)

# res_op = []
# i = 0

# while evens and odds:

#     if i%2 == 0:
#         res_op.append(evens[0])
#         evens = evens[1:]
#     else:
#         res_op.append(odds[0])
#         odds = odds[1:]
#     i += 1

# if evens:
#     res_op += evens

# if odds:
#     res_op += odds

# print(res_op)



