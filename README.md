
<h2 align="center"><b>Python Code Transformations<br>"When you see this, do that instead."</b></h2> 
<img src="/images/pythonLogoPro.png" alt="Drawing" style="width: 250px;"/><br>

<center>
    <b>-- Compiled by: Farnam Adelkhani --<br>Tips from talks by Python Core Developer, Raymond Hettinger for fast, clean, idiomatic code.</b><br>
<b>Raymond's rule:</b> One logical line of code equals one sentence in English.
</center>

***

### I'd recommend viewing with Binder instead of Github: [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/FarnamAdelkhani/Python_referenceGuide/may2019?filepath=pythonTransformations.ipynb)

### Another option is Jupyter NBViewer: <a href="https://nbviewer.jupyter.org/github/FarnamAdelkhani/Python_referenceGuide/blob/may2019/pythonTransformations.ipynb" target="_blank">NBViewer</a>  
<b>Last update: May 2019</b> 

***

<center><h4>When you see this, do that instead...</h4>
<li>Replace traditional index manipulation with Python's core looping idioms.</li>
<li>Learn advanced techniques with for-else clauses <b>and</b> the two argument form of iter().</li>
<li>Improve your craftmanship and aim for clean, fast, idiomatic Python code.</li></center>
***

&nbsp;&nbsp;&nbsp;&nbsp;<img src="/images/loops.png" alt="Drawing" style="height: 40px;"/>

<div class="alert alert-block alert-warning"><b>Important Note on Loops:</b><br>
<li>With python 3, xrange is no longer utilized.</li>
<li>In Python, "for" is not equal to "for" in C ... "for" in Python is better thought of as "for each".</li></div>

## Looping over a range of numbers:


```python
# Loop from 0 to 9:
for i in [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]:
    # '**' can be used to raise some number x to a power y.
    print(i**2)
```

### >> Do this instead (better method):


```python
for i in range(10):
    print(i**2)
```

***

## Looping over a range -- counting by 10s:


```python
for i in range(0, 100, 10):
    print(i)
```

***

[]: Used to define mutable data types - lists, list comprehensions and for indexing/lookup/slicing.<br>
(): Define tuples, order of operations, generator expressions, function calls and other syntax.<br>
{}: The two hash table types - dictionaries and sets.

## Looping over a collection:


```python
colors = ['red', 'green', 'blue', 'yellow']

for i in range(len(colors)):
    print(colors[i])
```

### >> Do this instead (better method):


```python
colors = ['red', 'green', 'blue', 'yellow']

for color in colors:
    print(color)
```

## Looping over a collection, backwards:


```python
colors = ['red', 'green', 'blue', 'yellow']

for i in range(len(colors)-1, -1, -1):
    print(colors[i])
```

### >> Do this instead (better method):


```python
colors = ['red', 'green', 'blue', 'yellow']

for color in reversed(colors):
    print(color)
```

## Looping over a collection and indices:


```python
colors = ['red', 'green', 'blue', 'yellow']

for i in range(len(colors)):
    print(i, '--->', colors[i])
```

### >> Do this instead (better method):


```python
colors = ['red', 'green', 'blue', 'yellow']

for i, color in enumerate(colors):
    print(i, '--->', color)
```

## Looping over two collections:


```python
names = ['raymond', 'rachel', 'matthew']
colors = ['red', 'green', 'blue', 'yellow']

n = min(len(names), len(colors))
for i in range(n):
    print(names[i], '--->', colors[i])

for name, color in zip(names, colors):
    print(name, '--->', color)
```

### >> Do this instead (better method):


```python
names = ['raymond', 'rachel', 'matthew']
colors = ['red', 'green', 'blue', 'yellow']

# Note that izip is no longer available in Python 3.0, use zip instead:
for name, color in zip(names, colors):
    print(name, '--->', color)
```

## Looping in sorted order (Best Method):


```python
colors = ['red', 'green', 'blue', 'yellow']

# Forward sorted order
for color in sorted(colors):
    print(colors)

# Backwards sorted order
for color in sorted(colors, reverse=True):
    print(colors)
```

## Custom Sort Order:


```python
colors = ['red', 'green', 'blue', 'yellow']

# Return -1,0,1 depending on lessThan,equal,greater
def compare_length(c1, c2):
    if len(c1) < len(c2): return -1
    if len(c1) > len(c2): return 1
    return 0

# Old method
#print sorted(colors, cmp=compare_length)

# New method
print(sorted(colors, key=len))

# Old method = 20 million calls to function
# New method = 1 million calls to function
#
# *Comparison functions do not exist in Python 3
```

## Call a function until a sentinel value:


