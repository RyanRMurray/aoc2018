import os

class node:	
	def __init__(self, childNum, metaNum):
		self.childNum = childNum
		self.metaNum = metaNum
		self.children = []
		self.metadata = []
		self.value = None
	
	def return_meta_sum(self):
		total = 0
		if len(self.children) == 0:
			return sum(self.metadata)
		else:
			for child in self.children:
				total += child.return_meta_sum()
			total += sum(self.metadata)
			return total
	
	def return_value(self):
		if self.value == None:
			if len(self.children) == 0:
				self.value = sum(self.metadata)
			else:
				self.value = 0
				for m in self.metadata:
					if m != 0 and m < len(self.children) + 1:
						self.value += self.children[m-1].return_value()
		return self.value

def get_input():
	input = open('input.txt', 'r')
	data = [int(x) for x in input.read().split()]
	data.reverse()
	return data

def generate_leaf(node_data):
	new_node = node(node_data[0], node_data[1])
	new_node.metadata = node_data[2:]
	return new_node

def main():
	data = get_input()
	root = node(1,0)
	node_stack = [root]
	child_stack = [1]
	meta_stack = [0]
	
	while True:
		if child_stack[-1] == 0:
			metadata = []
			for m in range(meta_stack[-1]):
				metadata.append(data.pop())
			node_stack[-1].metadata = metadata
			meta_stack.pop()
			child_stack.pop()
			if len(node_stack) == 1:
				break
			else:
				child = node_stack.pop()
				node_stack[-1].children.append(child)
		else:
			child_stack[-1] -= 1
			child_stack.append(data.pop())
			meta_stack.append(data.pop())
			new_node = node(child_stack[-1],meta_stack[-1])
			node_stack.append(new_node)
	
	meta_sum = root.return_meta_sum()
	print('Total of metadata is ' + str(meta_sum))
	val = root.children[0].return_value()
	print('Value of root node is ' + str(val))

main()