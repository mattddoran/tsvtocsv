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
    config = {
        'user': '15cfee',
        'password': 'Rrevolution@1',
        'host': '127.0.0.1',
        'database': 'MYDB2',
        'raise_on_warnings': True
    }

    cnx = mysql.connector.connect(user = '15cfee',password = 'Rrevolution@1',host = '127.0.0.1',database='TestingSamePort')

    # cursor = cnx.cursor()
    #
    # query = ("SELECT * "
    #          "FROM EMPLOYEE "
    #          "WHERE employee.Super_ssn IS NOT NULL;")
    #
    # cursor.execute(query)
    #
    # for (Fname, Minit, Lname, Ssn, Bdate, Address, Sex, Salary, Super_ssn, Dno) in cursor:
    #     print("{}, {}".format(Fname, Lname))
    #
    # cursor.close()

    cnx.close()

if __name__ == '__main__':
    # run()
    coolBreeze()
    var = Question("Qusetion1",{2,3,4})
    queryTest()
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