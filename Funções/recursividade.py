def soma_ate_n(n):
    if n <= 1:
        return n
    else:
        return n + soma_ate_n(n - 1)


print(soma_ate_n(5))  # 5 + 4 + 3 + 2 + 1 = 15

"""
soma_recursiva(5)
↳ return 5 + soma_recursiva(4)
             ↳ return 4 + soma_recursiva(3)
                          ↳ return 3 + soma_recursiva(2)
                                       ↳ return 2 + soma_recursiva(1)
                                                    ↳ return 1  // <-- CASO BASE ATINGIDO
"""
