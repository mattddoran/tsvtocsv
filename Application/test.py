import importlib
import numpy as np
import matplotlib
import matplotlib.pyplot as plt


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

if __name__ == '__main__':
    # run()
    coolBreeze()
    # Fixing random state for reproducibility
    np.random.seed(19680801)

    matplotlib.rcParams['axes.unicode_minus'] = False
    fig, ax = plt.subplots()
    ax.plot(10 * np.random.randn(100), 10 * np.random.randn(100), 'o')
    ax.set_title('Using hyphen instead of Unicode minus')
    plt.show()