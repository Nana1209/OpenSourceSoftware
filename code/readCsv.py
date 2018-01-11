import csv
import networkx as nx
import matplotlib.pyplot as plt
from networkx.algorithms import approximation as approx
# G=nx.Graph()
# csvReader=csv.reader(file('E:\dataProgram\datasets\Collaborations_PRA.csv','rb'))
# #creat Graph
# for row in csvReader:
# 	G.add_edge(row[0],row[1])
# #creat the largest connected component
# largest_cc = max(nx.connected_components(G), key=len)
# subG=G.subgraph(largest_cc)

# edge_list=subG.edges()
# node_list=subG.nodes()


# def nodeCon(edge_list,subG):
# 	csvfile=file('E:\dataProgram\datasets\NodeConnectivity.csv','wb')
# 	writer=csv.writer(csvfile)
# 	writer.writerow(['Source','Target','nodeConnectivity'])
# 	for row in edge_list:
# 		value= approx.node_connectivity(subG,row[0],row[1])
# 		writer.writerow([row[0],row[1],value])

# print approx.all_pairs_node_connectivity(subG)
# def allPairNodeCon(edge_list,subG):
# 	print approx.all_pairs_node_connectivity(subG)
	
# allPairNodeCon(edge_list,subG)


# csvfile1=file('E:\dataProgram\datasets\CN_Sxy.csv','wb')
# writer1=csv.writer(csvfile1)
# writer1.writerow(['Sx','Sy','comNeiNum'])
# for i in range(0,len(node_list)):
# 	for j in range(i,len(node_list)):
# 		comNeiNum=len(list(nx.common_neighbors(subG, node_list[i], node_list[j])))
# 		writer1.writerow([node_list[i],node_list[j],comNeiNum])

# nx.draw(subG)
# plt.savefig("youxiangtu.png")
# plt.show()
# nx.draw(subG
G=nx.Graph()
G.add_edge('1', '2')
G.add_edge('2', '3')
G.add_edge('4', '3')
G.add_edge('2', '4')
print G.number_of_nodes()
G.remove_edge('1','2')
print G.edges()
print G.number_of_nodes()