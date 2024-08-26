# def genparenthesis(s,left,right):
    
#     n = 3
#     if len(s) == 2*n:
#         res.append(s)
#         return
        
#     if left < n:
#         genparenthesis(s+"(" ,left+1,right)
        
#     if right < left:
#         genparenthesis(s+")" ,left,right+1)


# res = []
# genparenthesis('',0,0)
# print (res)

# s = "(1+(2*3)+((8)/4))+1"
# res = 0
# cnt = 0
# for c in s:
#     print (cnt,res)
#     if c == "(":
#         cnt += 1
        
#     elif c == ")":
#         cnt -= 1
#     res = max(cnt,res)
# print (res)



  

out = ''
s = 'a3b2c1'
j = 0


for _ in range(len(s)//2):
    import pdb;pdb.set_trace()
    out = out + s[j] * (int(s[j+1]))
    j += 2
    print (out)


print (out)

                