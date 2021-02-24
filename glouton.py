from main import *

pizzas.sort(key=lambda p: -len(p[1]))

def team_size_by_id(id):
    if id <= T2:
        return 2
    elif id <= T3:
        return 3
    elif id <= T4:
        return 4
    else:
        return -1

with open(f"Outputs/{FILE_NAME}", "w+") as file:
    current_pizza = 0
    output = []

    # pizzas, ingredients
    teams = [[[], set()] for _ in range(T2 + T3 + T4)]

    for pizza in pizzas:
        best_id = -1
        best_size = 0
        for i in range(len(teams)):
            if len(teams[i][1].union(pizza[1])) == len(pizza[1]) - len(teams[i][1]):
                teams[i][0].append(pizza[0])
                teams[i][1] = teams[i][1].union(pizza[1])
                break
            else:
                new_ingredients_number = len(teams[i][1].union(pizza[1]))
                if new_ingredients_number >= best_size:
                    best_id = i
                    best_size = new_ingredients_number
        if best_id != -1:
            teams[best_id][0].append(pizza[0])
            teams[best_id][1] = teams[best_id][1].union(pizza[1])

    for i in range(len(teams)):
        if team_size_by_id(i) == len(teams[i][0]):
            p = " ".join(list(map(str, teams[i][0])))
            output.append(f"{team_size_by_id(i)} {p}")

    file.write(f"{len(output)}\n")
    for line in output:
        file.write(line)
