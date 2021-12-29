def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)


def summary(n):
    if n == 1:
        return 1
    else:
        return n + summary(n - 1)

print(summary(2))
