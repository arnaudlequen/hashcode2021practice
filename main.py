def main():
    N, T2, T3, T4 = list(map(int, input().split()))

    pizzas = []

    for _ in range(N):
        pizzas.append(set(input().split()[1:]))

    for p in pizzas:
        print(p)




main()