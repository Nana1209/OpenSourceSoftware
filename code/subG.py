import csv
import networkx as nx
G=nx.Graph()
Gw=nx.Graph()
csvReader=csv.reader(file('E:\dataProgram\datasets\Collaborations_PRA.csv','rb'))
#creat Graph
for row in csvReader:
	Gw.add_edge(row[0],row[1],weight=row[2])
	G.add_edge(row[0],row[1])
#creat the largest connected component
largest_cc = max(nx.connected_components(G), key=len)
largest_ccw = max(nx.connected_components(Gw), key=len)
subG=G.subgraph(largest_cc)
subGw=Gw.subgraph(largest_ccw)


edge_list=subG.edges()
node_list=subG.nodes()

print G.get_edge_data(edge_list[0][0],edge_list[0][1]) 
print nx.average_clustering(subG)
print nx.average_clustering(subGw)