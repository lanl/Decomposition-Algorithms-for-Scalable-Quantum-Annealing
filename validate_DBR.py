from DBR import DBR
import networkx as nx
import random

def maximum_clique_exact_solve_np_hard(G_in):
	max_clique_number = nx.graph_clique_number(G_in)
	cliques = nx.find_cliques(G_in)
	for cl in cliques:
		if len(cl) == max_clique_number:
			return cl
def minimum_vertex_cover_exact_solve_np_hard(G):
	GC = nx.complement(G)
	nodes = list(G.nodes())
	MC = maximum_clique_exact_solve_np_hard(GC)
	return list(set(nodes)-set(MC))

for i in range(500):
	G = nx.gnp_random_graph(random.randint(66, 100), random.uniform(0.01, 0.99))
	print(len(G))
	soln = len(minimum_vertex_cover_exact_solve_np_hard(G))
	solution = DBR(G, 65, minimum_vertex_cover_exact_solve_np_hard)
	assert len(solution) == soln
