from random import randint

"""
Method that sorts the list
"""
def selection_sort(arr):
    for x in range(len(arr)):
        i = x
        for n in range(i,len(arr)):
            if n == len(arr)-1:
                s = arr[i]
                arr[i] = arr[n]
                arr[n] = s
            else:
                if arr[n]<arr[n+1]:
                    s = arr[n]
                    arr[n] = arr[n+1]
                    arr[n+1] = s
    return arr

'''
Method that returns a list of max random numbers
'''
def get_nums(max):
    n = []
    for i in range(0,max):
        n.append(randint(0,1000))
    return n

if __name__ == '__main__':
    a = get_nums(25)
    print("Before:\n",a)
    print("After:\n",selection_sort(a))
