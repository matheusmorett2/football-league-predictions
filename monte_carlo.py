from itertools import combinations
from random import choice
from tabulate import tabulate
import json

with open('results.json', 'r') as f:
    results = json.load(f)

with open('teams.json', 'r') as f:
    teams = json.load(f)

def calculate_standings(results):
    standings = {team: 0 for team in teams}

    for result in results:
        if result["winner"] == "draw":
            standings[result["team1"]] += 1
            standings[result["team2"]] += 1
        else:
            standings[result["winner"]] += 3

    return standings

def simulate_season(remaining_games, current_standings):
    simulated_standings = current_standings.copy()

    for game in remaining_games:
        outcome = choice([0, 1, 2])
        if outcome == 0:
            simulated_standings[game[0]] += 3
        elif outcome == 1:
            simulated_standings[game[0]] += 1
            simulated_standings[game[1]] += 1
        else:
            simulated_standings[game[1]] += 3

    return simulated_standings

def calculate_exact_probabilities(results, num_simulations):
    current_standings = calculate_standings(results)

    counts = {team: {"G4": 0, "Middle": 0, "Z2": 0} for team in teams}
    for _ in range(num_simulations):
        standings = simulate_season(remaining_games, current_standings)

        sorted_teams = sorted(standings.items(), key=lambda x: x[1], reverse=True)

        for i, (team, _) in enumerate(sorted_teams):
            if i < 4:
                counts[team]["G4"] += 1
            elif i < 8:
                counts[team]["Middle"] += 1
            else:
                counts[team]["Z2"] += 1

    probabilities = {team: {k: v / num_simulations for k, v in results.items()} for team, results in counts.items()}

    return probabilities

def print_sorted_probabilities(probabilities):
    sorted_probs = sorted(probabilities.items(), key=lambda x: x[1]["G4"], reverse=True)
    table = []

    for team, probs in sorted_probs:
        table.append([team, f"{probs['G4'] * 100:.2f}%", f"{probs['Middle'] * 100:.2f}%", f"{probs['Z2'] * 100:.2f}%"])

    print(tabulate(table, headers=["Team", "G4", "Meio da Tabela", "Z2"]))

# Calculando todos os jogos possíveis
all_games = list(combinations(teams, 2))

# Encontrando os jogos já realizados
played_games = set((result['team1'], result['team2']) for result in results)
played_games.update((result['team2'], result['team1']) for result in results)

# Jogos restantes são todos os jogos possíveis menos os já realizados
remaining_games = [game for game in all_games if game not in played_games]

# Simulando 1000000 temporadas com os jogos restantes:
probabilities = calculate_exact_probabilities(results, 10000)

print_sorted_probabilities(probabilities)