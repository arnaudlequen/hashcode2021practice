from main import *

pizzas.sort(key=lambda p: len(p))

with open(f"Outputs/{FILE_NAME}", "w+") as file:
    current_pizza = 0
    while current_pizza < len(pizzas):
        for team_size, team_number in [(2, T2), (3, T3), (4, T4)]:
            for team in range(team_number):
                if current_pizza + team_size - 1 <= len(pizzas):
                    p = " ".join(list(map(str, range(current_pizza, current_pizza + team_size))))
                    file.write(f"{team_size} {p} \n")
                    current_pizza += team_size