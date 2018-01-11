import csv

r1=open('E:\dataProgram\datasets\PRA_suBYearAverageClustering.csv','r')
csvReader1=csv.reader(r1)

addA={}

for m,row1 in enumerate(csvReader1):
	addA[m]=row1
sum=[]
real1=0
for j in range(4,24):
	ss=0
	for i in range(len(addA)):
		if(addA[i][j]=='FALSE'):
			ss=ss+1
	sum.append(ss)
#print sum
#sum1=int(sum*0.1)
# s=[]
# acc=[]
# r=[]
a=[]

for z in range(len(sum)):
	s=[]
	acc=[]
	r=[]
	for j in range(10):
		s.append(int(sum[z]*(0.1*(j+1))))
		real=0
		for i in range(s[j]):
			if(addA[i][4+z]=='FALSE'):
				real=real+1
		r.append(real)

		acc.append(float(r[j])/float(s[j]))
		print float(r[j])/float(s[j])
	a.append(acc)

#print a
w=open('E:\dataProgram\data\PRA_Accuracy.csv','wb')
writer1=csv.writer(w)
for i in range(20):
	writer1.writerow(a[i])