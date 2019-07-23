import sys
from math import sqrt
from math import pow
from math import exp


def ReadData():
	#global XValues
	#global MVvlaues_A   #holds the mean and variance values of class A 1D list
	#global MVvlaues_B   #holds the mean and variance values of class B 1D list
	#global Total_number_of_A #count of instances of class A
	#global Total_number_of_B 	#count of instances of class B


	XValues = []
	i=0
	flag = 0
	MVvlaues_A = []  #holds the mean and variance values of class A 1D list
	MVvlaues_B = []  #holds the mean and variance values of class B 1D list
	Attributes = 0
	Total_number_of_A = 0	#count of instances of class A
	Total_number_of_B = 0	#count of instances of class B
	counter = 0


	for line in datafile:
		XValues.insert(i,line.split("\t"))		
		if(flag == 0):
			l = len(XValues[i])
			print(XValues[i])
			Attributes = (l-2)
			for j in range(0,Attributes*2+1): 
				MVvlaues_A.insert(j,0.0)
				MVvlaues_B.insert(j,0.0)
			flag = 1			
		if(XValues[i][0] == 'A'):
			Total_number_of_A+=1
			#print(MVvlaues_A[0])
			#print(XValues[i][1])
			#print(type(XValues[i][1]))
			#print(type(MVvlaues_A[0]))
			MVvlaues_A[0] = float(XValues[i][1])+MVvlaues_A[0]
			MVvlaues_A[2] = float(XValues[i][2])+MVvlaues_A[2]			
		else:
			Total_number_of_B+=1
			MVvlaues_B[0] = float(XValues[i][1])+MVvlaues_B[0]
			MVvlaues_B[2] = float(XValues[i][2])+MVvlaues_B[2]
		i = i+1


	MVvlaues_A[0] = MVvlaues_A[0] / Total_number_of_A
	MVvlaues_A[2] = MVvlaues_A[2] / Total_number_of_A
	MVvlaues_B[0] = MVvlaues_B[0] / Total_number_of_B 
	MVvlaues_B[2] = MVvlaues_B[2] / Total_number_of_B 
	MVvlaues_B[Attributes*2] = Total_number_of_B / (Total_number_of_A + Total_number_of_B)
	MVvlaues_A[Attributes*2] = Total_number_of_A / (Total_number_of_A + Total_number_of_B)
	CalVariance(XValues,MVvlaues_A,MVvlaues_B,Total_number_of_A,Total_number_of_B)
	CalGuassian(XValues,MVvlaues_A,MVvlaues_B)

	
def CalVariance(XValues,MVvlaues_A,MVvlaues_B,Total_number_of_A = 0,Total_number_of_B = 0):


	i=0


	for line in XValues:
		if(XValues[i][0] == 'A'):
			MVvlaues_A[1] = MVvlaues_A[1]+(float(XValues[i][1])-MVvlaues_A[0])**2
			MVvlaues_A[3] = MVvlaues_A[3]+(float(XValues[i][2])-MVvlaues_A[2])**2
		else:
			MVvlaues_B[1] =  MVvlaues_B[1]+(float(XValues[i][1])-MVvlaues_B[0])**2
			MVvlaues_B[3] = MVvlaues_B[3]+(float(XValues[i][2])-MVvlaues_B[2])**2
		i+=1
	MVvlaues_A[1] = MVvlaues_A[1] /(Total_number_of_A-1)
	MVvlaues_A[3] = MVvlaues_A[3] /(Total_number_of_A-1)
	MVvlaues_B[1] = MVvlaues_B[1] /(Total_number_of_B-1)
	MVvlaues_B[3] = MVvlaues_B[3] /(Total_number_of_B-1)

	
def CalGuassian(XValues,MVvlaues_A,MVvlaues_B):


	Guass_of_A = []
	Guass_of_B = []
	i=0
	counter = 0
	
	
	for line in XValues:
		Cal1 = ((1/(sqrt(2*3.14*MVvlaues_A[1])))*(exp(-1*(pow((float(XValues[i][1])-MVvlaues_A[0]),2)/(2*MVvlaues_A[1])))))
		Cal2 = ((1/(sqrt(2*3.14*MVvlaues_A[3])))*(exp(-1*(pow((float(XValues[i][2])-MVvlaues_A[2]),2)/(2*MVvlaues_A[3])))))
		Guass_of_A.insert(i,(Cal1,Cal2))
		Cal1 = ((1/(sqrt(2*3.14*MVvlaues_B[1])))*(exp(-1*(pow((float(XValues[i][1])-MVvlaues_B[0]),2)/(2*MVvlaues_B[1])))))
		Cal2 = ((1/(sqrt(2*3.14*MVvlaues_B[3])))*(exp(-1*(pow((float(XValues[i][2])-MVvlaues_B[2]),2)/(2*MVvlaues_B[3])))))
		Guass_of_B.insert(i,(Cal1,Cal2))
		i+=1
	
	
	i = 0
	ProA = 0.0
	ProB = 0.0
	
	
	for line in XValues:
		ProA = MVvlaues_A[4] * Guass_of_A[i][0] * Guass_of_A[i][1]
		ProB = MVvlaues_B[4] * Guass_of_B[i][0] * Guass_of_B[i][1]
		if((ProA<ProB) and XValues[i][0] == 'A'):
			counter += 1
		if((ProA>ProB) and XValues[i][0] == 'B'):
			counter += 1	
		i+=1
	
	
	WriteData(MVvlaues_A,MVvlaues_B,counter)

	
def WriteData(MVvlaues_A,MVvlaues_B,counter):
	
	
	with open(outputfile, "a+") as output:
		for i in range((len(MVvlaues_A)-1)):
			output.write(str(MVvlaues_A[i]))
			output.write("\t")
		output.write("\n")
		for i in range((len(MVvlaues_B)-1)):
			output.write(str(MVvlaues_B[i]))
			output.write("\t")
		output.write("\n")
		output.write(str(counter))
		
def Main(df, of):
	global datafile
	global	outputfile
	datafile = open(df)
	outputfile = of

Main(sys.argv[1], sys.argv[2]) #program starts from here
ReadData()
