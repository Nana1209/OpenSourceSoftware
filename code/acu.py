import csv

r1=open('E:\dataProgram\data\DBLP_yearCluWU_order.csv','r')
csvReader1=csv.reader(r1)

csvfile1=file('E:\dataProgram\data\DBLP_AUC(WU).csv','wb')
writer1=csv.writer(csvfile1)

tableA={}

arrayF={}
arrayT={}

for m,row1 in enumerate(csvReader1):
	tableA[m]=row1
for k in range(20):
	m=0
	n=0
	for i in range(len(tableA)):
		if tableA[i][4+k]=='FALSE':
			#print tableA[i][3]
			arrayF[m]=tableA[i][3]
			m=m+1
		else:
			arrayT[n]=tableA[i][3]
			n=n+1
	tempa=0;
	auc=0;
	for i in range(m):
		for j in range(n):
			if arrayF[i]<arrayT[j]:
				tempa=tempa+1
				#print 1
			if arrayF[i]==arrayT[j]:
				tempa=tempa+0.5
				#print 11
	auc=tempa/(m*n)
	writer1.writerow([93+k,auc])
	print auc
#print n,m