import itertools as it

def all_possible_ops(problem_list,operations):
    cal_res = 0
    for i in problem_list:
        print(f"Step {data.index(i)} of {len(data)}")
        operations_list = list(it.product(operations,repeat=len(i) - 2))
        k = 0
        while k < len(operations_list):
            l = 0
            result = i[1]
            while l < len(i) - 2:
                result = eval(f"{result}{operations_list[k][l]}{i[l + 2]}")
                if result > int(i[0][0:-1]):
                    break
                l += 1
            if result == int(i[0][0:-1]):
                cal_res += result
                break
            k += 1
    return cal_res


data = list(map(lambda x: x.strip().split(),open("Inputs/Day7.txt").readlines()))

#Part1
operations_part1 = ["+","*"]
print(all_possible_ops(data,operations_part1))

#Part2
operations_part2 = ["+","*","*int('1'+'0'*len(i[l+2]))+"]
print(all_possible_ops(data,operations_part2))
