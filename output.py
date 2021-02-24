from typing import List
from main import pizzas, T2, T3, T4

pizzas_map = {}
for id, ingredients in pizzas:
    pizzas_map[id] = ingredients


class Output:
    teams_pizzas: List[List[int]]

    def __init__(self):
        self.teams_pizzas = []

    def add_team(self, team_pizzas: List[int]):
        assert len(list(set(team_pizzas))) == len(team_pizzas)
        self.teams_pizzas.append(team_pizzas)

    def check(self):
        all_pizzas = {}
        team_count = {2: 0, 3: 0, 4: 0}
        team_index = 0
        for team_pizzas in self.teams_pizzas:
            for pizza in team_pizzas:
                if pizza in all_pizzas:
                    print(f"Pizza {pizza} in team {all_pizzas[pizza]} and {team_index}")
                else:
                    all_pizzas[pizza] = team_index

            team_count[len(team_pizzas)] += 1
            team_index += 1

        assert team_count[2] <= T2
        assert team_count[3] <= T3
        assert team_count[4] <= T4

    def write(self, filename):
        self.check()

        lines = [str(len(self.teams_pizzas))]
        for team_pizzas in self.teams_pizzas:
            lines.append(f"{len(team_pizzas)} {' '.join([str(pizza) for pizza in team_pizzas])}")

        with open(f"Outputs/{filename}", "w") as file:
            file.writelines([line + "\n" for line in lines])

    def score(self):
        self.check()

        score = 0
        for team_pizzas in self.teams_pizzas:
            ingredients = set()
            for pizza in team_pizzas:
                for ingredient in pizzas_map[pizza]:
                    ingredients.add(ingredient)
            score += len(ingredients) * len(ingredients)

        return score
