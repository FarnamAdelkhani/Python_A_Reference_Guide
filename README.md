<h2 align="center">Reference Guide for Useful Python Tips</h2>

<p align="center">
    <img src="https://i.imgur.com/jx5zc80.png" alt="centered image" />
</p>

Farnam Adelkhani -- Last update: March 2019<br>
These tips are mostly compiled from talks by Python Core Developer, Raymond Hettinger.

<br>

View the jupyter notebook through the following nbviewer link:  
https://nbviewer.jupyter.org/github/FarnamAdelkhani/Python_referenceGuide/blob/master/pythonSkills.ipynb

---


<h2 align="center"><b>Reference Guide for Useful Python Tips</b></h2> 
<img src="pythonLogo.png" alt="Drawing" style="width: 60px;"/>

***

<center>Last update: March 2019<br>
These tips are mostly compiled from talks by Python Core Developer, Raymond Hettinger.</center>

<div class="alert alert-block alert-info">
Created by: Farnam Adelkhani
</div>


```python
# Variables
x = 54
```

### Declaring a string:


```python
phrase = "Hello, world"
# or just use '_'
phrase = 'Hello, world'
```

### Conditional Statements:


```python
# Can use the word "or", instead of || in C
if y < 55 or z == 44:
    # code goes here
```


```python
# if-else
if y < 55 and z == 44:
    # code block 1
else:
    # code block 2
```


```python
# if-elif
if course == 100:
    # code block 1
elif not course == 101:
    # code block 2
```


```python
# Conditions -- If input is alpha then true
# Use input() to take input from the user
letters_only = true if input().isalpha() else False
```

### Loops -- Printout 1 line at a time 0-100:


```python
counter = 0
while counter < 100:
    print(counter)
    counter += 1
```

#### Counting:
##### Remember: With python 3, xrange is no longer utilized:


```python
# Loop to range 100
for x in range(100):
    print(x)
```


```python
# For Loop -- count by 10s
for x in range(0, 100, 10):
    print(x)
```

[]: Used to define mutable data types - lists, list comprehensions and for indexing/lookup/slicing.<br>
(): Define tuples, order of operations, generator expressions, function calls and other syntax.<br>
{}: The two hash table types - dictionaries and sets.

### Lists:


```python
# Arrays -- not fixed in size, can add, splice
# Lists -- Let's call Arrays, lists now
nums = []
nums = [1, 2, 3 ,4]
```


```python
# List comprehension -- 0-499
nums = [x for x in range(500)]
nums = list()
```


```python
# List appending
nums = [1, 2, 3 ,4]

# These three lines all do the same thing ... put a 5 at the end of the array
nums.append(5)
nums.insert(4, 5)
# attach a list to the end of a list
nums[len(nums):] = [5]
```

### Tuple Data type -- ordered and immutable set of data:


```python
# Analogous to structs in C

# Here is a list with 4 tuples:
presidents = [
    ("George", 1789),
    ("John", 1789),
    ("Jason", 1789),
    ("Thomas", 1789),
]

# How to iterate this list:
for prez, year in presidents:
    print("In {1}, {0} took office".format(prez, year))
```

### Dictionaries:


```python
pizzas = {
    "Pepperoni": 9,
    "Cheese": 10,
    "Veggy": 11,
    "Buffalo Chicken": 12,
}

# Add or change
pizzas["Cheese"] = 15

# Conditions
if pizzas["vegetables"] < 20:
    # ...do something
```


```python
for pie in pizzas:
    print(pie)

# .items is transforming into a list 
# ... which creates order problems
for pie, price in pizzas.items():
    print(price)
    
for pie, price in pizzas.items():
    print("A whole {} pizza costs ${}".format(pie, price))
```

### Functions:  
No need to specify the return or data types.<br>
Use "def" to introduce the function.


```python
# To direct your program to start at the main function
if __name__ == "__main__":
    main()
```


```python
# Define a function:
def square(x):
    return x * x

# This is x squared:
def square(x):
    return x ** x
```

### Objects:


```python
# Method is another word for function
object.method()
```


```python
class Teams():
    def __init__(name, city, region):
        name.city = city
        name.region = region
        
    def changeID(city, region):
        city.region = region
        
    def print(name):
        print("{} - {}".format(name.city, name.region))
```


```python
'''
The code below allows us to write variables into your operating system as environment variables
where your os will then safely store them away for later use/reference in your code.

The open function opens a file and gives you a file object used to access the file's contents 
according to the specified modes.
The "w" mode supplied in your example opens a file for reading, discarding any data previously 
in that file.
'''

fptr = open(os.environ['OUTPUT_PATH'], 'w')
```

## Looping:

#### Looping over a collection:


```python
colors =['red', 'green', 'blue', 'yellow']

# Don't do this!
for i in range(len(colors)):
    print colors[i]
    
# Do this instead
# Simpler, easier to read, and in Python this is faster.
for color in colors:
    print color
```

#### Looping backwards:


