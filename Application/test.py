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
    print 12

if __name__ == '__main__':
    run()
    coolBreeze()