''' Q19 Predict the output'''

class Match:
    ''"Runs and Wickets"''
    runs=281
    wickets=5

    def __init__(self,runs,wickets):
        self.runs=runs
        self.wickets=wickets

    print "Runs scored are : ",runs
    print "Wickets taken are : ",wickets

print "Test.__do__ :",Match.__doc__
print "Test.__name__ : ",Match.__name__
print "Test.__module__ : ",Match.__module__
print "Test.__bases__ : ",Match.__bases__
print "Test.__dict__ : ",Match.__dict__

'''
SOLUTIONS : This is the output -

Runs scored are :  281
Wickets taken are :  5
Test.__do__ : Runs and Wickets
Test.__name__ :  Match
Test.__module__ :  __main__
Test.__bases__ :  ()
Test.__dict__ :  {'__module__': '__main__', 'runs': 281, '__doc__': 'Runs and Wickets', '__init__': <function __init__ at 0x0398BA70>, 'wickets': 5}
'''
