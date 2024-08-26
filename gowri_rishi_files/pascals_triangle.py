class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 1:
            return [[1]]
        
        prev_op = self.generate(numRows-1)
        prev_op_val = prev_op[-1]
        len_prev_op_val = len(prev_op_val)
        curr_op = []

        for j in range(len_prev_op_val+1):
            if j == 0:
                curr_op.append(prev_op_val[0])
            elif j == len_prev_op_val:
                curr_op.append(prev_op_val[-1])
            else:
                curr_op.append(prev_op_val[j-1]+prev_op_val[j])

        return prev_op + [curr_op]
        