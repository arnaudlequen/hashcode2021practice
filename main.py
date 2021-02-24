import sys

FILE_NAME = "a_example.in"

def main():
    f = open(FILE_NAME)
    N, T2, T3, T4 = list(map(int, f.readline().split()))

    pizzas = []

    for _ in range(N):
        pizzas.append(set(f.readline().split()[1:]))

    for p in pizzas:
        print(p)




main()