from main import *

def map_ingredients_to_pizzas(pizzaList):
    """
    Return a map that returns to each ingredients the pizzas in which it appear
    """
    dico_ingredients_to_pizzas = {}
    for pizza in pizzaList:
        for ingredient in pizza[1]:
            if ingredient in dico_ingredients_to_pizzas:
                dico_ingredients_to_pizzas[ingredient].append(pizza[0])
            else:
                dico_ingredients_to_pizzas[ingredient] = [pizza[0]]
    return dico_ingredients_to_pizzas

pizzas.sort(key=lambda p: -len(p[1]))

dico_ingredients_to_pizzas = map_ingredients_to_pizzas(pizzas)
#print(dico_ingredients_to_pizzas)

def collisions_pizza(pizza, pizzaList):
    all_collisions = []
    ingredients = pizza[1]
    for other_pizza in pizzaList:
        new_ingredients = other_pizza[1]
        collisions = ingredients.intersection(new_ingredients)
        nb_collisions = len(collisions)
        all_collisions.append(nb_collisions)
    return all_collisions

print(collisions_pizza(pizzas[0], pizzas))


"""
with open(f"Outputs/{FILE_NAME}", "w+") as file:
    current_pizza = 0
    output = []
    for team_size, team_number in [(2, T2), (3, T3), (4, T4)]:
        for team in range(team_number):
            if current_pizza + team_size - 1 < len(pizzas):
                p = " ".join(list(map(lambda x: str(pizzas[x][0]), range(current_pizza, current_pizza + team_size))))
                output.append(f"{team_size} {p}\n")
                current_pizza += team_size
            else:
                break

    file.write(f"{len(output)}\n")
    for line in output:
        file.write(line)
"""