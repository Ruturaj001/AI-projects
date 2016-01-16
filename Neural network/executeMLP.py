# Submitted By
# FNU Shivangi
# Ruturaj Hagawane
import sys
import csv
import math
import random

############################
# Read samples from file   #
############################
def readSamples(filename):
	sample=[]
	with open(filename, 'r') as f:
		for line in f:
			if line.strip():
				row = [float(i) for i in line.split(",")]
				sample.append(row)
	return sample

############################
#read weights from file    #
############################
def readWeights(filename):
	weights=[]
	with open(filename, 'r') as f:
		for line in f:
			if line.strip():
				row= [float(i) for i in line.split(",")]
				weights.append(row)
	return weights
	
###############################################
# Seperates class 1, class 2, class 3 and     #
# class 4                                     #
###############################################
def classify(samples,weights):
	layer12=[]
	layer23=[]
	correct=0
	incorrect=0
	profit=0.0
	confusionmatrix=[]
	matrix=[]
	
	
	#initalize confusion matrix
	for i in range(4):
		confusionmatrix.append([0]*4)
	
	#initialize value matrix
	matrix.append([0.20,-0.07,-0.07,-0.07])
	matrix.append([-0.07,0.15,-0.07,-0.07])
	matrix.append([-0.07,-0.07,0.05,-0.07])
	matrix.append([-0.03,-0.03,-0.03,-0.03])
	
	#initalize weights from file
	for i in range(3):
		temp=[]
		for j in range(5):
			temp.append(weights[i][j])
		layer12.append(temp)

	#initalize weights from file
	for i in range(6):
		temp=[]
		for j in range(4):
			temp.append(weights[i+3][j])
		layer23.append(temp)

	for j in range(len(samples)):
		layer1=[]
		layer2=[1.0]*6
		input2=[0.0]*5
		layer3=[0.0]*4
		input3=[0.0]*4
		
		layer1.append(samples[j][0])
		layer1.append(samples[j][1])
		layer1.append(1)
		
		#calculate input and v of all nodes in layer 2
		for k in range(5):
			for l in range(3):
				input2[k]+=layer12[l][k]*layer1[l]
			layer2[k]=1/(1+math.pow(math.e,-input2[k]))
		
		#calculate input and v of all nodes in layer 3
		for k in range(4):
			for l in range(6):
				input3[k]+=layer23[l][k]*layer2[l]
			layer3[k]=1/(1+math.pow(math.e,-input3[k]))	
	
		#find class
		output=layer3.index(max(layer3))
		
		confusionmatrix[output][int(samples[j][2])-1]+=1

		if(output==samples[j][2]-1):
			correct+=1
		else:
			incorrect+=1
	
	#calculate profit
	for i in range(4):
		for j in range(4):
			profit+=confusionmatrix[i][j]*matrix[i][j]
			
	print "Correctly classified",correct
	print "Incorrectly classified",incorrect
	print "Recognition rate",float(correct)/float(correct+incorrect)*100.00
	print "Profit",profit
	print "\tBolt\tNut\tRing\tScrap"
	print "Bolt\t",
	for i in range(4):
		print confusionmatrix[0][i],"\t",
	print
	print "Nut\t",
	for i in range(4):
		print confusionmatrix[1][i],"\t",
	print
	print "Ring\t",
	for i in range(4):
		print confusionmatrix[2][i],"\t",
	print
	print "Scrap\t",
	for i in range(4):
		print confusionmatrix[3][i],"\t",
	print

####################################
# Plots the classification regions #
####################################
def draw(weights):
	samples=[]
	layer12=[]
	layer23=[]
	
	#create samples
	for i in range(100):
		for j in range(100):
			temp=[]
			temp.append(float(i)/100)
			temp.append(float(j)/100)
			samples.append(temp)
	
	#initalize weights from file
	for i in range(3):
		temp=[]
		for j in range(5):
			temp.append(weights[i][j])
		layer12.append(temp)

	#initalize weights from file
	for i in range(6):
		temp=[]
		for j in range(4):
			temp.append(weights[i+3][j])
		layer23.append(temp)
	
	for j in range(len(samples)):
		layer1=[]
		layer2=[1.0]*6
		input2=[0.0]*5
		layer3=[0.0]*4
		input3=[0.0]*4
		
		layer1.append(samples[j][0])
		layer1.append(samples[j][1])
		layer1.append(1)

		#calculate input and v of all nodes in layer 2
		for k in range(5):
			for l in range(3):
				input2[k]+=layer12[l][k]*layer1[l]
			layer2[k]=1/(1+math.pow(math.e,-input2[k]))

		#calculate input and v of all nodes in layer 3
		for k in range(4):
			for l in range(6):
				input3[k]+=layer23[l][k]*layer2[l]
			layer3[k]=1/(1+math.pow(math.e,-input3[k]))	
	
		output=layer3.index(max(layer3))
		samples[j].append(output+1)
	
	import matplotlib.pyplot as plt
	for i in range(len(samples)):
		if(samples[i][2]==1):
	 		plt.plot(samples[i][0],samples[i][1], 'ro')
		elif(samples[i][2]==2):
			plt.plot(samples[i][0],samples[i][1], 'bo')
		elif(samples[i][2]==3):
			plt.plot(samples[i][0],samples[i][1], 'go')
		elif(samples[i][2]==4):
			plt.plot(samples[i][0],samples[i][1], 'yo')
	plt.axis([0,1,0,1])
	plt.show()


###############################################
# main										  #
###############################################
def main():
	if(len(sys.argv) == 3):
		samples=readSamples(sys.argv[1])
		weights=readWeights(sys.argv[2])
		classify(samples,weights)
		draw(weights)
	else:
		print "Usage: python executeMLP.py <inputfile> <weightfile>"
		
main()
