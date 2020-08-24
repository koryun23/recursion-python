def _sum(num):
    if num == 1:
        return num
    return _sum(num-1)+num
print(_sum(5))