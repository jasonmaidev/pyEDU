from collections import Counter, namedtuple, defaultdict, deque

# Counter is a dict subclass for counting hashable objects
myString = "aaaabbbbccccccccc"
counter = Counter(myString)

num = 1
print("most common: ",counter.most_common(num)) # returns the most common element(s) as a list num X items
print("tupple: ", counter.most_common(num)[0]) # returns the tuple from the list based on index
print("most common letter: ", counter.most_common(num)[0][0]) # returns the key of the tuple
print("times it appears: ", counter.most_common(num)[0][1]) # returns the occurence value of the tuple

""" Namedtuple is a subclass of tuple with named fields """
Vector = namedtuple('Vector', 'x,y')
vt = Vector(1, -4)
print(vt)
print(vt.x, vt.y)

# Defaultdict is a dict subclass that calls a factory function to supply missing values
dD = defaultdict(list)
dD['a'] = 'apple'
dD['b'] = 'banana'
print(dD['a'])
print(dD['b'])
print(dD['c'])
print({key: value for key, value in dD.items()}) #extracting keys and values
print(dict(dD)) # Convert to regular dict for display purposes

# Deque is a list-like container with fast appends and pops on either end
dq = deque()
dq.append(1)
dq.append(2)

dq.appendleft(0)
print(dq)

dq.extendleft([5,4,3])
print(dq)

dq.rotate(3)
print(dq)