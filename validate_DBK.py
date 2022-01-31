from DBK import DBK
import networkx as nx
import random

def maximum_clique_exact_solve_np_hard(G):
	max_clique_number = nx.graph_clique_number(G)
	cliques = nx.find_cliques(G)
	for cl in cliques:
		if len(cl) == max_clique_number:
			return cl

for i in range(500):
	G = nx.gnp_random_graph(random.randint(66, 80), random.uniform(0.01, 0.99))
	print(len(G))
	solution = DBK(G, 65, maximum_clique_exact_solve_np_hard)
	assert len(solution) == nx.graph_clique_number(G)
