import csv

csvReader1=csv.reader(file('E:\dataProgram\datasets\AverageClustering1.csv','rb'))
csvReader2=csv.reader(file('E:\dataProgram\datasets\Collaborations_PRA.csv','rb'))

csvfile1=file('E:\dataProgram\datasets\suBYearAverageClustering1.csv','wb')
writer1=csv.writer(csvfile1)
writer1.writerow(['source','target','averageClusteringCoefficient','sub','hasIn1Y','hasIn2Y','hasIn3Y','hasIn4Y','hasIn5Y','hasIn6Y','hasIn7Y','hasIn8Y','hasIn9Y','hasIn10Y','hasIn11Y','hasIn12Y','hasIn13Y','hasIn14Y','hasIn15Y','hasIn16Y','hasIn17Y','hasIn18Y','hasIn19Y','hasIn20Y'])

for row1 in csvReader1:
	for row2 in csvReader2:
		if (row1[0]==row2[0] and row1[1]==row2[1]) or (row1[0]==row2[1] and row1[1]==row2[0]):
			print 2
			# twenty=row2[22]+row2[21]+row2[20]+row2[19]+row2[18]+row2[17]+row2[16]+row2[15]+row2[14]+row2[13]+row2[12]+row2[11]+row2[10]+row2[9]+row2[8]+row2[7]+row2[6]+row2[5]+row2[4]+row2[3]
			# nineteen=row2[22]+row2[21]+row2[20]+row2[19]+row2[18]+row2[17]+row2[16]+row2[15]+row2[14]+row2[13]+row2[12]+row2[11]+row2[10]+row2[9]+row2[8]+row2[7]+row2[6]+row2[5]+row2[4]
			# eighteen=row2[22]+row2[21]+row2[20]+row2[19]+row2[18]+row2[17]+row2[16]+row2[15]+row2[14]+row2[13]+row2[12]+row2[11]+row2[10]+row2[9]+row2[8]+row2[7]+row2[6]+row2[5]
			# seventeen=row2[22]+row2[21]+row2[20]+row2[19]+row2[18]+row2[17]+row2[16]+row2[15]+row2[14]+row2[13]+row2[12]+row2[11]+row2[10]+row2[9]+row2[8]+row2[7]+row2[6]
			# sixteen=row2[22]+row2[21]+row2[20]+row2[19]+row2[18]+row2[17]+row2[16]+row2[15]+row2[14]+row2[13]+row2[12]+row2[11]+row2[10]+row2[9]+row2[8]+row2[7]
			fifteen=row2[22]+row2[21]+row2[20]+row2[19]+row2[18]+row2[17]+row2[16]+row2[15]+row2[14]+row2[13]+row2[12]+row2[11]+row2[10]+row2[9]+row2[8]
			# fourteen=row2[22]+row2[21]+row2[20]+row2[19]+row2[18]+row2[17]+row2[16]+row2[15]+row2[14]+row2[13]+row2[12]+row2[11]+row2[10]+row2[9]
			# thirteen=row2[22]+row2[21]+row2[20]+row2[19]+row2[18]+row2[17]+row2[16]+row2[15]+row2[14]+row2[13]+row2[12]+row2[11]+row2[10]
			# twelve=row2[22]+row2[21]+row2[20]+row2[19]+row2[18]+row2[17]+row2[16]+row2[15]+row2[14]+row2[13]+row2[12]+row2[11]
			# eleven=row2[22]+row2[21]+row2[20]+row2[19]+row2[18]+row2[17]+row2[16]+row2[15]+row2[14]+row2[13]+row2[12]
			# ten=row2[22]+row2[21]+row2[20]+row2[19]+row2[18]+row2[17]+row2[16]+row2[15]+row2[14]+row2[13]
			# nine=row2[22]+row2[21]+row2[20]+row2[19]+row2[18]+row2[17]+row2[16]+row2[15]+row2[14]
			# eight=row2[22]+row2[21]+row2[20]+row2[19]+row2[18]+row2[17]+row2[16]+row2[15]
			# seven=row2[22]+row2[21]+row2[20]+row2[19]+row2[18]+row2[17]+row2[16]
			# six=row2[22]+row2[21]+row2[20]+row2[19]+row2[18]+row2[17]
			# five=row2[22]+row2[21]+row2[20]+row2[19]+row2[18]
			# four=row2[22]+row2[21]+row2[20]+row2[19]
			# three=row2[22]+row2[21]+row2[20]
			# two=row2[22]+row2[21]
			# one=row2[22]
			# print int(one)>0
			# print int(two)
			# print int(one)+int(two)
			#writer1.writerow([row1[0],row1[1],row1[2],row1[3],int(one)>0,int(two)>0,int(three)>0,int(four)>0,int(five)>0,int(six)>0,int(seven)>0,int(eight)>0,int(nine)>0,int(ten)>0,int(eleven)>0,int(twelve)>0,int(thirteen)>0,int(fourteen)>0,int(fifteen)>0,int(sixteen)>0,int(seventeen)>0,int(eighteen)>0,int(nineteen)>0,int(twenty)>0])
			writer1.writerow([row1[0],row1[1],row1[2],row1[3],int(fifteen)>0])
			
			#break
		else:
			continue
