# Part 1

class Node:
    def __init__(self, left_name=None, right_name=None):
        """
        Initialize a node with the names of left and right connections.
        Actual connections will be established later.

        :param left_name: The name of the left connection node.
        :param right_name: The name of the right connection node.
        """
        self.left_name = left_name
        self.right_name = right_name
        self.left = None
        self.right = None

class Navigator:
    def __init__(self, network, start_node='AAA', end_node='ZZZ'):
        """
        Initialize the navigator with a network of nodes.

        :param network: A dictionary representing the network where keys are node names 
                        and values are Node objects.
        :param start_node: The name of the node where navigation starts.
        :param end_node: The name of the node we want to reach.
        """
        self.network = network
        self.start_node = start_node
        self.end_node = end_node

    def navigate(self, instructions):
        """
        Navigate through the network based on the given instructions.

        :param instructions: A string of 'L' and 'R' representing left and right turns.
        :return: The number of steps required to reach the end_node.
        """
        current_node = self.network[self.start_node]
        step_count = 0

        while current_node != self.network[self.end_node]:
            instruction = instructions[step_count % len(instructions)]
            current_node = current_node.left if instruction == 'L' else current_node.right
            step_count += 1

        return step_count

def create_network_from_file(file_content):
    """
    Create a network of nodes from the given file content.

    :param file_content: A string containing the node definitions.
    :return: A dictionary representing the network where keys are node names 
             and values are Node objects.
    """
    network = {}
    lines = file_content.split('\n')

    for line in lines:
        if '=' in line:
            node_name, connections = line.split('=')
            node_name = node_name.strip()
            left_name, right_name = connections.strip().strip('()').split(', ')
            network[node_name] = Node(left_name, right_name)
            network.setdefault(left_name, Node())
            network.setdefault(right_name, Node())

    for node_name, node in network.items():
        node.left = network[node.left_name]
        node.right = network[node.right_name]

    return network

# Test on network1 and network2
network1_content = """
AAA = (BBB, CCC)
BBB = (DDD, EEE)
CCC = (ZZZ, GGG)
DDD = (DDD, DDD)
EEE = (EEE, EEE)
GGG = (GGG, GGG)
ZZZ = (ZZZ, ZZZ)
"""
network2_content = """
AAA = (BBB, BBB)
BBB = (AAA, ZZZ)
ZZZ = (ZZZ, ZZZ)
"""

network1 = create_network_from_file(network1_content)
network2 = create_network_from_file(network2_content)

navigator1 = Navigator(network1)
steps_network1 = navigator1.navigate('RL')

navigator2 = Navigator(network2)
steps_network2 = navigator2.navigate('LLR')

assert steps_network1 == 2
assert steps_network2 == 6

# Test on the final test file
with open("input.txt", "r") as file:
    final_test_content = file.read()
final_network = create_network_from_file(final_test_content)
final_navigator = Navigator(final_network)
final_steps = final_navigator.navigate(final_test_content.split("\n")[0])  # Replace with your actual instructions

print("Steps in final test network: ", final_steps)

# Part 2
from collections import deque

class NavigatorGhostOptimized:
    def __init__(self, network):
        self.network = network

    def navigate(self, instructions):
        starting_nodes = {node for node in self.network if node.endswith('A')}
        current_nodes = deque(starting_nodes)  # Using a deque for efficient popleft operation
        visited_combinations = set()
        step_count = 0

        while current_nodes:
            current_combination = tuple(sorted(current_nodes))
            if all(node.endswith('Z') for node in current_combination):
                return step_count
            if current_combination in visited_combinations:
                current_nodes.popleft()
                continue
            
            visited_combinations.add(current_combination)
            instruction = instructions[step_count % len(instructions)]
            next_nodes = set()

            for node_name in current_nodes:
                next_node_name = self.network[node_name].left_name if instruction == 'L' else self.network[node_name].right_name
                next_nodes.add(next_node_name)

            current_nodes = deque(next_nodes)
            step_count += 1

        return step_count

# Test the function for part two using the example network
network_part_two_content = """
11A = (11B, XXX)
11B = (XXX, 11Z)
11Z = (11B, XXX)
22A = (22B, XXX)
22B = (22C, 22C)
22C = (22Z, 22Z)
22Z = (22B, 22B)
XXX = (XXX, XXX)
"""

# Testing the NavigatorGhost class with the example network
network_part_two_example = create_network_from_file(network_part_two_content)
navigator_ghost = NavigatorGhostOptimized(network_part_two_example)
steps_for_ghost_paths = navigator_ghost.navigate('LR')
steps_for_ghost_paths

assert steps_for_ghost_paths == 6

final_navigator = NavigatorGhostOptimized(final_network)
final_steps = final_navigator.navigate(final_test_content.split("\n")[0])  # Replace with your actual instructions


print("Steps in final test network: ", final_steps)
# TODO optimize