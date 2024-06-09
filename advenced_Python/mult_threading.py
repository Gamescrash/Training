import time
import threading

def calc_square(numbers):
    result = []
    for number in numbers:
        result.append(number*number)
    return result

def calc_cube(numbers):
    result = []
    for number in numbers:
        result.append(number*number*number)
    return result


array = range(1,100000)

t = time.time()

t1 = threading.Thread(target=calc_square, args=(array,))
t2 = threading.Thread(target=calc_cube, args=(array,))

t1.start()
t2.start()

t1.join()
t2.join()

print ("done in: ", (time.time()-t)*1000)