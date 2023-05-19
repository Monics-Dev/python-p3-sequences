def print_fibonacci(length=0):
    if length == 0:
        print([])
    elif length == 1:
        print([0])
    else:
        fib_seq = [0, 1]
        for _ in range(2, length):
            next_num = fib_seq[-1] + fib_seq[-2]
            fib_seq.append(next_num)
        print(fib_seq)