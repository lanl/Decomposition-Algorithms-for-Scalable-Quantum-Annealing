import networkx as nx

def is_clique(G):
	"""
	INPUT:
	 - "G" Networkx Undirected Graph
	OUTPUT:
	 - "True" if G is a clique, and "False" if G is not a clique
	"""
	n = len(list(G.nodes()))
	m = len(list(G.edges()))
	if int(m) == int((n*(n-1))/float(2)):
		return True
	else:
		return False

def highest_degree_vertex(graph):
	"""
	INPUT:
	 - "graph" Networkx Undirected Graph
	OUTPUT:
	 - "i" node that has the highest degree in the graph
	"""
	degrees = [graph.degree(a) for a in list(graph.nodes())]
	maximum = max(degrees)
	for i in list(graph.nodes()):
		if graph.degree(i) == maximum:
			return i

def vc_partitioning(vertex, G):
	"""
	INPUT:
	 - "vertex" splitting vertex
	 - "G" Networkx Undirected Graph
	OUTPUT:
	 - "SSG" Left subgraph after partitioning
	 - "SG" Right subgraph after partitioning
	"""
	G1 = G.copy()
	neighbors = G.neighbors(vertex)
	G.remove_node(vertex)
	halo = []
	for a in neighbors:
		G.remove_node(a)
		halo.append(a)
	G1.remove_node(vertex)
	return G, G1, halo

def is_vertex_cover(G, vars):
	"""
	INPUT:
	 - "G" Networkx Undirected Graph
	OUTPUT:
	 - "True" if G is a vertex cover, and "False" if G is not a vertex cover
	"""
	GC = nx.complement(G)
	nodes = list(G.nodes())
	potential_clique = list(set(nodes)-set(vars))
	subg = GC.subgraph(potential_clique)
	return is_clique(subg)

def simplify1(G):
	"""
	INPUT:
	 - "G" Networkx Undirected Graph
	OUTPUT:
	 - "G" after degree 1 NBVR
	 - "VC" list of variables in the minimum vertex cover found as a result of NBVR
	"""
	remove_nodes = []
	VC = []
	nodes = list(G.nodes())
	for n in nodes:
		if G.degree(n) == 1:
			neighbors = list(G.neighbors(n))
			assert len(neighbors) == 1
			remove_nodes.append(neighbors[0])
			remove_nodes.append(n)
			VC.append(neighbors[0])
			break
	for n in remove_nodes:
		G.remove_node(n)
	return G, VC

def simplify2(G):
	"""
	INPUT:
	 - "G" Networkx Undirected Graph
	OUTPUT:
	 - "G" after degree 2 NBVR
	 - "VC" list of variables in the minimum vertex cover found as a result of NBVR
	"""
	remove_nodes = []
	VC = []
	nodes = list(G.nodes())
	for n in nodes:
		if G.degree(n) == 2:
			neighbors = list(G.neighbors(n))
			subg = G.subgraph(neighbors+[n])
			if len(list(subg.edges())) == 3:
				degrees = [G.degree(i) for i in list(subg.nodes())]
				degree_dict = {i: G.degree(i) for i in list(subg.nodes())}
				if degrees.count(2) == 1:
					continue
				if degrees.count(2) == 3:
					VC.append(n)
					VC.append(neighbors[0])
					remove_nodes += list(subg.nodes())
					break
				if degrees.count(2) == 2:
					VC.append(n)
					for i in degree_dict:
						if degree_dict[i] != 2:
							VC.append(i)
					remove_nodes += list(subg.nodes())
					break
	for n in remove_nodes:
		G.remove_node(n)
	return G, VC

