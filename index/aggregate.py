delhi=open('upout.txt','w')
states=['andhra_pradesh.csv', 'arrunachal_pradesh.csv', 'assam.csv', 'bihar.csv', 'delhi.csv', 'goa.csv', 'Guj.csv', 'Haryana.csv', 'jharkhand.csv', 'JK.csv', 'karnataka.csv', 'kerala.csv', 'Maharashtra.csv', 'manipur.csv', 'meghalaya.csv', 'mizoram.csv', 'MP.csv', 'nagaland.csv', 'punjab.csv', 'rajasthan.csv', 'sikkim.csv', 'telangana.csv', 'TN.csv', 'tripura.csv', 'UP.csv', 'uttarakhand.csv', 'WB.csv']
import csv
for i in states:
	name='AGGREGATED_'
	dot=i.index('.')
	name+=i[:dot]+'.txt'
	outputfile=open(name,'w')
	data=open(i)
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
			outputfile.write(attribute_write)
		except:
			lol=0
		temp+=1
		#print(temp,attribute,avg)

