import sys
import copy
from Queue import PriorityQueue
import math

#initializes global varibles
xlimit=0
ylimit=0
goalx=0
goaly=0


########################
# Class to initialize, 
#read and print node 
########################
class Node:
    #########################
    # Initialization method
    #########################
    def __init__(self, pos, parent):
        self.pos = pos
        self.parent = parent
    
    #############################
    # Method to print path
    #############################
    def printNode(self):
        o=self
        path=[]
        while(o!= None):
            path.insert(0,o.pos)
            o=o.parent
        for i in path:
        	i.printMaze()
        print
        print "pathcost:",
        print len(path)

#############################
# Reads the maze file from 
# command line argument.
#############################
def readMaze(filename):
	with open(filename, 'r') as f:
		# Read the entire file, split on newlines manually.
		maze = f.read().split()

		# Convert string to list for easy indexing.
		for i in range(len(maze)):
			maze[i] = list(maze[i])

	return maze

############################
# Class state 
############################
class Mazestate:
    
	if(len(sys.argv) != 2):
	    # Usage 
		print "Usage: python maze.py <mazefile>"
		sys.exit()
	# Command line arg	
	mazefile = sys.argv[1]
	# Read in maze file
	maze = readMaze(mazefile)
	#using global variables
	global xlimit
	global ylimit
	global goalx
	global goaly
	# Get size of maze
	xlimit=len(maze[0])
	ylimit=len(maze)
	T='1'
	N='2'
	S='5'
	E='3'
	W='4'
	B='6'
	cost=0
	for i in range(len(maze)):
			for j in range(len(maze[i])):
			    #position of goal
				if maze[i][j]=='G':
					goalx=j
					goaly=i
				#position of start	
				if maze[i][j]=='S':
					x=j
					y=i
     
    ##################
    # Die moves right
    ##################    
	def moveR(self):
		temp=self.T
		self.T=self.W
		self.W=self.B
		self.B=self.E
		self.E=temp
		self.x+= 1
		self.cost+=1
	
	##################
    # Die moves left
    ##################	
	def moveL(self):
		temp= self.T
		self.T=self.E
		self.E=self.B
		self.B=self.W
		self.W=temp
		self.x-= 1
		self.cost+=1
	
	##################
    # Die moves UP
    ##################	
	def moveU(self):
		temp=self.T
		self.T=self.S
		self.S=self.B
		self.B=self.N
		self.N=temp
		self.y-= 1
		self.cost+=1
		
	##################
    # Die moves down
    ##################	
	def moveD(self):
		temp=self.T
		self.T=self.N
		self.N=self.B
		self.B=self.S
		self.S=temp
		self.y+= 1
		self.cost+=1
	
	####################
    # Prints the maze
    ####################
	def printMaze(self):
		print
		for i in range(len(self.maze)):
			for j in range(len(self.maze[i])):
				if j==self.x and i==self.y:
				    #if die on location
					print self.T,
				else:
					print self.maze[i][j],
			print
			#die orientation
		print
		print "  N         ",self.N
		print "W T E     ",self.W,self.T,self.E,"      B      ",self.B 
		print "  S         ",self.S
	
	###########################
    # determines position of 1
    ###########################
	def whereis1(self):
		if self.T=='1':
			return 'T'
		if self.E=='1':
			return 'E'
		if self.W=='1':
			return 'W'
		if self.N=='1':
			return 'N'
		if self.S=='1':
			return 'S'
	
	#########################
    # compares two state 
    # (comparator)
    #########################
	def compare(self,state):
		if self.T==state.T and self.E==state.E and self.x==state.x and self.y==state.y:
			return True
			
		
##########################
# path cost when 1 on top
##########################
def jump(x,y):
	"""when 1 is on top"""
	cost=0
	if math.fabs(goalx-x)!=0:
		cost=math.fabs(goalx-x)+2
	if math.fabs(goaly-y)!=0:
		cost=cost+math.fabs(goaly-y)+2
	return cost

###############################
# heuristic 1: get '1' on top
# if not  calculate path cost 
# using method jump
###############################	
def h1(state):
	ori=state.whereis1()
	if(ori=='T'):
		return jump(state.x,state.y)
	if(ori=='S'):
		return math.fabs(state.x-goalx)+jump(goalx,state.y-1)+1
	if(ori=='N'):
		return math.fabs(state.x-goalx)+jump(goalx,state.y+1)+1
	if(ori=='E'):
		return math.fabs(state.y-goaly)+jump(state.x-1,goaly)+1 
	if(ori=='W'):
		return math.fabs(state.y-goaly)+jump(state.x+1,goaly)+1 	

###########################
# heuristic 2: calculates
# manhattan distance
###########################
def h2(state):
	return math.fabs(goalx-state.x)+math.fabs(goaly-state.y)

###########################
# heuristic 3: calculates
# diagonal distance
###########################	
def h3(state):		
	return math.sqrt(math.pow(goalx-state.x,2)+math.pow(goaly-state.y,2))

#########################
# determines next 
# possible states
#########################	
def getnextstates(state):
	nextstates = []
	
	if(state.x>0 and state.E!='6' and state.maze[state.y][state.x-1]!='*'):
		next=copy.deepcopy(state)
		next.moveL()
		nextstates.append(next)
	
	if(state.y<ylimit-1 and state.N!='6' and state.maze[state.y+1][state.x]!='*'):
		next=copy.deepcopy(state)
		next.moveD()
		nextstates.append(next)
	
	if(state.y>0 and state.S!='6' and state.maze[state.y-1][state.x]!='*'):
		next=copy.deepcopy(state)
		next.moveU()
		nextstates.append(next)
	
	if(state.x<xlimit-1 and state.W!='6' and state.maze[state.y][state.x+1]!='*'):
		next=copy.deepcopy(state)
		next.moveR()
		nextstates.append(next)
	return nextstates

####################
# checks if goal 
# state is reached
####################
def goal(state):
	if state.x==goalx and state.y==goaly and state.T=='1':
		return True
	return False

##################
# main function
##################
def main():
	for i in range(3):
		start=Mazestate()
		solution_found=False
		nodesgenerated=0
		visitedcount=0
		visited = []
		q= PriorityQueue(0)	
		# Format: Node((x, y), parent)	
		startNode = Node(start, None)
		q.put((0,startNode))
		
		while not q.empty():
			current=q.get()[1]
			current_state=current.pos
			# if current state is goal
			if goal(current_state):
				solution_found=True
				break
			visitedcount+=1
			nextstates=getnextstates(current_state)
			for state in nextstates:
				found=False
				for visitedstate in visited:
					if state.compare(visitedstate):
						found=True
						break
				if not found: 
					nodesgenerated+=1
					visited.append(state)
					newnode = Node(state,current)
					# for heuristic 1
					if(i==0):
						q.put((state.cost+h1(state),newnode))
					#for heuristic 2	
					elif(i==1):
						q.put((state.cost+h2(state),newnode))
					#for heuristic 3
					elif(i==2):
						q.put((state.cost+h3(state),newnode))
						
		if(i==0):
		    #prints solution
			if solution_found:
				current.printNode()
			else:
				print "No Solution"
		print
		print "nodes generated for heuristic",i+1,":",
		print nodesgenerated
		print "total nodes visited for heuristic",i+1,":",
		print visitedcount
		print
	
main()
