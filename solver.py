# Put your solution here.

import networkx as nx
from math import ceil

def solve(client):
    client.end()
    client.start()

    graph = client.G
    home = client.h
    num_students = client.students
    num_bots = client.b
    max_lies = ceil(client.v / 2)
    bots_found = 0
    students = list(range(1, num_students + 1))

    #The dictionary of how many bots we currently know at each vertex
    bots_at = {}

    #The dictionary of unvisited nodes being the key, with the score of the node being the value
    unvisited = {}
    unvisited_list = list(graph.nodes())
    unvisited_list.remove(home)
    bots_at[home] = 0
    for i in unvisited_list:
    	unvisited[i] = 0
    	bots_at[i] = 0
    lies = {}

    #The dictionary of vertices being the key and dictionary of scout result of that vertex being the value
    scout_result = {}
    mst = nx.minimum_spanning_tree(graph)
    bots_locations = []
    for k in students:
    	lies[k] = 0
    	probability[k] = 0.5
    for i in unvisited:
    	scout_result[i] = client.scout(i, students)

    while bots_found < num_bots:
    	for vertex in unvisited:
    		unvisited[vertex] = count_score(vertex, scout_result, lies)
    	most_probable_vertex = max(unvisited, key=unvisited.get)
    	path_to_home = nx.shortest_path(mst, source=most_probable_vertex, target=home)
    	remote_result = client.remote(most_probable_vertex, path_to_home[1])
    	if remote_result > 0:
    		bots_found += remote_result - bots_at[most_probable_vertex]
    		if path_to_home[1] not in bots_locations:
    			bots_locations.append(path_to_home[1])
    		bots_at[path_to_home[1]] += remote_result
    		for student in scout_result[most_probable_vertex]:
    			if not scout_result[most_probable_vertex][student]:
    				lies[student] += 1
    	else:
    		for student in scout_result[most_probable_vertex]:
    			if scout_result[most_probable_vertex][student]:
    				lies[student] += 1
    	unvisited.pop(most_probable_vertex)

    client.end()




def count_score(vertex, scout_result, lies):
	sum_score = 0
	for student in scout_result[vertex]:
		sum_score += (lambda x: 1 if x else -1)(scout_result[vertex][student]) * (1 - ((max_lies - lies[student]) / client.v))