```python
colors =['red', 'green', 'blue', 'yellow']

# In C, we might do this:
for i in range(len(colors)-1, -1, -1):
    print colors[i]
 
# Do this instead, this is faster:
for color in reversed(colors):
    print color
    
# Think about 'for' in Python as 'for each'
```

#### Looping over a collection and indicies:


```python
colors =['red', 'green', 'blue', 'yellow']

# In C, we might do this:
for i in range(len(colors)):
    print i, '-->', colors[i]
 
# Do this instead, without indices:
# No need to track indicidual indices
for i, color in enumerate(colors):
    print i, "-->", colors[i]
    
# Think about 'for' in Python as 'for each'
```

#### Looping over two collections at once:


```python
# Take shorter list and look up ith name in ith color
names = ['raymond', 'rachel', 'matthew']
colors = ['red', 'green', 'blue', 'yellow']

# In C, we might do this:
n = min(len(names), len(colors))
for i in range(n):
    print names[i], '-->', colors[i]

# Do this instead, without indices:
# This is better but it takes more memory because creates a seperate list of tuples
#
# PROBLEM HERE: cacheing to a seperate list requires a ton of memory, this isn't good...
for name, color in zip(names, colors):
    print name, '-->', color
    
# This is even better!!
for name, color in izip(names, colors):
    print name, '-->', color
```

#### Looping in sorted order:


```python
colors =['red', 'green', 'blue', 'yellow']

# Loop forward
for color in sorted(colors):
    print color

# Loop backward
for color in sorted(colors, reverse=True):
    print color
```

***

#### Custom sort order:


```python
colors =['red', 'green', 'blue', 'yellow']

# Custom comparison function
# Calling this function each time is not good, it's slow
def compare_length(c1, c2):
    if len(c1) < len(c2): return -1
    if len(c1) > len(c2): return 1
    return 0
print sorted(colors, cmp=compare_length)


# Here is a better way:
# Comparison functions are no longer in Python 3
print sorted(colors, key=len)
```

#### Call a function until a sentinel value:


```python
# First method
blocks = []
while true:
    # Read memory block of 32 bytes at a time:
    block = f.read(32)
    # Eventually you will run out of data and when you do, you return a sentinel value, an empty string.
    if block == '':
        # @ empty string, break out.
        break
    blocks.append(block)

# Make it iterable instead, then you can feed it to other functions in Python tool kit.
# For 'iter' the first function must be a func of 1 arguments
blocks = []
for block in iter(partial(f.read, 32), ''):
    blocks.append(block)

# We no longer use break functions and NULL because sometimes we include these values into our strings.
# Recall the story of the program that broke from scanning punchcards at the capitol of equador which beggins with 'quit..'
```

#### Distringuishing multiple exit points in loops:


```python
# Flag variables, like found = false
# This slows your program down!
def find(seq, target):
    found = false
    for i, value in enumerate(seq):
        if value == tgt:
            found = True
            break
        if not found:
            return -1
        return i
    
# This is a better way of doing it...
# 'for' loops have 'else'
def find(seq, target):
    for i, value in enumerate(seq):
        if value == tgt:
            break
    # Call else: 'no break', you'd know what it did.
    else:
        return -1
    return i
```

***

### Dictionary Skills:
Fundamental tool for expressing relationships, linking, counting, and grouping.


```python
# Looping of dictionary keys

d = {'matthew:': 'blue', 'rachel': 'green', 'raymond': 'red'}

for k in d:
    print k
    
# Another way... 
# Do this when mutating out the dictionary... because you cant mutate while iterating through it.
for k in d.keys():
    if k.startswith('r'):
        del d[k]
```


```python
# Looping over a dictionary keys and values

# Loop over key and look up value
# slow: rehash every key and do a look up on it.
for k in d:
    print k, '-->', d[k]

# Better way if you need items
for k, v in d.items():
    print k, '-->', v
    
# Best way
for k, v in d.iteritems():
    print k, '-->', v
```


```python
# Constructing a dictionary from pairs

names = ['raymond', 'rachel', 'matthew']
colors = ['red', 'green', 'blue']

# Assemble these two lists into a dictionary: use izip
# Does not need to make a tuple at each iteration... uses one tuple over and over again. This is fast.
d = dict(izip(names, colors))
{'matthew': 'blue', 'rachel': 'green', 'raymond': 'red'}
```


```python
# Counting with dictionaries

colors = ['red', 'green', 'blue', 'red', 'green', 'blue']

# loop over the colors, check if the color is there, if it is not then add it.
d = {}
for colors in colors:
    if color not in d:
        d[color] = 0
    d[color] += 1
    
{'blue':1, 'green': 2, 'red': 3}

# Simplify the code above to this:
# Get the color, if color is missing, return 0 and add 1 to it
d = {}
for color in colors:
    d[color] = d.get(color, 0) + 1

# A more modern way ... not good for beginners with limited understanding.
d = defaultdict(int)
for color in colors:
    d[color] += 1
```


