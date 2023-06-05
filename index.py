import random
from tabulate import tabulate
import json

with open('results.json', 'r') as f:
    results = json.load(f)

with open('teams.json', 'r') as f:
    teams = json.load(f)

def calculate_win_rates(results):
    win_rates = {team: {"wins": 0, "games": 0} for team in teams}

    for result in results:
        team1 = result["team1"]
        team2 = result["team2"]
        winner = result["winner"]

        win_rates[team1]["games"] += 1
        win_rates[team2]["games"] += 1

        if winner != "draw":
            win_rates[winner]["wins"] += 1

    for team in teams:
        wins = win_rates[team]["wins"]
        games = win_rates[team]["games"]
        win_rates[team] = wins / games if games > 0 else 0

    return win_rates


def calculate_standings(results):
    standings = {team: 0 for team in teams}

    for result in results:
        if result["winner"] == "draw":
            standings[result["team1"]] += 1
            standings[result["team2"]] += 1
        else:
            standings[result["winner"]] += 3

    return standings


def simulate_game(team1, team2, win_rates):
    rand_num = random.random()
    win_rate_difference = win_rates[team1] - win_rates[team2]
    if win_rate_difference > rand_num:
        return team1
    elif win_rate_difference < rand_num:
        return team2
    else:
        return "draw"


def simulate_remaining_rounds(remaining_games, win_rates):
    simulated_results = []

    for game in remaining_games:
        simulated_winner = simulate_game(game["team1"], game["team2"], win_rates)
        simulated_results.append({"team1": game["team1"], "team2": game["team2"], "winner": simulated_winner})

    return simulated_results


def calculate_remaining_games(results):
    played_games = [(game["team1"], game["team2"]) for game in results]
    played_games += [(game["team2"], game["team1"]) for game in results]
    remaining_games = []

    for team1 in teams:
        for team2 in teams:
            if team1 != team2 and (team1, team2) not in played_games:
                remaining_games.append({"team1": team1, "team2": team2})

    return remaining_games


def calculate_probabilities(results, num_simulations):
    remaining_games = calculate_remaining_games(results)
    win_rates = calculate_win_rates(results)
    current_standings = calculate_standings(results)
    final_standings = []

    for _ in range(num_simulations):
        simulated_results = simulate_remaining_rounds(remaining_games, win_rates)
        simulated_standings = calculate_standings(results + simulated_results)
        final_standings.append(simulated_standings)

    probabilities = {team: {"G4": 0, "Middle": 0, "Z2": 0} for team in teams}

    for standings in final_standings:
        sorted_standings = sorted(standings.items(), key=lambda x: x[1], reverse=True)

        for i, (team, points) in enumerate(sorted_standings):
            if i < 4:
                probabilities[team]["G4"] += 1
            elif i >= len(teams) - 2:
                probabilities[team]["Z2"] += 1
            else:
                probabilities[team]["Middle"] += 1

    for team, probs in probabilities.items():
        probs["G4"] /= num_simulations
        probs["Middle"] /= num_simulations
        probs["Z2"] /= num_simulations

    # Adjust probabilities based on mathematical certainty
    sorted_current_standings = sorted(current_standings.items(), key=lambda x: x[1], reverse=True)
    max_points_remaining = len(remaining_games) * 3

    for i, (team, points) in enumerate(sorted_current_standings):
        if points + max_points_remaining < sorted_current_standings[3][1]:  # Cannot reach G4
            probabilities[team]["G4"] = 0
        if points + max_points_remaining < sorted_current_standings[len(teams) - 2][1]:  # Can fall to Z2
            probabilities[team]["Z2"] = 1

    return probabilities


def print_sorted_probabilities(probabilities):
    sorted_probs = sorted(probabilities.items(), key=lambda x: x[1]["G4"], reverse=True)
    table = []

    for team, probs in sorted_probs:
        table.append([team, f"{probs['G4'] * 100:.2f}%", f"{probs['Middle'] * 100:.2f}%", f"{probs['Z2'] * 100:.2f}%"])

    print(tabulate(table, headers=["Team", "G4", "Meio da Tabela", "Z2"]))

# Simulando 100000 temporadas com os jogos restantes:
probabilities = calculate_probabilities(results, 10000)

print_sorted_probabilities(probabilities)

