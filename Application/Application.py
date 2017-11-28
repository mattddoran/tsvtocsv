# acts as a facade
class Organizer(object):
    @staticmethod
    def runQ(qNumber):
        print "needs to be implemented"


#Should take care of the user choosing the question
# return question number or -1 for exit
def menu():
    name = raw_input("Either type the question number you want to run (1-5) or -1 for exit: ")
    return int(name)


if __name__ == '__main__':
    state = menu()
    while not(state == -1):
        #Organizer.runQ(3)
        state = menu()




