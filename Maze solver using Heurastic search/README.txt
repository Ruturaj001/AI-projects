How to run
1. To run program type in terminal,
   python maze.py <mazefile>
   ex. python maze.py puzzle3.txt 

2. mazefile must represent 
   obstacle by '*'
   start state by 'S'
   goal state by 'G'
   
Note: input mazefile shouldn't have extra spaces and '\n' or next line character

How to interpret output 
1. The path is printed
   Path will have every state (as given in input) with showing current position of die.
   next it will show orientation of die for each position, in this form
     N
   W T E     B
   	 S
   where, 	N represent North/Up side of die
   			W represent West/Left side of die
   			T represent Top(visible) side of die
   			E represent East/Right side of die
   			S represent South/Down side of die
   			B represent bottom(not visible) side of die
   			
2. Then it prints path cost.

3. Then prints number of nodes generated and number of nodes visited for
   each heuristic.
