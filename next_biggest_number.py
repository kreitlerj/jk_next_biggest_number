#!/usr/bin/python3
import sys

def main():
    next_biggest_number(sys.argv[1])


def next_biggest_number(number):
    #TODO: Implement me!
    #convert the number to an array
    arr = [int(x) for x in str(number)]

    #store the length of the array
    n = len(arr)

    #iterate through the array starting from the right
    #try to find the the first digit is greater than the next digit going right to left
    for i in range(n-1, -1, -1):
        if arr[i] > arr[i-1]:
            break
            
    #if you iterrate through the whole array and end up at the first digit 
    #without finding a digit less than the one to the right, return -1
    if i==0:
        return -1
    
    #set the value of the digit in position i-1
    d = arr[i-1]
    #create a variable to store the smallest digit position right of the i-1 position
    smallest = i
    
    #iterrate through the digits right of "d" to find the smallest digit greater than "d"
    for j in range(i, n):
        if arr[j] > d and arr[j] < arr[smallest]:
            smallest = j
    
    #swap "d" with the next greatest digit right of "d"
    arr[i-1], arr[smallest] = arr[smallest], arr[i-1]
    
    #split the array based on the i position
    first, second = arr[:i], arr[i:]
    
    #sort the digits right of "d"
    second = sorted(second)
    
    #combine the two arrays together into on array
    final_arr = first
    for digit in second:
        final_arr.append(digit)
    
    #create the final number
    final_number = ''.join(map(str,final_arr))
    
    return int(final_number)

if __name__ == "__main__":
    main()