```python
# Looping over a function with a sentinel:
# *Traditional method*
#
# Reading 32 bytes at a time, eventually run out of data...
# ... then sentinel value is returned(ie. an empty string)
# When empty string is returned, you break out the function
blocks = []
while True:
    block = f.read(32)
    if block == '':
        break
    blocks.append(block)
```

### >> Do this instead (better method):


```python
# iter function can take two arguments:
# 1st - function that you repeatedly call
# 2nd - sentinel value

# Using a for loop makes this iterable! Magical...
# now you can feed it to set, sorted, min, max, sum, etc
# * Making something iterable, it works with the entire Python tool kit.
blocks = []
for block in iter(partial(f.read, 32), ''):
    blocks.append(block)
```

***

## Distinguishing multiple exit points in loops:


```python
# Typical solution: Flag variables(like found = false...)
# This slows your program down!

# If target is true, change the flag and act on it at end:
def find(seq, target):
    found = false
    for i, value in enumerate(seq):
        if value == tgt:
            found = True
            break
        if not found:
            return -1
        return i
```

### >> Do this instead (better method):


```python
# If finish look and don't encounter a break: return -1
# If finish the loop normally: return i
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

&nbsp;&nbsp;&nbsp;&nbsp;<img src="images/dictionaries.png" alt="Drawing" style="height: 40px;"/>

<li>Mastering dictionaries is a fundamental Python skill!</li>
<li>Fundamental tool for expressing relationships, linking, counting, and grouping.</li>

## Looping of dictionary keys:


```python
d = {'matthew:': 'blue', 'rachel': 'green', 'raymond': 'red'}

for k in d:
    print k
```

### >> Do this instead (When you're mutating the dictionary):


```python
# Treating a list as a dictionary...
# ... the indices in a list are parrallel to the keys in a dictionary

d = {'matthew:': 'blue', 'rachel': 'green', 'raymond': 'red'}

# d.keys makes a copy of all the keys and stores them in a list:
# ... then you can mutate the dictionary without consequence.
for k in list(d.keys()):
    if k.startswith('r'):
        del d[k]
```

`d.keys()` makes a copy of all the keys and stores them in a list. Then you can modify the dictionary. Note: in python 3 to iterate through a dictionary you have to explicitly write: `list(d.keys())` because `d.keys()` returns a "dictionary view" (an iterable that provide a dynamic view on the dictionary’s keys).

## Looping over a dictionary keys and values:


```python
# Loop over key and look up value

# slow: rehash every key and do a look up on it.
for k in d:
    print(k, '-->', d[k])

# Better way if you need items
for k, v in d.items():
    print(k, '-->', v)
```

### >> Do this instead (... but only in Python 2):  


```python
# ** This was previously a better method, but no good in Python 3!  **
# ** Just use 'items' in Python 3.>: **
for k, v in d.iteritems():
    print(k, '-->', v)
```

**Python 2:** `iteritems()` is better as it returns an iterator.  
**Python 3:** `iteritems()` has been deprecated and `items()` behaviour is close to what `iteritems()` had been in Python 2. 

## Constructing a dictionary in pairs:


```python
# ** izip does not exist in Python 3, use zip instead! **

names = ['raymond', 'rachel', 'matthew']
colors = ['red', 'green', 'blue']

# Assemble these two lists into a dictionary using izip
# Does not need to make a tuple at each iteration... 
# ... uses one tuple over and over again. This is fast!
#
d = dict(izip(names, colors))
{'matthew': 'blue', 'rachel': 'green', 'raymond': 'red'}
```

**For python 3:** Use: `d = dict(zip(names, colors))`

## Counting with dictionaries:


```python
# Most basic method: Looping over a dictionary
#
colors = ['red', 'green', 'blue', 'red', 'green', 'blue']

# loop over the colors 
#    check if the color is there
#       if it is not then add it
d = {}
for colors in colors:
    if color not in d:
        d[color] = 0
    d[color] += 1
    
{'blue':1, 'green': 2, 'red': 3}
```

### >> Do this instead (Simplify the code above to this):


```python
colors = ['red', 'green', 'blue', 'red', 'green', 'blue']

# loop over the colors 
#    Get the color
#       if color is missing, return 0 and add 1 to it

d = {}
for color in colors:
    d[color] = d.get(color, 0) + 1
```

### >> A more modern method (advance):  
`defaultdict()`: Not good for beginners with limited understanding...
<ul>
<b>Prerequisites to understanding defaultdict():</b>
<ul>
<li>Know how to import the collections</li>
<li>Learn the distintions between a regular/default dictionary</li>
<li>Know about factory functions</li>
<li>`int` can be called with no arguements, producing the value '0'</li>
<li>What you get back is no longer a dictionary, but a default dictionary</li>  
<ul><li>... so it must be converted back for some use-cases</li>
</ul>
</ul>
</ul>  

Know and understand the above idioms before utilizing `defaultdict()`!


```python
colors = ['red', 'green', 'blue', 'red', 'green', 'blue']

