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

csvfile1=file('E:\dataProgram\datasets\PRA_AverageClustering.csv','wb')
writer1=csv.writer(csvfile1)
#writer1.writerow(['source','target','averageClusteringCoefficient'])

#writer1.writerow(['null',nx.average_clustering(subG)])
#print edge_list[1]
average=nx.average_clustering(subG)
for i in range(0,len(edge_list)):
	#print edge_list[i]
	temp=edge_list[i]
	subG.remove_edge(*edge_list[i])
	average1=nx.average_clustering(subG)
	writer1.writerow([temp[0],temp[1],average1,average-average1])
	subG.add_edge(*temp)
#print subG.edges()