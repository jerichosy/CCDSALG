import random
import time

# Input parser
def get_input(min, max, prompt):
    while True:
        try:
            user_input = int(input(prompt))
        except ValueError:
            print("INVALID! Please enter a number.")
            continue
        if user_input < min or user_input > max:
            print(f"Please input a number from {min} to {max}.")
        else:
            break

    return user_input

# Display suffix array
def display_suffix():
    print("Suffix array: ", end='')
    for a, b in arr:
        print(str(b) + " ", end='')
    print("\n")
    width = len(str(len(arr) - 1))
    for a, b in arr:
        print(str(b).rjust(width, ' ') + ':' + a)

string = ""

choice = get_input(1, 2, "\nGenerate random string (1) or Input your own string (2)?: ")

# Option 1: Generate random string of length n specified by the user
if choice == 1:  
    alphabet = ['a', 'c', 'g', 't']
    print("\nRandom alphabet generator")
    n = get_input(0, 1000000, "Input number of n: ")
    for x in range(n):
        string = string + random.choice(alphabet)
# Option 2: Accepts string input from user
if choice == 2:  
    string = input("Input string: ")

#print(string)  WILL LAG

# Creates a unsorted suffix array from "string"
arr = [(string[i:], i) for i in range(len(string))]

#print(arr)

# INSERTION SORT
def insertion_sort():
    start_time = time.time()

    for i in range (len(arr)):
        key = arr[i]
        j = i-1

        while j >= 0 and arr[j] > key:
            arr[j+1] = arr[j]
            j = j-1
        
        arr[j+1] = key

    end_time = time.time()
    print(f"\nTime (Insertion Sort): {round((end_time - start_time) * 1000)}ms\n")

# Used in quick sort function
def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1
    j = low
    while j <= high - 1:
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
        j += 1
    arr[i+1], arr[high] = arr[high], arr[i+1]
    return (i+1)

# QUICK SORT
def quick_sort(arr, low, high):
    if (low < high):
        pi = partition(arr, low, high)
        quick_sort(arr, low, pi-1)
        quick_sort(arr, pi+1, high)


# Asks the user to pick what sorting algorithm to use
choice = get_input(1, 2, "Sort using Insertion sort (1) or Quick Sort (2)?: ")
if choice == 1:
    insertion_sort()
if choice == 2:
    start_time = time.time()
    quick_sort(arr, 0, len(arr)-1)
    end_time = time.time()
    print(f"\nTime (Quick Sort): {round((end_time - start_time) * 1000)}ms\n")


#print(arr)

# Output the (sorted) suffix array
if len(arr) > 77:
    print("There are a lot of suffixes. Do you still want to display them?")
    choice = get_input(1, 2, "    Yes (1)  No (2)?: ")
    if choice == 1:
        print()
        display_suffix()
    else:
        exit()
else:
    display_suffix()
