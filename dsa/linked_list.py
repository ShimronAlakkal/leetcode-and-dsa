# Create a linked list class with basic CRUD functionality and some util funcs like print 

class Node:

	def __init__(self, data = None, ref = None):
		self.data = data
		self.ref = ref


class LinkedList : 

	def __init__(self):
		self.head = None


	def add_at_start(self, data):
		self.head = Node(data, self.head)


	def print(self):
		if self.head is None :
			print('Empty linked list found')
		else:
			flag = self.head

			print('head before iteration ',self.head,'\n')

			while flag:
				print ( f'data = {flag.data}  and ref = {flag.ref}')
				flag = flag.ref

		return 


if __name__ == '__main__':
	ll = LinkedList()
	ll.add_at_start(123)
	ll.add_at_start(2342342)
	ll.add_at_start(2323)
	ll.add_at_start(4554)
	ll.add_at_start(0)
	ll.print()


