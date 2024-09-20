# Given number of steps tell me how many possible ways you can climb these steps

n = 4
num_possible_ways = 0

def dfs(curr_step):
    global num_possible_ways
    if curr_step == n:
        num_possible_ways += 1
        return

    if curr_step > n:
        return

    dfs(curr_step+1)
    dfs(curr_step+2)

dfs(0)
print(num_possible_ways)