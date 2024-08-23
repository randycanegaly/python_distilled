nums = [1, 2, 3, 4, 6]

def prc_reduce(func, items, initial):
    result = initial
    for item in items:
        result = func(result, item)
        print('result: ', result)
    return result

answer = prc_reduce(lambda x, y: x * y, nums, 1)

print(answer)

