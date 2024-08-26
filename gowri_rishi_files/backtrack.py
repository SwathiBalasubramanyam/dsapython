# def backtrack(path,target,indx,candidates,res): 

#     if target == 0:
#         res.append(path)
#         return
    
#     if target < 0:
#         return

#     for x in range(indx,len(candidates)):
#         backtrack(path + [candidates[x]],target -candidates[x],x,candidates,res)

#     return (res)

      

# candidates = [2,3,6,7]
# target = 7
# print (backtrack([],target,0,candidates,[]))

# ########################################################################################
#     ########################################################################################


# def backtrackc(nums,path,res):

#     if not nums:
#         res.append(path)
#         return

#     for x in range(len(nums)):
#         backtrackc(nums[:x]+ nums[x+1:], path+[nums[x]], res)
        
#     return res

# res = []
# path = []
# nums = [1,2,3]
# print (backtrackc(nums,path,res))


# ########################################################################################
#     ########################################################################################




def generateparnt(out,left,right,n,res):

    import pdb;pdb.set_trace()
    if len(out) == 2*n:
        res.append(out)

    if left < n:
        generateparnt(out+"(",left+1,right,n,res)

    if right < left:
        generateparnt(out +")",left,right+1,n,res)

    return res

print (generateparnt('',0,0,3,[]))


    
        

