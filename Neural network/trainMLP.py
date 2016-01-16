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
# Train neural network	   #
############################
def BackPropLearning(samples):
	squared_errors=[0.0]*10001
	layer12=[]
	layer23=[]

	#give random weights
	for i in range(3):
		temp=[]
		for j in range(5):
			temp.append(random.uniform(-1,1))
		layer12.append(temp)
	
	#give random weights
	for i in range(6):
		temp=[]
		for j in range(4):
			temp.append(random.uniform(-1,1))
		layer23.append(temp)
	
	for i in range(10001):
		#write weights to file
		if(i==0 or i==10 or i==100 or i==1000 or i==10000):
			with open("weights"+str(i)+".csv", "wb") as f:
				writer = csv.writer(f)
				for j in range(3):
					writer.writerow(layer12[j])
				for j in range(6):	
					writer.writerow(layer23[j])
		
		#backpropgation
		for j in range(len(samples)):
			layer1=[]
			layer2=[1.0]*6
			input2=[0.0]*5
			layer3=[0.0]*4
			input3=[0.0]*4
			delta3=[0.0]*4
			delta2=[0.0]*5			
			y=[0.0]*4

			layer1.append(samples[j][0])
			layer1.append(samples[j][1])
			layer1.append(1)
			y[int(samples[j][2])-1]=1
			
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
			
			#squered error
			for k in range(4):
				squared_errors[i]+=(y[k]-layer3[k])*(y[k]-layer3[k])

			#calculate delta for all nodes in layer 3(output layer)
			for k in range(4):
				delta3[k]=layer3[k]*(1-layer3[k])*(y[k]-layer3[k])
					
			#calculate delta for all nodes in layer 2(hidden layer)
			for k in range(5):
				for l in range(4):				
					delta2[k]+=delta3[l]*layer23[k][l]	
				delta2[k]=delta2[k]*layer2[k]*(1-layer2[k])
			
			#update weights between layer 1-2
			for k in range(3):
				for l in range(5):
					layer12[k][l]+=0.1*layer1[k]*delta2[l]

			#update weights between layer 2-3
			for k in range(6):
				for l in range(4):
					layer23[k][l]+=0.1*layer2[k]*delta3[l]	
	#draw line graph
	#pass over the entire training set vs. the sum of squared error 
	import matplotlib.pyplot as plt
	plt.axis([0,10000,0,max(squared_errors)])
	plt.xlabel('Iterations')
	plt.ylabel('Sum of squared errors')
	plt.plot(squared_errors)
	plt.show()	

###############################################
# main										  #
###############################################
def main():
	if(len(sys.argv) == 2):
		samples=readSamples(sys.argv[1])
		BackPropLearning(samples)
	else:
		print "Usage: python trainMLP.py <inputfile>"
		
main()
