def how_sum(target, arr, memo={}):
    if target in memo:
        return memo[target]
    if target == 0:
        return []
    if target < 0:
        return None

    for num in arr:
        remain = target - num
        result = how_sum(remain, arr)
        memo[remain] = result
        if result is not None:
            return [*result, num]
    return None

# Prehe green button in the gutter to run the script.
if __name__ == '__main__':
    print(how_sum(7, [5,3,4,7]))