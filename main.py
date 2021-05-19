index = []

f = open('zadanie_B/slo1ocen.in')
n = int(f.readline())

wagi = list(f.readline().split(' '))
for _ in range(0, len(wagi)):
    wagi[_] = int(wagi[_])


for r in range(len(wagi)):
    index.append('%i' %(r + 1))


wag = dict(zip(index, wagi))


org = list(f.readline().split((' ')))
org = list(map(lambda x: x.strip('\n'), org))


fin = list(f.readline().split(' '))
fin = list(map(lambda x: x.strip('\n'), fin))




import networkx as nx

edges = list(zip(org, fin))
all_work = 0

G = nx.DiGraph(edges)

for cycle in nx.simple_cycles(G):
    cycle
    
    cycle = [wag.get(item, item) for item in cycle]
    cycle = list(map(int, cycle))

    praca1 = sum(item for item in cycle) + (len(cycle) - 2) * (min(cycle))
    praca2 = sum(item for item in cycle) + min(cycle) + (len(cycle) + 1) * min(wagi) 
    all_work += min(praca1, praca2) 

print(all_work)






# print()
# cyk = list(nx.simple_cycles(G))
# print(cyk)