```python
# Grouping with dictionaries

names = ['raymond', 'rachel', 'matthew' 'Roger', 'Charlie', 'katie' 'raj', 'zhang', 'ping']

# Traditional way, start with empty dictionary, the key is what we are grouping by.
d = {}
for name in names:
    key = len(name)
    if key not in d:
        d[key] = []
    d[key].append(name)
    
# Better way...
d = {}
for name in names:
    key = len(name)
    d.setdefault(key, []).append(name)
    
# Modern way... Do this!
d = defaultdict(list)
for name in names:
    key = len(name)
    d[key].append(name)
```


```python
# Is a dictionary popitem() atomic?

d = ['raymond': 'blue', 'rachel': 'red', 'matthew': 'pink']

while d:
    key, value = d.popitem()
    print key, '-->', value
```

***

### Clarify function calls with keyword arguments:


```python
# What does False and true mean?
twitter_search('@obama', False, 20, True)

# Use keyword arguements... slows by microseconds but saves hours of programmer time.
# Easy way to improve code quality
twitter_search('@obama', retweets=False, numtweets=20, popular=True)
```

### Clarify multiple return values with named tuples:


```python
# What does this mean?
doctest.testmod()
(0, 4)

# This provides clarity... named tuples are the same so this code runs the same as above.
# Improve your code base like this!
doctest.testmod()
TestResults(failed=0, attempted=4)

TestResults = namedtuple('TestResults', ['failed', 'attempted'])
```

### Unpacking sequences:


```python
p = 'Raymond', 'Hettinger', 0x30, 'python@example.com'

# Instead of this...
fname = p[0]
lname = p[1]
age = p[2]
email = p[3]

# Do this instead!
fname, lname, age, email = p
```

### Updating multiple/simultaneous state variables:


```python
# take a temp var for y
def fibonacci(n):
    x = 0
    y = 1
    for i in range(n):
        # Risk of order is an issue here, common source of error
        print x
        t = y
        y = x + y
        x = t
        
# better way... using tuple packing/unpacking
# Use old values of x and y
def fibonacci(n):
    x, y = 0, 1
    for i in range(n):
        print x
        x, y = y, x + y
```

### Concatenating strings:


```python
names = ['raymond', 'rachel', 'matthew' 'Roger', 'Charlie', 'katie' 'raj', 'zhang', 'ping']

# Don't do this...
s = names[0]
for name in names[1:]:
    s += ', ' + name
print s

# Do this instead...
print ', '.join(names)
```

### Updating sequences:


```python
names = ['raymond', 'rachel', 'matthew' 'Roger', 'Charlie', 'katie' 'raj', 'zhang', 'ping']

# Wrong data structure used in all these instances is common:
del names[0]
names.pop(0)
names.insert(0, 'mark')

# Use this instad:
names = deque(['raymond', 'rachel', 'matthew' 'Roger', 'Charlie', 'katie' 'raj', 'zhang', 'ping'])
# With deque you can efficiently do the following:
del names[0]
names.popleft()
names.appendleft('mark')
```

## Decorators and Context Managers:
- #### Using decorators to factor-out administrative logic




```python
# business logic is opening a url and return a webpage
# admin logic is caching in dictionary, so if you lookup a webpage over and over again
# mixes bus and admin logic... not reusable
def web_lookup(url, saved={}):
    if url in saved:
        return saved[url]
    page = urllib.urlopen(url).read()
    saved[url] = page
    return page


# The fix:
# This is reusable
@cache
def web_lookup(url):
    return urllib.urlopen(url).read()

# Rewrite like this: Caching decorator
# Fill your code with solutions like this, then you can add @cache elsewhere in your code and the problem is solved:
def cache(func):
    saved = {}
    @wraps(func)
    def newfunc(*args):
        if args in saved:
            return newfunc(*args)
        result = func(*args)
        saved[args] = result
        return result
    return newfunc
```

### Factor-out temporary contexts for decimals:


```python
# Saving the old, restoring the new
old_context = getcontext().copy()
getcontext().prec = 50
print Decimal(355) / Decimal(133)
setcontext(old_context)

# Better way...
# Repeatable logic:
with localcontext(Context(prec=50)):
    print Decimal(355) / Decimal(113)
```

### How to open and close files:


```python
# Old way
f = open('data.txt')
try:
    data = f.read()
finally:
    f.close()
    
# New way
with open('data.txt') as if:
    data = f.read()
```

### How to use locks:


```python
# Make a lock
lock = threading.Lock()

# Old-way to use a lock
lock.acquire()
try:
    print 'critical section 1'
    print 'critical section 2'
finally:
    lock.release()
    
# new-way to use a lock
with lock:
    print 'Critical section 1'
    print 'Critical section 2'
```

### Factor out temporary contexts:


```python
try:
    os.remove('somefile.tmp')
except OSError:
    pass

# Another way to check if file exists in the first place

# Here is a better way to ignore exceptions:
with ignored(OSError):
    os.remove('somefile.tmp')
    
    
# *** TO USE ABOVE FUNCTION ***
# Stick this in util directory
@contextmanager
def ignored(*exceptions):
    try:
        yield
    except exceptions:
        pass
```

***
