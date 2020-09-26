def fibonacci(start, end):
    fib = []
    for i in range(end):
        if len(fib) < 2:
            fib.append(i)
        else:
            fib.append(fib[-1] + fib[-2])

    print(fib)
    result = " ".join(map(str, fib[start:end]))
    print(result)
    return result


fibonacci(10, 15)