import sys

assert len(sys.argv) == 2, "Usage: main.py filename"

FILE_NAME = sys.argv[1]
print("Reading " + FILE_NAME)

with open(f"Inputs/{FILE_NAME}") as file:
    N, T2, T3, T4 = list(map(int, file.readline().split()))

    pizzas = []

    for i in range(N):
        pizzas.append((i, set(file.readline().split()[1:])))

    #for p in pizzas:
    #    print(p)
