# Put your solution here.

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

    #The dictionary of unvisited nodes being the key, with the score of the node being the value
    unvisited = list(graph.nodes())
    
    lies = {}
    scout_result = {}
    mst = nx.minimum_spanning_tree(graph)
    unvisited.remove(home)
    bots_locations = []
    for k in students:
    	lies[k] = 0
    	probability[k] = 0.5
    for i in unvisited:
    	result = client.scout(i, students)
    	scout_result[i] = result

    while bots_found < num_bots:
    	for vertex in unvisited:
    		count_score(vertex)


def count_score(vertex, scout_result, lies):
	sum_score = 0
	for student in scout_result[vertex]:
		sum_score += (lambda x: 1 if x else -1)(student) * (1 - ((max_lies - lies[student]) / client.v))







