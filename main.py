import sys

assert len(sys.argv) == 2, "Usage: main.py filename"

FILE_NAME = sys.argv[1]
print("Reading " + FILE_NAME)

with open(FILE_NAME) as file:
    N, T2, T3, T4 = list(map(int, file.readline().split()))

    pizzas = []

    for _ in range(N):
        pizzas.append(set(file.readline().split()[1:]))

    for p in pizzas:
        print(p)
