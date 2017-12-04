from Q1 import Q1
from Q2 import Q2
from Q3 import Q3
from Q4 import Q4
from Q5 import Q5
# acts as a facade
class Organizer(object):

    def __init__(self):
        # fill the list with the different question numbers
        a = []
        a.append(Q1("query1.csv"))
        a.append(Q2("query2.csv"))
        a.append(Q3("query3.csv"))
        a.append(Q4("query4.csv"))
        a.append(Q5("query51.csv","query5_2.csv"))
        self.a = a

    def runQ(self,qNumber):
        # switch the number to an index
        qNumber -= 1
        #prevent out of bounds exception
        if (qNumber < len(self.a) and qNumber >= 0):
            self.a[qNumber].query()
            self.a[qNumber].visualize()
            return
        print "That question number does not exsist"


#Should take care of the user choosing the question
# return question number or -1 for exit
def menu():
    name = raw_input("Either type the question number you want to run (1-5) or -1 for exit: ")
    # while not (type(name) == int):
    #     name = raw_input("Not an integer: ")
    return int(name)


if __name__ == '__main__':
    state = menu()
    while not(state == -1):
        organizer = Organizer()
        organizer.runQ(state)
        state = menu()




