import importlib
# import numpy as np
# import matplotlib
# import matplotlib.pyplot as plt
import mysql.connector
from Question import Question

def run():
    m = 0
    while m != 1:    
        p = input('Please choose p: ')
        p = makeInt(p)
        #Some other code
        print(p)
        m = makeInt(input('Enter 1 if you would like to quit: '))

def makeInt(i):
    try:
        i = int(i)
    except ValueError:
        i = input('Incorrect input! Enter your answer: ')
        i = makeInt(i)
    return i

#Some other functions    

def coolBreeze():
    print "coolBreeze"

def queryTest():

    cnx = mysql.connector.connect(user = 'root',password = 'Rrevolution@1',host = '127.0.0.1',database='mydb2')

    cursor = cnx.cursor()
    #
    # query = ("SELECT primaryTitle,originalTitle "
    #          "FROM title "
    #          "WHERE idTitle = 9;")
    query =     ("SELECT primaryTitle,originalTitle "            
                "FROM title;")
                # "WHERE idTitle > 50;")
                # "LIMIT = 100;")

    #cursor.execute()

    cursor.execute(query)


    list = []
    num = 0
    for (isTitle,a) in cursor:
        list.append(isTitle)
        # print isTitle, a
        # print("{}".format(isTitle))
        num += 1
        if(num%100000 == 0):
            print num
    print
    cursor.close()

    cnx.close()

if __name__ == '__main__':
    # run()

    var = Question("Qusetion1",{2,3,4})
    queryTest()
    coolBreeze()
    #var.doSome()
    #var.createImage()
    # Fixing random state for reproducibility
    # np.random.seed(19680801)
    #
    # matplotlib.rcParams['axes.unicode_minus'] = False
    # fig, ax = plt.subplots()
    # ax.plot(10 * np.random.randn(100), 10 * np.random.randn(100), 'o')
    # ax.set_title('Using hyphen instead of Unicode minus')
    # plt.show()