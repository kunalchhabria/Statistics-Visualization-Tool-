delhi=open('upout.txt','w')
import csv
data=open('UP.csv')
data=csv.reader(data)
temp=0
data=list(data)
for lines in data[4:]:
	
	attribute=lines[0]
	values=lines[1:]
	avg=0
	count=0
	bad=['NA','*','']
	for i in values:
		if not i.strip() in bad:
			try:
				avg+=abs(float(i))
				count+=1
			except:
				lol=0
	try:
		avg=avg/count
		attribute_write=attribute+' '+str(avg)+'\n'
		delhi.write(attribute_write)
	except:
		lol=0
	temp+=1
	print(temp,attribute,avg)