def vertex_cover_reduction(G):
	"""
	INPUT:
	 - "G" Networkx Undirected Graph
	OUTPUT:
	 - "G" Networkx Undirected Graph where Neighbor Based Vertex Removal (NBVR) reduction has been applied
	 - "vars" is a set of nodes which belong to the minimum vertex cover
	"""
	vars = []
	ref1 = len(G)
	G = remove_zero_degree_nodes(G)
	G, res = simplify1(G)
	vars += res
	G, res = simplify2(G)
	vars += res
	G = remove_zero_degree_nodes(G)
	ref2 = len(G)
	while ref1 != ref2:
		ref1 = len(G)
		G = remove_zero_degree_nodes(G)
		G, res = simplify1(G)
		vars += res
		G, res = simplify2(G)
		vars += res
		G = remove_zero_degree_nodes(G)
		ref2 = len(G)
	return G, vars

def vc_upper_bound(G):
	"""
	INPUT:
	 - "G" Networkx Undirected Graph
	OUTPUT:
	 - "upper bound" list of variables which form a vertex cover in G
	"""
	res = nx.maximal_independent_set(G)
	return list(set(list(G.nodes()))-set(res))

def vc_lower_bound(G):
	"""
	INPUT:
	 - "G" Networkx Undirected Graph
	OUTPUT:
	 - "chromatic_number" integer lower bound on the minimum vertex cover number
	"""
	GC = nx.complement(G)
	answ = nx.algorithms.coloring.greedy_color(GC)
	chromatic_number = list(set(list(answ.values())))
	return len(G)-len(chromatic_number)

def remove_zero_degree_nodes(graph):
	"""
	INPUT:
	 - "graph" Networkx Undirected Graph
	OUTPUT:
	 - "graph" Networkx Undirected Graph with no zero degree nodes
	"""
	nodes = list(graph.nodes())
	for n in nodes:
		if graph.degree(n) == 0:
			graph.remove_node(n)
	return graph

