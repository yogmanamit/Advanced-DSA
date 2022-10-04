# Trie = AKA digital tree or prefix tree
# Demonstration of auto-complete feature using Trie data structure.

class TrieNode():
	def __init__(self):
		# Initialising one node for trie
		self.children = {}
		self.last = False


class Trie():
	def __init__(self):
    #Initiliazation
		self.root = TrieNode()

	def formTrie(self, keys):
		for key in keys:
			self.insert(key) # inserting one key to the trie.

	def insert(self, key):
		node = self.root

		for a in key:
			if not node.children.get(a):
				node.children[a] = TrieNode()

			node = node.children[a]

		node.last = True

	def suggestionsRec(self, node, word):
		# Method to recursively traverse the trie and return a whole word.
		if node.last:
			print(word)

		for a, n in node.children.items():
			self.suggestionsRec(n, word + a)

	def printAutoSuggestions(self, key):
		# Returns all the words in the trie whose common prefix is the given key 
		node = self.root

		for a in key:
			# no string in the Trie has this prefix
			if not node.children.get(a):
				return 0
			node = node.children[a]
      
      
		if not node.children:
			return -1

		self.suggestionsRec(node, key)
		return 1


  
# Driver Code
keys = ["hello", "dog", "hell", "cat", "a", "hel", "help", "helps", "helping"]
key = "h" # for autocomplete suggestions

t = Trie()
t.formTrie(keys)

comp = t.printAutoSuggestions(key)

if comp == -1:
	print("No other strings found with this prefix\n")
elif comp == 0:
	print("No string found with this prefix\n")
