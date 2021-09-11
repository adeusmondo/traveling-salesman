import pathlib
import statistics

import matplotlib.pyplot as plt
import numpy as np

from src.implementations import greedy, random, semi_greedy


def write_in_file(file, content):
    with open(file, 'a') as opened_file:
        opened_file.write(content)
        
def remove_files_results():
    files = [
            "output/random_results.txt",
            "output/greedy_results.txt",
            "output/semi_greedy_results.txt",
            "output/avg_algol.txt",
            "output/boxplot.png",
    ]
    for file in files:
        file_to_rem = pathlib.Path(file)
        if file_to_rem.exists():
            file_to_rem.unlink()

def draw_boxplot(avgs):
    #fig = plt.figure(figsize =(10, 7))
    #ax = fig.add_axes([0, 0, 1, 1])
    #ax.set_title('Caixeiro Viajante - BoxPlot')
    #bp = ax.boxplot(x=avgs, labels=["Randomico", "Guloso", "Híbrido"])
    #plt.savefig('output/boxplot.png')
    #plt.close()
    font_1 = {'family':'serif', 'color':'#993556'}
    font_2 = {'family':'serif', 'color':'#5C1BCC'}
    font_3 = {'family':'serif', 'color':'000', 'size':12}

    plt.figure(figsize =(10, 7))
    plt.boxplot(x=avgs, labels=["Randomico", "Guloso", "Híbrido"])
    plt.axes([0, 0, 1, 1])
    plt.title('Caixeiro Viajante - BoxPlot')
    plt.ylabel("Altura")

    for i in range(0, len(avgs)):
        plt.text(i + 1, min(avgs[i]), '{0:.2f}'.format(min(avgs[i])), fontdict=font_2)
        plt.text(i + 1, statistics.mean(avgs[i]), '{0:.2f}'.format(statistics.mean(avgs[i])), fontdict=font_1)
        plt.text(i + 1, max(avgs[i]), '{0:.2f}'.format(max(avgs[i])), fontdict=font_1)

    plt.xticks([1, 2, 3], ['R', 'G', 'H'])
    plt.text(2.8, 1.45, 'R - Randomico\nG - Guloso\nH - Híbrido',
                               horizontalalignment='left', fontdict=font_3)

    plt.savefig('boxplot.png')
    plt.close()

def main():
    remove_files_results()

    distances_random = []
    distances_greedy = []
    distances_semi_greedy = []

    print("Running Traveling Salesman Algorithm - Random...")
    write_in_file("output/random_results.txt", "Running Traveling Salesman Algorithm - Random...\n\n")
    for i in range(30):
        trv_mgr = random.TravelerManager()
        trv_mgr.load()
        solution = trv_mgr.solution()
        distances = trv_mgr.calculate_distances(solution)
        distances_random.append(distances)
        print(f"Random N{i + 1} - Distância da Solução: {distances}")
        write_in_file("output/random_results.txt", f"Random N{i + 1} - Distância da Solução: {distances}\n")

    print("\nRunning Traveling Salesman Algorithm - Greedy...")
    write_in_file("output/greedy_results.txt", "Running Traveling Salesman Algorithm - Greedy...\n\n")
    for i in range(30):
        trv_mgr = greedy.TravelerManager()
        trv_mgr.load()
        solution = trv_mgr.solution()
        distances = trv_mgr.calculate_distances(solution)
        distances_greedy.append(distances)
        print(f"Greedy N{i + 1} - Distância da Solução: {distances}")
        write_in_file("output/greedy_results.txt", f"Greedy N{i + 1} - Distância da Solução: {distances}\n")

    print("\nRunning Traveling Salesman Algorithm - Semi Greedy...")
    write_in_file("output/semi_greedy_results.txt", "Running Traveling Salesman Algorithm - Semi Greedy...\n\n")
    for i in range(30):
        trv_mgr = semi_greedy.TravelerManager()
        trv_mgr.load()
        solution = trv_mgr.solution()
        distances = trv_mgr.calculate_distances(solution)
        distances_semi_greedy.append(distances)
        print(f"SemiGreedy N{i + 1} - Distância da Solução: {distances}")
        write_in_file("output/semi_greedy_results.txt", f"SemiGreedy N{i + 1} - Distância da Solução: {distances}\n")

    random_avg = sum(distances_random)/len(distances_random)
    greedy_avg = sum(distances_greedy)/len(distances_greedy)
    semi_avg   = sum(distances_semi_greedy)/len(distances_semi_greedy)
    
    avg = f"""
    - - Médias Aritiméticas - -
    Algoritmo Aleatório: {random_avg:.2f} KM
    Algoritmo Guloso:    {greedy_avg:.2f} KM
    Algoritmo Híbrido:   {semi_avg:.2f} KM

    - - Desvio Padrão - -
    Algoritmo Aleatório: {statistics.stdev(distances_random):.2f}
    Algoritmo Guloso:    {statistics.stdev(distances_greedy):.2f}
    Algoritmo Híbrido:   {statistics.stdev(distances_semi_greedy):.2f}
"""
    write_in_file("output/avg_algol.txt", avg)
    draw_boxplot([distances_random, distances_greedy, distances_semi_greedy])


if __name__ == "__main__":
    main()

