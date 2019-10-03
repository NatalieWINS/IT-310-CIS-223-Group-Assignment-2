import time
from random import *


class frac():
    def __init__(self,dem,num):
        self.dem = dem
        self.num = num

    def returnDec(self):
        return self.num/self.dem


def generateList(length):
    intList = []
    for i in range(0, length):
        intList.append(randint(1, 1000))
    return intList


def generateFracList(length):
    fracList = []
    for i in range(0,length):
        tempFrac = frac(randint(1, 1000), randint(1, 1000))
        fracList.append(tempFrac.returnDec())
    return fracList


def selectionSort(unsort):
    # This checks every item in the list, bar the last one since it will already be sorted
    for i in range(len(unsort)-1):
        lowest = i  # Default the lowest value to be the current index
        for k in range(i, len(unsort)):  # Starting at the current 'i' index, compare 'lowest' with each item in unsort
            if unsort[k] < unsort[lowest]:
                lowest = k # 'lowest' is reassigned every time a new lowest number is found
        # Swap the lowest number with the current 'i' index
        temp = unsort[i]
        unsort[i] = unsort[lowest]
        unsort[lowest] = temp


def insertionSort(unsort):
    for i in range(len(unsort)): # This will check through each item in the array
        j = i  # Assign the next index as the pointer
        # This will loop until j hits 0 or j becomes greater than the value behind itself
        while j > 0 and unsort[j] < unsort[j-1]:
            # The next three lines swap index j with the value behind itself
            temp = unsort[j]
            unsort[j] = unsort[j-1]
            unsort[j-1] = temp
            j -= 1  # Iterate i by one so that we keep track of the number we are working with


def bubbleSort(unsort):
    for i in range(len(unsort)):  # For each item in unsorted...
        for k in range(i, len(unsort)-1):  # Loop through the list until every number is sorted
            if unsort[k+1] < unsort[k]:  # If the value ahead of 'k' is less than itself: swap them
                temp = unsort[k]
                unsort[k] = unsort[k+1]
                unsort[k+1] = temp


def mainFun():
    selectionTimesInt = []
    insertionTimesInt = []
    bubbleTimesInt = []

    selectionTimesFrac = []
    insertionTimesFrac = []
    bubbleTimesFrac = []

    for i in range(0, 10):
        intList = generateList(1000+1000*i)
        fracList = generateFracList(1000+1000*i)

        # Selection Sort with Integer List
        selectionTime1 = time.time()
        selectionSort(intList)
        selectionTime2 = time.time()
        selectionTimesInt.append(selectionTime2 - selectionTime1)

        # Selection Sort with Fraction List
        selectionTime1 = time.time()
        selectionSort(fracList)
        selectionTime2 = time.time()
        selectionTimesFrac.append(selectionTime2 - selectionTime1)

        # Insertion Sort with Integer List
        InsertionTime1 = time.time()
        insertionSort(intList)
        InsertionTime2 = time.time()
        insertionTimesInt.append(InsertionTime2 - InsertionTime1)

        # Insertion Sort with Fraction List
        InsertionTime1 = time.time()
        insertionSort(fracList)
        InsertionTime2 = time.time()
        insertionTimesFrac.append(InsertionTime2 - InsertionTime1)

        # Bubble Sort with Integer List
        BubbleTime1 = time.time()
        insertionSort(intList)
        BubbleTime2 = time.time()
        bubbleTimesInt.append(BubbleTime2 - BubbleTime1)

        # Bubble Sort with Fraction List
        BubbleTime1 = time.time()
        insertionSort(fracList)
        BubbleTime2 = time.time()
        bubbleTimesFrac.append(BubbleTime2 - BubbleTime1)

    # Selection Times
    print("Selection Sort:")
    print("Int List Time: " + str(sum(selectionTimesInt) / len(selectionTimesInt)))
    print("Frac List Time: " + str(sum(selectionTimesFrac) / len(selectionTimesFrac)))

    # Insertion Times
    print("Selection Sort:")
    print("Int List Time: " + str(sum(insertionTimesInt) / len(insertionTimesInt)))
    print("Frac List Time: " + str(sum(insertionTimesFrac) / len(insertionTimesFrac)))

    # Bubble Times
    print("Selection Sort:")
    print("Int List Time: " + str(sum(bubbleTimesInt) / len(bubbleTimesInt)))
    print("Frac List Time: " + str(sum(bubbleTimesFrac) / len(bubbleTimesFrac)))
mainFun()