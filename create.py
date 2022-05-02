import sys


def readinput():
    inputList = []
    num = 0
    while num < 5:
        data = input("Enter an integer: ")
        # store input as a integer
        inputList.append(int(data))
        num = num + 1
    return inputList


def printsortedlist(sortlist):
    print("Sorted List")
    for value in sortlist:
        print(value)


def sort(inputlist):
    print("Sorting now ...")
    length = len(inputlist)
    for i in range(length-1):
        for j in range(0, length-i-1):
            if inputlist[j] > inputlist[j+1]:
                inputlist[j], inputlist[j+1] = inputlist[j+1], inputlist[j]
    return inputlist

# read input list
inputlist = readinput()
# sort the input
sortlist = sort(inputlist)
#print sorted list
printsortedlist(sortlist)
