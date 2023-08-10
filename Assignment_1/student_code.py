from expand import expand

def a_star_search (dis_map, time_map, start, end):
    ################################################################
    ###### work in progress ########################################
    ################################################################
	pass

def depth_first_search(time_map, start, end):
	# Initialize the stack with the starting landmark
	stack = [start]

	# Create a dictionary to store parent-child relationships
	parents = {}

	# Flag to track if the goal landmark is found
	found = False

	# Continue searching while there are nodes in the stack
	while stack:
		# Pop the top node from the stack
		current = stack.pop(0)
		
		# Check if the current node is the goal landmark
		if current == end:
			found = True
			break
		
		# Expand the current node to get its child nodes
		nodes = expand(current, time_map)
		
		# Iterate through the child nodes
		for child_node in nodes:
			# Insert the child node at the front of the stack
			stack.insert(0, child_node)
			
			# Store the parent-child relationship
			parents[child_node] = current

	# Initialize the path list with the end landmark
	path = [end]

	# If the goal landmark is found, reconstruct the path
	if found == True:
		current = end
		# Traverse back from the end landmark to the start landmark
		while current != start:
			# Insert the parent node at the beginning of the path
			path.insert(0, parents[current])
			current = parents[current]

	# Return the path from start to end
	return path 

def breadth_first_search(time_map, start, end):
	# Initialize the queue with the starting landmark and its path
	queue = [(start, [start])]

	# List to keep track of visited landmarks
	visited = []

	# Create a dictionary to store parent-child relationships
	parents = {}

	# Flag to track if the goal landmark is found
	found = False

	# Continue searching while there are nodes in the queue
	while queue:
		# Dequeue the first element from the queue
		current, path = queue.pop(0)
		
		# Check if the current node is the goal landmark
		if current == end:
			found = True
			break
		
		# Check if the current node has not been visited yet
		if current not in visited:
			# Mark the current node as visited
			visited.append(current)
			
			# Expand the current node to get its child nodes
			nodes = expand(current, time_map)
			
			# Iterate through the child nodes
			for child_node in nodes:
				# Check if the child node has not been visited
				if child_node not in visited:
					# Enqueue the child node along with the extended path
					queue.append((child_node, path + [child_node]))
					
					# Store the parent-child relationship
					parents[child_node] = current

	# Initialize the path list with the end landmark
	path = [end]

	# If the goal landmark is found, reconstruct the path
	if found == True:
		current = end
		# Traverse back from the end landmark to the start landmark
		while current != start:
			# Insert the parent node at the beginning of the path
			path.insert(0, parents[current])
			current = parents[current]

	# Return the path from start to end
	return path






