def findBiggestNumbersRange(sequence):
    if len(sequence) != 1:
        sequence = tuple(sorted(set(sequence)))
        result_list, res = [], []
        for i in sequence:
            if len(res) < 1:
                res.append(i)
            elif i == (res[-1] + 1):
                res.append(i)
            else:
                result_list.append(res)
                res = []
                res.append(i)
        result_list.append(res)
        res = [len(result_list[i]) for i in range(len(result_list))]
        max_index_res = max(map(int, res))
        result_index = res.index(max_index_res)
        return [result_list[result_index][0], result_list[result_index][-1]]
    else:
        return [sequence[0], sequence[0]]


print(findBiggestNumbersRange(
    [19, -1, 18, 17, 2, 10, 3, 12, 5, 16, 4, 11, 8, 7, 6, 15, 12, 12, 2, 1, 6, 13, 14]))
