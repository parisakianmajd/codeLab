import time
import multiprocessing

def calc_square(numbers):
    print "calculate square numbers"
    for n in numbers:
        time.sleep(5)
        print 'square:',n*n

def calc_cube(numbers):
    print "calculate cube of numbers"
    for n in numbers:
        time.sleep(5)
        print 'cube:',n*n*n

if __name__ == "__main__":
    arr = [2,3,8]
    p1 = multiprocessing.Process(target=calc_square, args=(arr,))
    p2 = multiprocessing.Process(target=calc_cube, args=(arr,))

    p1.start()
    p2.start()

    # Waits until the execution of these two process is over
    p1.join()
    p2.join()

    print "Done!"
