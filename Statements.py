
# coding: utf-8

### Conditional Statements

# basic conditional statements

# In[2]:

x=4
if x>1:  #evaluate if x is greater than 1
    print 'x is in fact greater than 1'
else:
    print 'x is not greater than 1'


#  empty objects test as false

# In[3]:

x = []
if x:
    print 1
else:
    print 0


# make even more conditions
# <p> Test the condition:  <i> if condition 1.... else if condition 2.....  else if condition 3..... </i> </p>

# In[10]:

x=4.00001
if x>4:  #evaluate if x is greater than 1
    print 'x is in fact greater than 4'
elif x>3: #else if statement
    print 'x is greater than 3'
else:
    print 'x is not greater than 3'


### For loops 

# for loops iterate over a sequence of objects
# <p>  <i> for loop_var in sequence: 
# <br>
# statements
# </i> </p>

# TYPICAL SCENARIO 
# 

# In[11]:

for item in range(5): 
    print item, 


# LOOPING OVER A LIST
# 

# In[12]:

animals=['dogs','cats','bears']
for animal in animals:
    print animal 


# Looping over a dictionary
# 

# In[13]:

d = {'a':1, 'b':2, 'c':3}


# DEFAULT LOOPING (KEYS) 
# 

# In[14]:

for key in d: 
    print key, d[key] 


# LOOPING OVER ITEMS
# 

# In[15]:

for key, val in d.items():
    print key, val


### While loops 

# while loops iterate until a condition is met
# <p> while condition:
#     statements
#     </p>

# In[16]:

# breaking from an infinite
# loop
i = 0
while i < 3:
    i = i + 1
    print i


# In[ ]:



