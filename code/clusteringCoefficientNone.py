import networkx as nx
from numpy import *

import csv
import networkx as nx
G=nx.Graph()
csvReader=csv.reader(file('E:\dataProgram\datasets\Collaborations_PRA.csv','rb'))
#creat Graph
for row in csvReader:
	G.add_edge(row[0],row[1])
#creat the largest connected component
largest_cc = max(nx.connected_components(G), key=len)
subG=G.subgraph(largest_cc)

edge_list=subG.edges()
node_list=subG.nodes()

csvfile1=file('E:\dataProgram\datasets\clusteringCoefficientNone.csv','wb')
writer1=csv.writer(csvfile1)
writer1.writerow(['Node','clusteringCoefficient'])

for i in range(0,len(node_list)):
	#print nx.clustering(subG,node_list[i])
	writer1.writerow([node_list[i],nx.clustering(subG,node_list[i])])
