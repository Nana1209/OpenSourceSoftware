import csv

r1=open('E:\dataProgram\datasets\PRA_AverageClustering.csv','r')
csvReader1=csv.reader(r1)


r2=open('E:\dataProgram\datasets\Collaborations_PRA.csv','r')
csvReader2=csv.reader(r2)

addA={}
addB={}


w=open('E:\dataProgram\datasets\PRA_suBYearAverageClustering.csv','wb')
writer1=csv.writer(w)
writer1.writerow(['source','target','averageClusteringCoefficient','sub','hasIn1Y','hasIn2Y','hasIn3Y','hasIn4Y','hasIn5Y','hasIn6Y','hasIn7Y','hasIn8Y','hasIn9Y','hasIn10Y','hasIn11Y','hasIn12Y','hasIn13Y','hasIn14Y','hasIn15Y','hasIn16Y','hasIn17Y','hasIn18Y','hasIn19Y','hasIn20Y'])
for m,row1 in enumerate(csvReader1):
	addA[m]=row1
for n,row2 in enumerate(csvReader2):
	addB[n]=row2
for i in range(len(addA)):
	for j in range(len(addB)):
		if (addA[i][0]==addB[j][0] and addA[i][1]==addB[j][1]) or (addA[i][1]==addB[j][0] and addA[i][0]==addB[j][1]):
			#print (1)
			in93=addB[j][3]
			in94=addB[j][4]+addB[j][3]
			in95=addB[j][5]+addB[j][4]+addB[j][3]
			in96=addB[j][6]+addB[j][5]+addB[j][4]+addB[j][3]
			in97=addB[j][7]+addB[j][6]+addB[j][5]+addB[j][4]+addB[j][3]
			in98=addB[j][8]+addB[j][7]+addB[j][6]+addB[j][5]+addB[j][4]+addB[j][3]
			in99=addB[j][9]+addB[j][8]+addB[j][7]+addB[j][6]+addB[j][5]+addB[j][4]+addB[j][3]
			in00=addB[j][10]+addB[j][9]+addB[j][8]+addB[j][7]+addB[j][6]+addB[j][5]+addB[j][4]+addB[j][3]
			in01=addB[j][11]+addB[j][10]+addB[j][9]+addB[j][8]+addB[j][7]+addB[j][6]+addB[j][5]+addB[j][4]+addB[j][3]
			in02=addB[j][12]+addB[j][11]+addB[j][10]+addB[j][9]+addB[j][8]+addB[j][7]+addB[j][6]+addB[j][5]+addB[j][4]+addB[j][3]
			in03=addB[j][13]+addB[j][12]+addB[j][11]+addB[j][10]+addB[j][9]+addB[j][8]+addB[j][7]+addB[j][6]+addB[j][5]+addB[j][4]+addB[j][3]
			in04=addB[j][14]+addB[j][13]+addB[j][12]+addB[j][11]+addB[j][10]+addB[j][9]+addB[j][8]+addB[j][7]+addB[j][6]+addB[j][5]+addB[j][4]+addB[j][3]
			in05=addB[j][15]+addB[j][14]+addB[j][13]+addB[j][12]+addB[j][11]+addB[j][10]+addB[j][9]+addB[j][8]+addB[j][7]+addB[j][6]+addB[j][5]+addB[j][4]+addB[j][3]
			in06=addB[j][16]+addB[j][15]+addB[j][14]+addB[j][13]+addB[j][12]+addB[j][11]+addB[j][10]+addB[j][9]+addB[j][8]+addB[j][7]+addB[j][6]+addB[j][5]+addB[j][4]+addB[j][3]
			in07=addB[j][17]+addB[j][16]+addB[j][15]+addB[j][14]+addB[j][13]+addB[j][12]+addB[j][11]+addB[j][10]+addB[j][9]+addB[j][8]+addB[j][7]+addB[j][6]+addB[j][5]+addB[j][4]+addB[j][3]
			in08=addB[j][18]+addB[j][17]+addB[j][16]+addB[j][15]+addB[j][14]+addB[j][13]+addB[j][12]+addB[j][11]+addB[j][10]+addB[j][9]+addB[j][8]+addB[j][7]+addB[j][6]+addB[j][5]+addB[j][4]+addB[j][3]
			in09=addB[j][19]+addB[j][18]+addB[j][17]+addB[j][16]+addB[j][15]+addB[j][14]+addB[j][13]+addB[j][12]+addB[j][11]+addB[j][10]+addB[j][9]+addB[j][8]+addB[j][7]+addB[j][6]+addB[j][5]+addB[j][4]+addB[j][3]
			in10=addB[j][20]+addB[j][19]+addB[j][18]+addB[j][17]+addB[j][16]+addB[j][15]+addB[j][14]+addB[j][13]+addB[j][12]+addB[j][11]+addB[j][10]+addB[j][9]+addB[j][8]+addB[j][7]+addB[j][6]+addB[j][5]+addB[j][4]+addB[j][3]
			in11=addB[j][21]+addB[j][20]+addB[j][19]+addB[j][18]+addB[j][17]+addB[j][16]+addB[j][15]+addB[j][14]+addB[j][13]+addB[j][12]+addB[j][11]+addB[j][10]+addB[j][9]+addB[j][8]+addB[j][7]+addB[j][6]+addB[j][5]+addB[j][4]+addB[j][3]
			in12=addB[j][22]+addB[j][21]+addB[j][20]+addB[j][19]+addB[j][18]+addB[j][17]+addB[j][16]+addB[j][15]+addB[j][14]+addB[j][13]+addB[j][12]+addB[j][11]+addB[j][10]+addB[j][9]+addB[j][8]+addB[j][7]+addB[j][6]+addB[j][5]+addB[j][4]+addB[j][3]
			# twenty=addB[j][22]+addB[j][21]+addB[j][20]+addB[j][19]+addB[j][18]+addB[j][17]+addB[j][16]+addB[j][15]+addB[j][14]+addB[j][13]+addB[j][12]+addB[j][11]+addB[j][10]+addB[j][9]+addB[j][8]+addB[j][7]+addB[j][6]+addB[j][5]+addB[j][4]+addB[j][3]
			# nineteen=addB[j][22]+addB[j][21]+addB[j][20]+addB[j][19]+addB[j][18]+addB[j][17]+addB[j][16]+addB[j][15]+addB[j][14]+addB[j][13]+addB[j][12]+addB[j][11]+addB[j][10]+addB[j][9]+addB[j][8]+addB[j][7]+addB[j][6]+addB[j][5]+addB[j][4]
			# eighteen=addB[j][22]+addB[j][21]+addB[j][20]+addB[j][19]+addB[j][18]+addB[j][17]+addB[j][16]+addB[j][15]+addB[j][14]+addB[j][13]+addB[j][12]+addB[j][11]+addB[j][10]+addB[j][9]+addB[j][8]+addB[j][7]+addB[j][6]+addB[j][5]
			# seventeen=addB[j][22]+addB[j][21]+addB[j][20]+addB[j][19]+addB[j][18]+addB[j][17]+addB[j][16]+addB[j][15]+addB[j][14]+addB[j][13]+addB[j][12]+addB[j][11]+addB[j][10]+addB[j][9]+addB[j][8]+addB[j][7]+addB[j][6]
			# sixteen=addB[j][22]+addB[j][21]+addB[j][20]+addB[j][19]+addB[j][18]+addB[j][17]+addB[j][16]+addB[j][15]+addB[j][14]+addB[j][13]+addB[j][12]+addB[j][11]+addB[j][10]+addB[j][9]+addB[j][8]+addB[j][7]
			# fifteen=addB[j][22]+addB[j][21]+addB[j][20]+addB[j][19]+addB[j][18]+addB[j][17]+addB[j][16]+addB[j][15]+addB[j][14]+addB[j][13]+addB[j][12]+addB[j][11]+addB[j][10]+addB[j][9]+addB[j][8]
			# fourteen=addB[j][22]+addB[j][21]+addB[j][20]+addB[j][19]+addB[j][18]+addB[j][17]+addB[j][16]+addB[j][15]+addB[j][14]+addB[j][13]+addB[j][12]+addB[j][11]+addB[j][10]+addB[j][9]
			# thirteen=addB[j][22]+addB[j][21]+addB[j][20]+addB[j][19]+addB[j][18]+addB[j][17]+addB[j][16]+addB[j][15]+addB[j][14]+addB[j][13]+addB[j][12]+addB[j][11]+addB[j][10]
			# twelve=addB[j][22]+addB[j][21]+addB[j][20]+addB[j][19]+addB[j][18]+addB[j][17]+addB[j][16]+addB[j][15]+addB[j][14]+addB[j][13]+addB[j][12]+addB[j][11]
			# eleven=addB[j][22]+addB[j][21]+addB[j][20]+addB[j][19]+addB[j][18]+addB[j][17]+addB[j][16]+addB[j][15]+addB[j][14]+addB[j][13]+addB[j][12]
			# ten=addB[j][22]+addB[j][21]+addB[j][20]+addB[j][19]+addB[j][18]+addB[j][17]+addB[j][16]+addB[j][15]+addB[j][14]+addB[j][13]
			# nine=addB[j][22]+addB[j][21]+addB[j][20]+addB[j][19]+addB[j][18]+addB[j][17]+addB[j][16]+addB[j][15]+addB[j][14]
			# eight=addB[j][22]+addB[j][21]+addB[j][20]+addB[j][19]+addB[j][18]+addB[j][17]+addB[j][16]+addB[j][15]
			# seven=addB[j][22]+addB[j][21]+addB[j][20]+addB[j][19]+addB[j][18]+addB[j][17]+addB[j][16]
			# six=addB[j][22]+addB[j][21]+addB[j][20]+addB[j][19]+addB[j][18]+addB[j][17]
			# five=addB[j][22]+addB[j][21]+addB[j][20]+addB[j][19]+addB[j][18]
			# four=addB[j][22]+addB[j][21]+addB[j][20]+addB[j][19]
			# three=addB[j][22]+addB[j][21]+addB[j][20]
			# two=addB[j][22]+addB[j][21]
			# one=addB[j][22]
			# print int(one)>0
			# print int(two)
			# print int(one)+int(two)
			writer1.writerow([addA[i][0],addA[i][1],addA[i][2],addA[i][3],int(in93)>0,int(in94)>0,int(in95)>0,int(in96)>0,int(in97)>0,int(in98)>0,int(in99)>0,int(in00)>0,int(in01)>0,int(in02)>0,int(in03)>0,int(in04)>0,int(in05)>0,int(in06)>0,int(in07)>0,int(in08)>0,int(in09)>0,int(in10)>0,int(in11)>0,int(in12)>0])
			#writer1.writerow([addA[i][0],addA[i][1],addA[i][2],addA[i][3],int(fifteen)>0])
			break			
		
		# if addA[i][1]==addB[j][0] and addA[i][0]==addB[j][1]:
		# 	#print (2)
		# 	fifteen=addB[j][22]+addB[j][21]+addB[j][20]+addB[j][19]+addB[j][18]+addB[j][17]+addB[j][16]+addB[j][15]+addB[j][14]+addB[j][13]+addB[j][12]+addB[j][11]+addB[j][10]+addB[j][9]+addB[j][8]
		# 	writer1.writerow([addA[i][0],addA[i][1],addA[i][2],addA[i][3],int(fifteen)>0])
		# 	break

