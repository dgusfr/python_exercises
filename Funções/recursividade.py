def soma_ate_n(n):
    if n == 0:
        return 1
    else:
        return n + soma_ate_n(n - 1)


print(soma_ate_n(5))
