from time import ctime,sleep

def talk():
    print("Start talk %r" %ctime())
    sleep(2)

def write():
    print("Start write %r" %ctime())
    sleep(3)

if __name__ == '__maim__':
    talk()
    write()
    print("All done %r" %ctime())