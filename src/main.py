from src.implementations import greedy, random, semi_greedy


def ma(distances):
    soma = 0
    n = len(distances)
    for i in lista:
        soma += i
    total = soma/n
    return total

def calcSQD(distances):
    med = ma(distances)
    soma = 0
    for i in distances:
        soma += (i - med)**2

    return soma

def devPP(distances):
    soma = calcSQD(distances)
    n = len(distances)
    total = soma/n
    dpp = total**(1/2)
    return dpp

def main():
    distances_random = []
    distances_greedy = []
    distances_semi_greedy = []

    print("Running Traveling Salesman Algorithm - Random...")
    for i in range(30):
        trv_mgr = random.TravelerManager()
        # trv_mgr.load()
        solution = trv_mgr.solution()
        distances = trv_mgr.calculate_distances(solution)
        distances_random.append(distances)
        print(f"Random N{i + 1} - Distância da Solução: {distances}")

    print("\nRunning Traveling Salesman Algorithm - Greedy...")
    for i in range(30):
        trv_mgr = greedy.TravelerManager()
        # trv_mgr.load()
        solution = trv_mgr.solution()
        distances = trv_mgr.calculate_distances(solution)
        distances_greedy.append(distances)
        print(f"Greedy N{i + 1} - Distância da Solução: {distances}")

    print("\nRunning Traveling Salesman Algorithm - Semi Greedy...")
    for i in range(30):
        trv_mgr = semi_greedy.TravelerManager()
        # trv_mgr.load()
        solution = trv_mgr.solution()
        distances = trv_mgr.calculate_distances(solution)
        distances_semi_greedy.append(distances)
        print(f"SemiGreedy N{i + 1} - Distância da Solução: {distances}")

    print(f"""
    - - Médias - -
    Algoritmo Aleatório: {sum(distances_random) / len(distances_random)}
    Algoritmo Guloso:    {sum(distances_greedy) / len(distances_greedy)}
    Algoritmo Híbrido:   {sum(distances_semi_greedy) / len(distances_semi_greedy)}
""")


if __name__ == "__main__":
    main()

