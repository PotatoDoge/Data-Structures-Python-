from random import randint
import timeit

def bubble_sort(num_array):
    print(num_array)
    tic = timeit.default_timer()
    for i in range(len(num_array)):
        for n in range(0,len(num_array)-i-1):
            curr = num_array[n]
            if num_array[n] > num_array[n+1]:
                num_array[n] = num_array[n+1]
                num_array[n+1] = curr

    toc = timeit.default_timer()
    tt = toc-tic
    print(num_array)
    print(str(tt))

def get_nums(max):
    n = []
    for i in range(0,max):
        n.append(randint(0,1000))
    return n

if __name__ == '__main__':
    test = get_nums(25)
    bubble_sort(test)
    print("Done!")
