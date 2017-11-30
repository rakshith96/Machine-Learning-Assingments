class Cluster:
	def __init__(self):
		pass
	def __repr__(self):
		return '(%s,%s)' % (self.left, self.right)
	def add(self, clusters, grid, lefti, righti):
		self.left = clusters[lefti]
		self.right = clusters[righti]
		# merge columns grid[row][righti] and row grid[righti] into corresponding lefti
		for r in grid:
			r[lefti] = min(r[lefti], r.pop(righti))
		grid[lefti] = list(map(min, zip(grid[lefti], grid.pop(righti))))
		clusters.pop(righti)
		return (clusters, grid)

def agglomerate(labels, grid):
	"""
	given a list of labels and a 2-D grid of distances, iteratively agglomerate
	hierarchical Cluster
	"""
	clusters = labels
	while len(clusters) > 1:
		# find 2 closest clusters
		print(clusters)
		distances = [(1, 0, grid[1][0])]
		for i,row in enumerate(grid[2:]):
			distances += [(i+2, j, c) for j,c in enumerate(row[:i+2])]
		j,i,_ = min(distances, key=lambda x:x[2])
		# merge i<-j
		c = Cluster()
		clusters, grid = c.add(clusters, grid, i, j)
		clusters[i] = c
	return clusters.pop()

if __name__ == '__main__':

	# Ref #1
	ItalyCities = ['BA','FI','MI','NA','RM','TO']
	ItalyDistances = [
		[  0, 662, 877, 255, 412, 996],
		[662,   0, 295, 468, 268, 400],
		[877, 295,   0, 754, 564, 138],
		[255, 468, 754,   0, 219, 869],
		[412, 268, 564, 219,   0, 669],
		[996, 400, 138, 869, 669,   0]]
	print(agglomerate(ItalyCities, ItalyDistances))

