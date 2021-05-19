import networkx as nx  # biblioteka do obliczania cykli


# wczytanie pliku
f = open('zadanie_B/slo1ocen.in')

n = int(f.readline())  # liczba słoni

waga = list(f.readline().split(' '))  # lista wag słoni, str zamienione na int
for _ in range(0, len(wagi)):
    wagi[_] = int(wagi[_])

index = []  # index dla wag
for idx in range(len(waga)):
    index.append('%i' %(idx + 1))

dict_waga = dict(zip(index, waga))  # słownik przypisujący konkretną wagę do indexu

start = list(f.readline().split((' ')))  # początkowa kolejność słoni 
start = list(map(lambda x: x.strip('\n'), start))  # oczyszczenie danych z niepotrzebnych znaków

end = list(f.readline().split(' '))  # lista końcowa zaproponowana przez dyrektora zoo
end = list(map(lambda x: x.strip('\n'), end))

edges = list(zip(start, end)) # wyznaczenie wspólnych krawędzi dla obu list

G = nx.DiGraph(edges)  # model krawędzi 

for cycle in nx.simple_cycles(G):  # iteracja przez cykle
    cycle
    
    cycle = [dict_waga.get(item, item) for item in cycle]  # przypisanie konkretnej wagi do danego imdeksu
    cycle = list(map(int, cycle))
    
    # praca wykonana przy przesuwaniu słoni dla metody 1 i 2 w pojedyńczym cyklu
    praca1 = sum(item for item in cycle) + (len(cycle) - 2) * (min(cycle))
    praca2 = sum(item for item in cycle) + min(cycle) + (len(cycle) + 1) * min(waga) 
    all_work += min(praca1, praca2)  # suma minimalnej pracy wykonanej przez wszystkie cykle

print(all_work)
