from Q1 import Q1
from Q2 import Q2
from Q3 import Q3
from Q4 import Q4
from Q5 import Q5
# acts as a facade
class Organizer(object):

    @staticmethod
    def init():
        a = "nothing going on yet"


    @staticmethod
    def runQ(qNumber):
        if (qNumber == 1):
            Q1.query()
            Q1.visualize("query1.csv")
            return
        if (qNumber == 2):
            Q2.query()
            Q2.process("query2.csv")
            return
        if (qNumber == 3):
            Q3.query()
            Q3.visualize("query3.csv")
            return
        if(qNumber == 4):
            Q4.query()
            Q4.visualize("query4.csv")
            return
        if (qNumber == 5):
            Q5.query()
            return
        print "needs to be implemented"


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
        Organizer.init()
        Organizer.runQ(state)
        state = menu()




