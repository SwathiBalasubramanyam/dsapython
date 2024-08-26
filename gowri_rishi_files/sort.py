
# def quicksort(sequence):

#     # (nlog(n))
#     #split it to 2 lists recusively

#     if len(sequence) <= 1:
#         return sequence
#     else:
#         pivot = sequence.pop()

#     ig = []
#     il = []
#     for item in sequence:
#         if item > pivot:
#             ig.append(item)
#         else:
#             il.append(item)
    
#     return quicksort(il) + [pivot] + quicksort(ig)


def bubblesort(sequence):

    for i in range(len(sequence)-1):
        for j in range(len(sequence)-1-i):
            if sequence[j] > sequence[j+1]:
                sequence[j] , sequence[j+1] = sequence[j+1] , sequence[j]


    return sequence

# def mergesort(list1):
    
#     if len(list1) > 1:
#         mid = len(list1)//2
#         l_list = list1[:mid]
#         r_list = list1[mid:]
#         mergesort(l_list)
#         mergesort(r_list)

#         i = j = k = 0
#         while i < len(l_list) and j < len(r_list):
#             if l_list[i] < r_list[j]:
#                 list1[k] = l_list[i]
#                 i += 1
#                 k += 1
#             else:
#                 list1[k] = r_list[j]
#                 j += 1
#                 k += 1
#         while i < len(l_list):
#             list1[k] = l_list[i]
#             i += 1
#             k += 1
#         while j < len(r_list):
#             list1[k] = r_list[j]
#             j += 1
#             k += 1
        
# sequence = [2,3,9,5,2,83,4,5,6,7,0,8,8,7]
# (mergesort(sequence))
# print (sequence)



#bubblesort