def DBR(graph, LIMIT, solver_function):
	"""
	INPUT:
	 - "graph" must be a Networkx Undirected Graph
	 - "LIMIT" is an integer describing the largest size of graph which solver_func can solve; all subgraph sizes solved will be less than or equal to LIMIT
	 - "solver_function" takes a Networkx Graph, and outputs a list of nodes which are hopefully the Minimum Vertex Cover elements; it can be an approximate or exact solver function
	OUTPUT:
	 - "k" is a list of graph nodes which form a vertex cover in the input graph. If the solver is exact, then k is the Minimum Vertex Cover
	NOTES:
	 - There are many assert statements in this function. These all serve as "sanity checks"; if any of them are tripped, something went wrong or an input was incorrect
	"""
	assert type(graph) is nx.Graph
	assert type(LIMIT) is int
	assert len(graph) != 0
	print("=== Starting DBR Algorithm ===")
	G = graph.copy()
	if len(graph) <= LIMIT:
		print("=== Input Graph Size is Smaller than LIMIT ===")
		print("=== Calling Solver Function ===")
		k = solver_function(graph)
		print("=== Finished DBR Algorithm ===")
		return k
	graph = remove_zero_degree_nodes(graph)
	assert len(graph) != 0
	if is_vertex_cover(G, list(graph.nodes())) == True:
		upper = len(vc_upper_bound(graph))
		lower = vc_lower_bound(graph)
		if upper == lower and lower == len(graph):
			print("=== Input Graph with no zero degree nodes is the global Minimum Vertex Cover ===")
			print("=== No Solver Function Call Required ===")
			print("=== Finished DBR Algorithm ===")
			return list(graph.nodes())
	graph, vars = vertex_cover_reduction(graph)
	if len(graph) == 0:
		assert is_vertex_cover(G, vars) == True
		print("=== NBVR found the Minimum Vertex Cover ===")
		print("=== No Solver Function Call Required ===")
		print("=== Finished DBR Algorithm ===")
		return vars
	vertex_removal = {graph: vars}
	if len(graph) <= LIMIT:
		print("=== After NBVR the Graph Size is Smaller than LIMIT ===")
		print("=== Calling Solver Function ===")
		k = solver_function(graph)+vertex_removal[graph]
		print("=== Finished DBR Algorithm ===")
		return k
	k = vc_upper_bound(graph)+vertex_removal[graph]
	assert is_vertex_cover(G, k) == True
	subgraphs = [graph]
	while len(subgraphs) != 0:
		SG = subgraphs.pop()
		SG = remove_zero_degree_nodes(SG)
		assert len(SG) != 0
		vcount = vertex_removal[SG]
		del vertex_removal[SG]
		vertex = highest_degree_vertex(SG)
		print("=== Partitioning Subgraph ===")
		SSG, SG, halo = vc_partitioning(vertex, SG)
		SSG, SSG_vars = vertex_cover_reduction(SSG)
		SG, SG_vars = vertex_cover_reduction(SG)
		vertex_removal[SSG] = halo+vcount+SSG_vars
		vertex_removal[SG] = [vertex]+vcount+SG_vars
		#####################################################################################################
		if is_vertex_cover(G, list(SSG.nodes())) == True:
			sub_solution_SSG = list(SSG.nodes())+vertex_removal[SSG]
			assert is_vertex_cover(G, sub_solution_SSG) == True
			if len(sub_solution_SSG) < len(k):
				k = sub_solution_SSG
				del vertex_removal[SSG]
				SSG = nx.Graph()
		if is_vertex_cover(G, list(SG.nodes())) == True:
			sub_solution_SG = list(SG.nodes())+vertex_removal[SG]
			assert is_vertex_cover(G, sub_solution_SG) == True
			if len(sub_solution_SG) < len(k):
				k = sub_solution_SG
				del vertex_removal[SG]
				SG = nx.Graph()
		#####################################################################################################
		if len(SSG) != 0:
			SSG_upper = vc_upper_bound(SSG)+vertex_removal[SSG]
			assert is_vertex_cover(G, SSG_upper) == True
			if len(SSG_upper) < len(k):
				k = SSG_upper
			SSG_lower = vc_lower_bound(SSG)+len(vertex_removal[SSG])
			if SSG_lower < len(k):
				if len(SSG) <= LIMIT:
					print("=== Calling Solver Function ===")
					sub_solution_SSG = solver_function(SSG)+vertex_removal[SSG]
					del vertex_removal[SSG]
					assert is_vertex_cover(G, sub_solution_SSG) == True
					if len(sub_solution_SSG) < len(k):
						k = sub_solution_SSG
				else:
					subgraphs.append(SSG)
			else:
				del vertex_removal[SSG]
		if len(SSG) == 0:
			if SSG in list(vertex_removal.keys()):
				sub_solution_SSG = vertex_removal[SSG]
				del vertex_removal[SSG]
				assert is_vertex_cover(G, sub_solution_SSG) == True
				if len(sub_solution_SSG) < len(k):
					k = sub_solution_SSG
		#####################################################################################################
		if len(SG) != 0:
			SG_upper = vc_upper_bound(SG)+vertex_removal[SG]
			assert is_vertex_cover(G, SG_upper) == True
			if len(SG_upper) < len(k):
				k = SG_upper
			SG_lower = vc_lower_bound(SG)+len(vertex_removal[SG])
			if SG_lower < len(k):
				if len(SG) <= LIMIT:
					print("=== Calling Solver Function ===")
					sub_solution_SG = solver_function(SG)+vertex_removal[SG]
					del vertex_removal[SG]
					assert is_vertex_cover(G, sub_solution_SG) == True
					if len(sub_solution_SG) < len(k):
						k = sub_solution_SG
				else:
					subgraphs.append(SG)
			else:
				del vertex_removal[SG]
		if len(SG) == 0:
			if SG in list(vertex_removal.keys()):
				sub_solution_SG = vertex_removal[SG]
				del vertex_removal[SG]
				assert is_vertex_cover(G, sub_solution_SG) == True
				if len(sub_solution_SG) < len(k):
					k = sub_solution_SG
	assert len(vertex_removal) == 0
	print("=== Finished DBR Algorithm ===")
	return k
