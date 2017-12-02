from Q1 import Q1
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
            return
        if (qNumber == 3):
            Q3.query()
            return
        if(qNumber == 4):
            Q4.query()
            return
        if (qNumber == 5):
            Q5.query()
            return
        if (qNumber == 6):
            Q4.visualize("query4.csv")
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




