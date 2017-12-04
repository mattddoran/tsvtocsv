from Q1 import Q1
from Q2 import Q2
from Q3 import Q3
from Q4 import Q4
from Q5 import Q5
# acts as a facade
class Organizer(object):

    def __init__(self):
        a = []
        a.append(Q1("query1.csv"))
        a.append(Q2(2))
        a.append(Q3(3))
        a.append(Q4(4))
        a.append(Q5(5))
        self.a = a

    def runQ(self,qNumber):
        qNumber -= 1
        if (qNumber < 5 and qNumber >= 0):
            self.a[qNumber].visualize()
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




