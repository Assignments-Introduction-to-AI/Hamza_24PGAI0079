
from expand import expand
import heapq


def a_star_search(distance_map, time_map, start, goal):
	def calculate_heuristic(node):
		return distance_map[node][goal]  # Using distance as heuristic

	open_nodes = [(0, start)]  # Initialize the open nodes list with the starting node and its cost.
	came_from = {}  # A dictionary to keep track of the parent nodes for each node in the path.
	g_cost = {node: float('inf') for node in distance_map}  # Initialize the g_cost (cost from start) for each node as infinity.
	g_cost[start] = 0  # Set the g_cost of the starting node to 0.
	f_cost = {node: float('inf') for node in distance_map}  # Initialize the f_cost (estimated total cost) for each node as infinity.
	f_cost[start] = calculate_heuristic(start)  # Set the f_cost of the starting node using the heuristic function.

	while open_nodes:
		_, current_node = heapq.heappop(open_nodes)  # Pop the node with the lowest f_cost from the open nodes list.

		if current_node == goal:  # If the goal node is reached,
			path = [current_node]  # Initialize a path with the goal node.
			while current_node in came_from:
				current_node = came_from[current_node]  # Backtrack through the parent nodes to reconstruct the path.
				path.append(current_node)
			path.reverse()  # Reverse the path to get it from start to goal.
			return path  # Return the reconstructed path.

		neighbors = expand(current_node, distance_map)  # Expand the current node to get its neighboring nodes.

		for neighbor in neighbors:  # Iterate through the neighboring nodes.
			if time_map[current_node][neighbor] is not None:  # Check if there is a valid connection between the current node and its neighbor.
				tentative_g_cost = g_cost[current_node] + time_map[current_node][neighbor]  # Calculate the tentative g_cost for the neighbor.
				if tentative_g_cost < g_cost[neighbor]:  # If the tentative g_cost is better than the current g_cost for the neighbor,
					came_from[neighbor] = current_node  # Update the parent node for the neighbor.
					g_cost[neighbor] = tentative_g_cost  # Update the g_cost for the neighbor.
					f_cost[neighbor] = g_cost[neighbor] + calculate_heuristic(neighbor)  # Update the f_cost for the neighbor.
					heapq.heappush(open_nodes, (f_cost[neighbor], neighbor))  # Add the neighbor to the open nodes list with its f_cost.

	return None  # If no path is found and the open nodes list becomes empty, return None.
	# If no path is found and the open list becomes empty, return None.

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






