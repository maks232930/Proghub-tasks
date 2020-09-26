def findBiggestNumbersRange(sequence):
    if len(sequence) != 1:
        sequence = set(sequence)
        sequence = sorted(list(sequence))
        result_list = []
        res = []
        for i in sequence:
            if len(res) < 1:
                res.append(int(i))
            elif i == res[-1]:
                res.append(i)
                result_list.append(res)
                res = []
            elif i == (res[-1] + 1):
                res.append(i)
                if sequence.index(i) == (len(sequence) - 1):
                    result_list.append(res)
                    res = []
            else:
                result_list.append(res)
                res = []
                res.append(i)

        for i in range(len(result_list)):
            res.append(len(result_list[i]))

        max_index_res = max(res)
        result_index = res.index(max_index_res)
        result_list = result_list[result_index]

        return [result_list[-0], result_list[-1]]
    else:
        return [sequence[0], sequence[0]]


print(findBiggestNumbersRange(
    [19, -1, 18, 17, 2, 10, 3, 12, 5, 16, 4, 11, 8, 7, 6, 15, 12, 12, 2, 1, 6, 13, 14]))
