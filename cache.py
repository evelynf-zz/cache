# What is the purpose of caching? What are some caching strategies? what is the worst case scenarios of those caching strategies?
# cacheing can improve your program's performance because it makes getting the data faster  since you don't need to pull it straight from memory
# you can store smaller amounts of data in a cache, and the program will check the cache before it goes to memory
# caching strategy: different levels of caching. 
# computer will check the lowest level cache (the fastest but stores the least amount of data), if it misses it will check the next level and then finally outer level
# if it misses that it will check memory
# worst case scenario you have to check every cache, and will have a bunch of cache misses

# Implement an LRU cache such that lookups and inserts can be done in O(1) time

class ListNode():
	def __init__(self, name, value):
		self.value = value
		self.name = name
		self.next = None
		self.prev = None

class LRUCache():
	def __init__(self, max_size):
		assert(max_size > 0)
		self.dictionary = {}
		self.head = None
		self.last = None
		self.max_size = max_size
		self.size = 0


	def make_space(self):
		if self.size == self.max_size:
			# get rid of the oldest node
			self.dictionary[self.last.name] = None
			if self.last != self.head:
				self.last = self.last.prev
				self.last.next = None
			else:
				self.head = None
				self.last = None
			self.size -= 1

	def insert(self, name, value):
		if name in self.dictionary:
			node = self.dictionary[name]
			node.value = value
		else:
			self.make_space()
			node = ListNode(name, value)
			self.dictionary[name] = node
			self.size += 1
		if self.head == None:
			self.last = node
		else:
			self.head.prev = node
		node.next = self.head
		self.head = node

	def lookup(self, name):
		# change head to be that value
		if name in self.dictionary and self.dictionary[name]:
			node = self.dictionary[name]
			# remove this node from the linked list
			if node != self.head:
				node.prev.next = node.next
				# make this node the head
				old_head = self.head
				self.head = node
				self.head.next = old_head
			return node.value
		else:
			return None



