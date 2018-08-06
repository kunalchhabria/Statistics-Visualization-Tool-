states=['AGGREGATED_andhra_pradesh.txt', 'AGGREGATED_arrunachal_pradesh.txt', 'AGGREGATED_assam.txt', 'AGGREGATED_bihar.txt', 'AGGREGATED_delhi.txt', 'AGGREGATED_goa.txt', 'AGGREGATED_Guj.txt', 'AGGREGATED_Haryana.txt', 'AGGREGATED_jharkhand.txt', 'AGGREGATED_JK.txt', 'AGGREGATED_karnataka.txt', 'AGGREGATED_kerala.txt', 'AGGREGATED_Maharashtra.txt', 'AGGREGATED_manipur.txt', 'AGGREGATED_meghalaya.txt', 'AGGREGATED_mizoram.txt', 'AGGREGATED_MP.txt', 'AGGREGATED_nagaland.txt', 'AGGREGATED_punjab.txt', 'AGGREGATED_rajasthan.txt', 'AGGREGATED_sikkim.txt', 'AGGREGATED_telangana.txt', 'AGGREGATED_TN.txt', 'AGGREGATED_tripura.txt', 'AGGREGATED_UP.txt', 'AGGREGATED_uttarakhand.txt', 'AGGREGATED_WB.txt']
test=states[0]
attributes=[]
temp=open(test,'r')
for line in temp:
	values=line.split()[1:-1]
	values=' '.join(values)
	attributes.append(values)
temp.close()

import sys
final_matrix=[]
for state in states:
	attribute_list=[]
	temp=open(state,'r')
	for lines in temp:
		value=lines.split()[-1]
		value=float(value)
		attribute_list.append(value)
	final_matrix.append(attribute_list)
	temp.close()

states1=['andhra_pradesh.csv', 'arrunachal_pradesh.csv', 'assam.csv', 'bihar.csv', 'delhi.csv', 'goa.csv', 'Guj.csv', 'Haryana.csv', 'jharkhand.csv', 'JK.csv', 'karnataka.csv', 'kerala.csv', 'Maharashtra.csv', 'manipur.csv', 'meghalaya.csv', 'mizoram.csv', 'MP.csv', 'nagaland.csv', 'punjab.csv', 'rajasthan.csv', 'sikkim.csv', 'telangana.csv', 'TN.csv', 'tripura.csv', 'UP.csv', 'uttarakhand.csv', 'WB.csv']
while(True):
	count_state=0
	for i in states1:
		print(count_state,'.  ',i[:-4])
		count_state+=1
	print('Enter the indexes of the states separated by space:')
	input_states=input().split()
	input_states1=[]
	for i in input_states:
		input_states1.append(int(i))
	print(input_states1)

	input_states1.sort()
	print(input_states1)
	count_attributes=0
	for i in attributes:
		print(count_attributes,'.  ',i)
		count_attributes+=1
	print('Enter the index of the attribute:')
	input_attribute=int(input())

	final_array=[]
	for i in input_states1:
		final_array.append(float(str(round(final_matrix[i][input_attribute], 2))))


	print(final_array)

	import matplotlib.pyplot as plt; plt.rcdefaults()
	import numpy as np
	import matplotlib.pyplot as plt
	plt.style.use('ggplot')

	objects=[]
	for i in input_states1:
		objects.append(states1[i][:-4])


	y_pos = np.arange(len(objects))
	performance = final_array
	 
	plt.bar(y_pos, performance, align='center', alpha=0.65)
	plt.xticks(y_pos, objects)
	plt.ylabel(attributes[input_attribute])
	plt.title(attributes[input_attribute])
	for a,b in zip(y_pos, performance):
	    plt.text(a, b, str(b), color='blue', fontweight='bold',horizontalalignment ='center')
	plt.show()

	print('Do you want to continue: Y/N:')
	con=input()
	if con=='N':
		sys.exit()

