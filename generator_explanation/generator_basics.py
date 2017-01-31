import code

def make_counter(x):
    while True:
        yield x
        x += 1

def get_upto_number(n):
    return [i for i in range(n)]

def grab_element(listing, start):
    index = start
    while True:
        yield listing[index]
        index += 1

def gen_fib(max):
    a, b = 0, 1          
    while a < max:
        yield a          
        a, b = b, a + b  

def fib(n):
    if n == 0:
        return 1
    if n == 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)
    
#listing = get_upto_number(100)
#generator = make_counter(0)

#[i for i in range(10000000000000)]

#for _ in range(100000000000000):
#    next(generator)
    

def read_file(filename):
    thing = []
    with open(filename,"r") as f:
        for i in f.read().split("\n"):
            thing.append(i)
    return thing

def gen_read_file(filename):
    with open(filename,"r") as f:
        while f.readable():
            yield f.readline()
    
thing = read_file("thing.txt")
for i in thing:
    if int(i) < 50:
        print("whatever")
    else:
        continue

other_thing = gen_read_file("thing.txt")
while other_thing:
    tmp = next(other_thing)
    if int(i) < 50:
        print("whatever")
    else:
        continue
    
