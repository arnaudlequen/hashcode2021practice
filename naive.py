from main import *
from output import Output

output = Output()
pizzas.sort(key=lambda p: -len(p[1]))

current_pizza = 0
for team_size, team_number in [(2, T2), (3, T3), (4, T4)]:
    for team in range(team_number):
        if current_pizza + team_size - 1 < len(pizzas):
            output.add_team(list(map(lambda x: pizzas[x][0], range(current_pizza, current_pizza + team_size))))
            current_pizza += team_size
        else:
            break

print("Score: " + str(output.score()))
output.write(FILE_NAME)