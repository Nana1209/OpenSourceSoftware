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

#the size of Laplacian matrix
len=len(node_list)
L=zeros([len,len])
#new Laplacian matrix
for i in range(0,len):
	for j in range(0,len):
		if i==j:
			L[i,j]=nx.degree(subG,node_list[i])
		elif nx.has_path(subG,node_list[i],node_list[j]):
			L[i,j]=-1
		else:
			L[i,j]=0
#the Pseudo inverse matrix of L
Lpi=linalg.pinv(L)

csvfile1=file('E:\dataProgram\datasets\ACT_Sxy.csv','wb')
writer1=csv.writer(csvfile1)
writer1.writerow(['Sx','Sy','Sxy(ACT)'])

#Sxy(basic average commute time)
for i in range(0,len):
	for j in range(i,len):
		Sxy=1/(Lpi[i,i]+Lpi[j,j]-2*Lpi[i,j])
		writer1.writerow([node_list[i],node_list[j],Sxy])



