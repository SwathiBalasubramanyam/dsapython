def solution(S, B):
    potholes = [ele for ele in S.split(".") if ele]

    if len(potholes) == 1:
        num_potholes = len(potholes[0])
        cost_to_fix = num_potholes + 1
        if B >= cost_to_fix:
            return num_potholes
        return B - 1

    lp = 0
    rp = len(potholes) - 1

    potholes_fixed = 0

    while lp <= rp and B:

        cost_to_fix_lp = len(potholes[lp]) + 1
        cost_to_fix_rp = len(potholes[rp]) + 1

        if cost_to_fix_lp >= cost_to_fix_rp:
            if B >= cost_to_fix_lp:
                B -= cost_to_fix_lp
                potholes_fixed += cost_to_fix_lp - 1
                lp += 1
            else:
                num_of_potholes_can_be_fixed = B - 1
                potholes_fixed += num_of_potholes_can_be_fixed
                potholes[lp] = 'X' * (len(potholes[lp]) - num_of_potholes_can_be_fixed)
                B = 0
        else:
            if B >= cost_to_fix_rp:
                B -= cost_to_fix_rp
                potholes_fixed += cost_to_fix_rp - 1
                rp -= 1
            else:
                num_of_potholes_can_be_fixed = B - 1
                potholes_fixed += num_of_potholes_can_be_fixed
                potholes[rp] = 'X' * (len(potholes[rp]) - num_of_potholes_can_be_fixed)
                B = 0

    return potholes_fixed


print(solution("..", 14))