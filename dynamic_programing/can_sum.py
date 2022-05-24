def can_sum(num, arr, memo={}):
    if num in memo:
        return memo[num]

    if num == 0:
        return True

    if num < 0:
        return False

    for i in arr:
        memo[num - i] = can_sum(num - i, arr, memo)
        if memo[num - i]:
            return True

    return False

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print(can_sum(300, [7, 14]))