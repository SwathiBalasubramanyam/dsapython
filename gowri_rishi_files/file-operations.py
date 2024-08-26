# with open('inputfiles/text.txt','r') as f, open('inputfiles/out-text.txt','w') as w:


#     for line in f:
#         print (line)

#     # c = f.readlines()

#     # for each in c:
#     #     rslt = True
#     #     pat = "\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}"
#     #     import re
#     #     m= re.search(pat,each)
#     #     if m:
#     #         ip= (m.group(0)).split(".")
#     #         for octet in ip:
#     #             if not (0 <= int(octet) < 256):
#     #                 rslt = False
#     #     if not rslt:
#     #         print ("fail")
#     #     else:
#     #         print (ip)

# import json

# with open('inputfiles/json.json','r') as j:
#     j1 = json.load(j)

# for each in j1:
#     print (j1[each])




# # import yaml

# # with open('inputfiles/yaml.yaml','f') as y:
# #     y1 = yaml.load(y)

# # print (y1)


# # sample_url = 'http://coreyms.com'
# # print (sample_url)

# # # Reverse the url
# # # print sample_url[::-1]

# # # # Get the top level domain
# # print (sample_url[-4:])

# with open("inputfiles/text.txt",'r') as f:

#     import pdb;pdb.set_trace()
    
#     c = f.read().splitlines()
#     import pdb;pdb.set_trace()
#     d = {}
#     mw,mc = '',0
#     for line in c:
#         nl = line.split(" ")
#         for word in nl:
#             d[word] =d.get(word,0) + 1
#             if d[word] > mc:
#                 mc= d[word]
#                 mw = word
# print (d)
# m = (len(d.values()))
# print (m)
# print (mc,mw)


# a='Beautiful, is; better*than\nugly'

# import re

# out = re.split("; |, |\*",a)

# print (out)





# with open('inputfiles/newfile.txt','r') as f ,open('inputfiles/newfile1.txt','a+') as k:

#     d = {}
#     mc = 0
#     w = ''
#     content = f.read().splitlines()
#     for c in content:
#         cn = c.split()
#         for word in cn:
#             d[word] = d.get(word,0) + 1

#             if d[word] > mc:
#                 mc = d[word]
#                 w = word

#     k.write(str(mc))



# l = [1,2,10,23,2,1,98]
# l.sort()
# print (l)



with open('inputfiles/newfile1.txt','r') as h:

    content = h.read()
    print (content)

    pat = '^(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\.(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\.(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\.(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])$'

    import re
    for line in content:
        if re.search(pat,line):
            print (line)

