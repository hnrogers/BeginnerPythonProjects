
def end_result(n):
    if n == 0:
        return n
    else:
        return n + end_result(n - 1)

print(end_result(5))