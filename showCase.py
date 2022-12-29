class graph:
	def __init__(self):
		self.graph = dict()

	def addVertex(self, node):
		self.graph[node] = list()

	def addEdge(self, node, value):
		if value in self.graph[node]:
			return
		self.graph[node].append(value)
		if value in self.graph.keys():
			self.graph[value].append(node)

	def printGraph(self):
		for i in self.graph.keys():
			print(f'{i}-->{self.graph[i]}')

	""" 
        def showGraph(self):
          for i in self.GraphC:
            print('{} --> {}'.format(i, list(set(self.GraphC[i]))))
    """

	def bfs(self, src):
		if src not in self.graph.keys():
			print("Node Not Available")
		else:
			v, q = list(), list()
			v.append(src)
			q.append(src)
			while q:
				k = self.graph[q[0]]
				print(q.pop(0), end=' ')
				for z in k:
					if z not in v:
						v.append(z)
						q.append(z)

	def dfs_h(self, src_, v, g):
		print(src_, end=',')
		v.append(src_)
		for i in range(len(g[src_])):
			if g[src_][i] in v:
				continue
			else:
				self.dfs_h(g[src_][i], v, g)
		return

	def dfs(self, src):
		v = list()
		self.dfs_h(src, v, self.graph)
		print()

	def findOne(self, a):
		val, v = list(), list()
		sum = 0
		for i in range(len(a)):
			for j in range(len(a[i])):
				if a[i][j] == 0:
					v += [(i, j)]
				if (i, j) in v:
					continue
				if a[i][j] == 1:
					k, d = i, j
					self.IfOne(i, j, v, a, sum)
					val.append(sum)
					sum = 0
					i, j = k, d
		print(val)

	def IfOne(self, i, j, v, a, sum):
		try:
			if a[i][j] != 1:
				return
			else:
				if (i, j) in v:
					return
				else:
					sum += 1
					v += [i, j]
				self.IfOne(i, j + 1, a, sum)
				self.IfOne(i, j - 1, a, sum)
				self.IfOne(i - 1, j, a, sum)
				self.IfOne(i + 1, j, a, sum)
		except:
			return


c = graph()
c.addVertex('0')
c.addVertex('1')
c.addVertex('2')
c.addVertex('3')
c.addVertex('4')
c.addVertex('5')
c.addVertex('6')
c.addVertex('60')
c.addEdge('3', '6')
c.addEdge('3', '2')
c.addEdge('3', '1')
c.addEdge('3', '4')
c.addEdge('0', '1')
c.addEdge('0', '2')
c.addEdge('2', '4')
c.addEdge('2', '1')
c.addEdge('4', '5')
c.addEdge('5', '6')
c.addEdge('1', '2')
c.addEdge('60', '3')
c.addEdge('60', '3')
c.printGraph()
c.bfs('60')
print()
c.dfs('60')
a=[[1,0,0,1,0],
   [1,0,0,1,1],
  [0,0,0,1,1]]
c.findOne()
