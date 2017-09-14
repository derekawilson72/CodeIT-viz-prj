
# coding: utf-8



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




def quad(x=1, a=1,b=1,c=0):
    """
    Determine the quadratic of a number
    """
    y = a*x**2 + b*x + c 
    return y


if __name__=='__main__':

    record = {'First': 'Jessica', 'Last': 'Mendez',
              'Age': 29, 'Likes':["Jets", "Mets", "Nets"]}

    First = record['First']
    Last  = record['Last']
    Age   = record['Age']
    Likes = record['Likes']
    print "Name is: ", First, " ", Last
    print "Age is: " , Age
    print "Likes are: ",  Likes


    printPerson(record)

    record01 = {'First': 'Jessica', 'Last': 'Mendez', 'Age': 29,
                'Likes':["Jets", "Mets", "Nets"]}
    record02 = {'First': 'John',    'Last': 'Franco', 'Age': 21,
                'Likes':["Giants", "Yankees", "Nicks"]}

    records = [  record01, record02]

    for record in records:
        printPerson(record)
        print ''

    record03 = createPerson("Chuck", "Schumer", 62,
                            ["Celtics" , "Red Sox", "Bruins"])

    record03 = had_a_birthday(record03)
