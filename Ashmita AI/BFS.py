# Python3 Program to print BFS traversal
from collections import defaultdict
# This class represents a directed graph
class Graph:
	def __init__(self):
		self.graph = defaultdict(list)
	# Function to add an edge to graph
	def addEdge(self, u, v):
		self.graph[u].append(v)
	# Function to print a BFS of graph
	def BFS(self, s):
		visited = [False] * (max(self.graph) + 1)
		# Create a queue for BFS
		queue = []
		queue.append(s)
		visited[s] = True
		while queue:
			s = queue.pop(0)
			print(s, end=" ")
			for i in self.graph[s]:
				if visited[i] == False:
					queue.append(i)
					visited[i] = True
# Driver code
if __name__ == '__main__':
	# Create a graph given in the above diagram
	g = Graph()
	g.addEdge(0, 1)
	g.addEdge(0, 2)
	g.addEdge(1, 2)
	g.addEdge(2, 0)
	g.addEdge(2, 3)
	g.addEdge(3, 3)

	print("Following is Breadth First Traversal"
		" (starting from vertex 2)")
	g.BFS(2)


