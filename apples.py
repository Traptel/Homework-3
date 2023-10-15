N = int(input("Введіть кількість школярів: "))
K = int(input("Введіть кількість яблук: "))

apples_per_student = K // N
leftovers = K % N

print("Кожному школяру дісталося яблук:", apples_per_student)
print("Яблук залишилось в корзинці:", leftovers)
