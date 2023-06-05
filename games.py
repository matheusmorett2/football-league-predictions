
teams = [
    "Andraus",
    "Grêmio Maringá",
    "PSTC",
    "Apucarana",
    "Paraná",
    "Toledo",
    "Iguaçu",
    "Patriotas FC",
    "Laranja Mecanica",
    "Araucaria",
]

results = []

def addGameResult(team1, team2, winner):
    if team1 not in teams or team2 not in teams:
        print("Invalid team name")
        return

    if team1 == team2:
        print("A team cannot play against itself")
        return

    if winner != team1 and winner != team2 and winner != "draw":
        print("Invalid winner")
        return

    results.append({"team1": team1, "team2": team2, "winner": winner})


addGameResult("Andraus", "Grêmio Maringá", "Andraus")
addGameResult("PSTC", "Apucarana", "PSTC")
addGameResult("Paraná", "Toledo", "Paraná")
addGameResult("Iguaçu", "Patriotas FC", "Patriotas FC")
addGameResult("Laranja Mecanica", "Araucaria", "Laranja Mecanica")

addGameResult("Andraus", "Paraná", "draw")
addGameResult("Grêmio Maringá", "Laranja Mecanica", "Grêmio Maringá")
addGameResult("Araucaria", "PSTC", "PSTC")
addGameResult("Iguaçu", "Apucarana", "draw")
addGameResult("Patriotas FC", "Toledo", "Patriotas FC")

addGameResult("Apucarana", "Grêmio Maringá", "Apucarana")
addGameResult("Laranja Mecanica", "Iguaçu", "Iguaçu")
addGameResult("Patriotas FC", "Andraus", "draw")
addGameResult("PSTC", "Paraná", "draw")
addGameResult("Toledo", "Araucaria", "Toledo")

addGameResult("Apucarana", "Patriotas FC", "Patriotas FC")
addGameResult("Laranja Mecanica", "PSTC", "draw")
addGameResult("Paraná", "Grêmio Maringá", "draw")
addGameResult("Araucaria", "Andraus", "Andraus")
addGameResult("Iguaçu", "Toledo", "Iguaçu")

addGameResult("Paraná", "Apucarana", "Apucarana")
addGameResult("Toledo", "Laranja Mecanica", "Laranja Mecanica")
addGameResult("Patriotas FC", "Araucaria", "Patriotas FC")
addGameResult("Grêmio Maringá", "PSTC", "PSTC")
addGameResult("Andraus", "Iguaçu", "Andraus")

addGameResult("PSTC", "Iguaçu", "Iguaçu")
addGameResult("Laranja Mecanica", "Paraná", "draw")
addGameResult("Apucarana", "Araucaria", "Apucarana")
addGameResult("Toledo", "Andraus", "Andraus")
addGameResult("Grêmio Maringá", "Patriotas FC", "Patriotas FC")

print(results)