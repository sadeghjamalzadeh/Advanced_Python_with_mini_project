import re


def solve(path):
    ans = 0
    with open(path, 'r') as f:
        lines = f.readlines()
        for line in lines:
            if len(line.strip()) != 0 and re.fullmatch("(^#).+", line.strip()) == None:
                ans += 1
    return ans
