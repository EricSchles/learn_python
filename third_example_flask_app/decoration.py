# This syntax was stolen from: http://python-3-patterns-idioms-test.readthedocs.io/en/latest/PythonDecorators.html#using-functions-as-decorators
import time
def timeit(func):
    def func_wrapper(*args,**kwargs):
        start = time.time()
        result = func(*args,**kwargs)
        print("time it took:",time.time() - start)
        return result
    return func_wrapper 

@timeit
def average(list_of_values):
    return sum(list_of_values)/float(len(list_of_values))

if __name__ == '__main__':
    for i in range(5,100,5):
        print( average(list(range(i))))
