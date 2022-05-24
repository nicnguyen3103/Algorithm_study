

def grid_traverse(m, l, d) -> int:
    if len(m) == 0:
        return -1
    max_l = len(m[0]) - 1
    max_d = len(m) - 1

    if l == max_l or d == max_d:
        return 1
    else:
        return grid_traverse(m, l+1, d) + grid_traverse(m, l, d+1)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    import numpy as np

    x = [[1]]
    ways = grid_traverse(x, 0, 0)
    print(ways)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
