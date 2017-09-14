
# coding: utf-8

## Functions in Python

# Convert variables and data structures in Python to a specific output consistently and repetitively.

# In[1]:

record = {'First': 'Jessica', 'Last': 'Mendez', 'Age': 29, 'Likes':["Jets", "Mets", "Nets"]}


# In[5]:

First = record['First']
Last  = record['Last']
Age   = record['Age']
Likes = record['Likes']
print "Name is: ", First, " ", Last
print "Age is: " , Age
print "Likes are: ",  Likes


# Perform the same action as a function

# In[7]:

def printPerson(record):
    """
    Defines a function to handle a person record and process it
    """
    First = record['First']
    Last  = record['Last']
    Age   = record['Age']
    Likes = record['Likes']
    print "Name is: ", First, " ", Last
    print "Age is: " , Age
    print "Likes are: ",  Likes


# In[8]:

printPerson(record)


# In[9]:

record01 = {'First': 'Jessica', 'Last': 'Mendez', 'Age': 29, 'Likes':["Jets", "Mets", "Nets"]}
record02 = {'First': 'John',    'Last': 'Franco', 'Age': 21, 'Likes':["Giants", "Yankees", "Nicks"]}


# In[10]:

printPerson(record01)


# In[11]:

printPerson(record02)


# Iterate over arbitrary numbers of records

# In[12]:

records = [
    {'First': 'Jessica', 'Last': 'Mendez', 'Age': 29, 'Likes':["Jets", "Mets", "Nets"]},
    {'First': 'John',    'Last': 'Franco', 'Age': 21, 'Likes':["Giants", "Yankees", "Nicks"]},
    {'First': 'Jill',    'Last': 'Stein',  'Age': 51, 'Likes':["Patriots", "RedSox", "Celtics"]},
]


# In[14]:

for record in records:
    printPerson(record)
    print ''


# In[ ]:

#Receiving output from functions based on input

def createPerson(First=None, Last=None, Age=None, Likes=[]):
    """
    Defines a function to create a persons record and output the results
    """
    record={'First': First,
            'Last':  Last,
            'Age':   Age,
            'Likes': Likes,
    }
    print "Name is: ", First, " ", Last
    print "Age is: " , Age
    print "Likes are: ",  Likes
    return record

record03 = createPerson("Chuck", "Schumer", 62, ["Celtics" , "Red Sox", "Bruins"])


def createPerson(First=None, Last=None, Age=None, Likes=[]):
    """
    Defines a function to create a persons record and output the results
    """
    record={'First': First,
            'Last':  Last,
            'Age':   Age,
            'Likes': Likes,
    }
    printPerson(record)
    return record


def had_a_birthday(record):
    """
    Defines a function to handle a person record and increment the age and return the new record
    """
    First = record['First']
    Last  = record['Last']
    Age   = record['Age']
    Likes = record['Likes']
    Age = Age + 1 ##increment the age
    print "Happy Birthday!: ", First, " ", Last
    print "new Age is: " , Age
    record.update({'Age': Age })
    return record


record03 = had_a_birthday(record03)