d = defaultdict(int)
for color in colors:
    d[color] += 1
```

***

## Grouping with dictionaries:


```python
# Group by length of first names:
names = ['raymond', 'rachel', 'matthew' 'Roger', 
         'Charlie', 'katie' 'raj', 'zhang', 'ping']

# Traditional way, start with empty dictionary, the key is what we are grouping by.
d = {}
for name in names:
    key = len(name)
    if key not in d:
        d[key] = []
    d[key].append(name)
```

### >> Do this instead (better method):


```python
d = {}
for name in names:
    key = len(name)
    d.setdefault(key, []).append(name)
```

### >> Better yet... most modern method... do this!


```python
d = defaultdict(list)
for name in names:
    key = len(name)
    d[key].append(name)
```

## Pop Item:


```python
# Is a dictionary popitem() atomic?
#   popitem() removes an arbitrary item

d = ['raymond': 'blue', 'rachel': 'red', 'matthew': 'pink']

while d:
    key, value = d.popitem()
    print key, '-->', value
```

`popitem` is atomic so you don't have to put locks around it to use it in threads.

***

## Linking dictionaries:


```python
defaults = {'color': 'red', 'user': 'guest'}
parser = argparse.ArgumentParser()
parser.add_argument('-u', '--user')
parser.add_argument('-c', '--color')
namespace = parser.parse_args([])
command_line_args = {k:v for k, v in vars(namespace).items() if v}

# The common approach below allows you to use defaults at first, then override them
# with environment variables and then finally override them with command line arguments.
# It copies data like crazy, unfortunately. (Not fast!)
d = defaults.copy()
d.update(os.environ)
d.update(command_line_args)

# Environment variables take precedence over defaults.
```


```python
d = ChainMap(command_line_args, os.environ, defaults)
```

`ChainMap` has been introduced into python 3. Fast and beautiful.

***

## Clarify function calls with keyword arguments:


```python
# What does False and true mean?
twitter_search('@obama', False, 20, True)
```

### >> Do this instead (better method):


```python
# Use keyword arguements... slows by microseconds but saves hours of programmer time.
twitter_search('@obama', retweets=False, numtweets=20, popular=True)

# ... Easy way to improve code quality like this.
# Slows code slightly (microseconds) but saves hours of programming time.
```

***

## Clarify multiple return values with named tuples:


```python
# Old testmod return value:
doctest.testmod()
(0, 4)
# Is this good or bad? You don't know because it's not clear.
```

### >> Do this instead (better method):


```python
# This provides clarity... named tuples are the same so this code runs the same.
#
# Improve your code base like this!
doctest.testmod()
TestResults(failed=0, attempted=4)

TestResults = namedtuple('TestResults', ['failed', 'attempted'])
```

***

## Unpacking sequences:


```python
p = 'Raymond', 'Hettinger', 0x30, 'python@example.com'

# Instead of this...
fname = p[0]
lname = p[1]
age = p[2]
email = p[3]

# Do this instead! ... Easier to read and faster:
fname, lname, age, email = p
```

***

## Updating multiple/simultaneous state variables:


```python
# Take a temp var for y
#    add up new y
#       then use temp variable
def fibonacci(n):
    x = 0
    y = 1
    for i in range(n):
        # Risk of order is an issue here, common source of error
        print x
        t = y
        y = x + y
        x = t
```

### >> Do this instead (better method):


```python
# Using tuple packing/unpacking

def fibonacci(n):
    x, y = 0, 1
    for i in range(n):
        print x
        x, y = y, x + y
```

***

## Simultaneous state updates:


```python
tmp_x = x + dx * t
tmp_y = y + dy * t
# NOTE: The "influence" function here is just an example function, 
#   what it does is not important. 
# The important part is how to manage updating multiple variables at once.
tmp_dx = influence(m, x, y, dx, dy, partial='x')
tmp_dy = influence(m, x, y, dx, dy, partial='y')
x = tmp_x
y = tmp_y
dx = tmp_dx
dy = tmp_dy
```

### >> Do this instead (better method):


```python
# NOTE: The "influence" function here is just an example function, what it does 
# is not important. The important part is how to manage updating multiple 
# variables at once.
x, y, dx, dy = (x + dx * t,
                y + dy * t,
                influence(m, x, y, dx, dy, partial='x'),
                influence(m, x, y, dx, dy, partial='y'))
```

***

&nbsp;&nbsp;&nbsp;&nbsp;<img src="images/efficiency.png" alt="Drawing" style="height: 40px;"/>

- An optimization fundamental rule
- Don’t cause data to move around unnecessarily
- It takes only a little care to avoid `O(n**2)` behavior instead of linear behavior

**Raymond says:** Don't move data around unnecessarily.

## Concatenating strings:


```python
names = ['raymond', 'rachel', 'matthew' 'Roger', 
         'Charlie', 'katie' 'raj', 'zhang', 'ping']

# Don't do this...
s = names[0]
for name in names[1:]:
    s += ', ' + name
print s

# This is quadratic behavior, don't add strings in this way.
```

### >> Do this instead (better method):


```python
names = ['raymond', 'rachel', 'matthew' 'Roger', 
         'Charlie', 'katie' 'raj', 'zhang', 'ping']

# Do this instead, join them:
print ', '.join(names)
```

***

## Updating sequences:


```python
names = ['raymond', 'rachel', 'matthew' 'Roger', 
         'Charlie', 'katie' 'raj', 'zhang', 'ping']

# If you see anyone of these 3:
# ... You're doing it wrong!
del names[0]
names.pop(0)
names.insert(0, 'mark')
```

### >> Do this instead (better method):


```python
# Use this instad:
names = collections.deque(['raymond', 'rachel', 'matthew' 'Roger', 
               'Charlie', 'katie' 'raj', 'zhang', 'ping'])

# More efficient with collections.deque
del names[0]
names.popleft()
names.appendleft('mark')
```

### Grep for the above, replace, and quickly speed up a large code base!

***

&nbsp;&nbsp;&nbsp;&nbsp;<img src="images/decorators.png" alt="Drawing" style="height: 40px;"/>

<li>Helps separate business logic from administrative logic</li>
<li>Clean, beautiful tools for factoring code and improving code reuse</li>
<li>Good naming is essential.</li>
<li>Remember the Spiderman rule: With great power, comes great responsibility!</li>


```python
# business logic is opening a url and return a webpage
#
# admin logic is caching in dictionary, so if you lookup a... 
# ...webpage over and over again mixes bus and admin logic... not reusable
def web_lookup(url, saved={}):
    if url in saved:
        return saved[url]
    page = urllib.urlopen(url).read()
    saved[url] = page
    return page
```

### >> The fix:


```python
# Following is reusable:
@cache
def web_lookup(url):
    return urllib.urlopen(url).read()
```

### >> Rewrite like this: Caching decorator


```python
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

**Note:** since python 3.2 there is a decorator for this in the standard library: `functools.lru_cache`.

***

## Factor-out temporary contexts for decimals:


```python
# Saving the old, restoring the new
#
# Copy the context -> Change decimal precision to 50 -> 
#    -> Do a calculation -> Restore old context

old_context = getcontext().copy()
getcontext().prec = 50
print Decimal(355) / Decimal(133)
setcontext(old_context)
```

### >> Better method (Repeatable logic):


```python
# Anyone your context gets repeated in your code...
#     you want a context manager to improve it

with localcontext(Context(prec=50)):
    print Decimal(355) / Decimal(113)
```

***

## How to open and close files:

### Old method:


```python
f = open('data.txt')
try:
    data = f.read()
finally:
    f.close()
```

### >> New Method:


```python
with open('data.txt') as f:
    data = f.read()
```

***

## How to use locks:

### Old method:


```python
# Make a lock the old way:
lock = threading.Lock()

# Old-way to use a lock
lock.acquire()

# You need to use try -> finally to release in case of an error:
try:
    print 'critical section 1'
    print 'critical section 2'
finally:
    lock.release()
```

### >> New method to use a lock:


```python
with lock:
    print 'Critical section 1'
    print 'Critical section 2'
```

***

## Factor out temporary contexts:


```python
try:
    os.remove('somefile.tmp')
except OSError:
    pass

# Another way to check if file exists in the first place
```

### >> Better:


```python
# Here is a better way to ignore exceptions:
with ignored(OSError):
    os.remove('somefile.tmp')
```

`ignored` is is new in python 3.4. Note: `ignored` is actually called `suppress` in the standard library.

To make your own `ignored` context manager in the meantime:


```python
# Stick this in util directory in order to ignore exceptions:
@contextmanager
def ignored(*exceptions):
    try:
        yield
    except exceptions:
        pass
```

***

&nbsp;&nbsp;&nbsp;&nbsp;<img src="images/objects.png" alt="Drawing" style="height: 40px;"/>


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

---


<center><b>Can also contact me on Linked[in]:</b><br>
<a href="https://www.linkedin.com/in/farnamadelkhani/" target="_blank">https://www.linkedin.com/in/farnamadelkhani/</a></center><br><br>
<img src="images/signature.png" alt="Drawing" style="width: 250px;"/>

***
