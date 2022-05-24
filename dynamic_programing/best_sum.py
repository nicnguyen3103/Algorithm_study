def best_sum(target, arr, memo={}):
    if target in memo:
        return memo[target]
    if target == 0:
        return []
    if target < 0:
        return None
    # shortest_way here is the parent.
    # We did update the shortest way below, but this only record the last value of a tree
    shortest_way = None
    for num in arr:
        remain = target - num
        result = best_sum(remain, arr, memo)
        memo[remain] = result
        if result is not None:
            way = [*result, num]
            if shortest_way is None or len(way) < len(shortest_way):
                shortest_way = way

    # memo[target] = shortest_way
    return shortest_way

if __name__ == '__main__':
    # print(best_sum(7, [2, 4])) # None
    print(best_sum(7, [5, 3, 4, 7])) # [7]
    # print(best_sum(8, [2, 3, 5])) # [3, 5]
    # print(best_sum(8, [1, 4, 5])) # [4, 4]
    # print(best_sum(100, [1, 2, 5, 25])) # [25, 25, 25, 25]