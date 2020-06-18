# Sort Analyzer Starter

import time

# Define Sort Algorithms Here
#********************************************************************
def bubbleSort(anArray):
    print("Write your Bubble Sort code here...")

def selectionSort(anArray):
    print("Write your Selection Sort code here...")

def insertionSort(anArray):
    print("Write your Insertion Sort code here...")

#********************************************************************


# Return data from file as an array of integers.
def loadDataArray(fileName):
    temp = []

    # Read file line by line
    fileref = open(fileName, "r")
    for line in fileref:
        line = line.strip() # Clean up line
        temp.append(int(line)) # Add integer to temp list
    
    fileref.close()

    return temp


# Load data files into global variables
randomData = loadDataArray("data-files/random-values.txt")
reversedData = loadDataArray("data-files/reversed-values.txt")
fewUniqueData = loadDataArray("data-files/few-unique-values.txt")
nearlySortedData = loadDataArray("data-files/nearly-sorted-values.txt")


# Main Menu
loop = True
while loop:
    # Print Main Menu
    print("Main Menu")
    print("1: Bubble Sort Random Data")
    print("2: Bubble Sort Reversed Data")
    print("3: Bubble Sort Few Unique Data")
    print("4: Bubble Sort Nearly Sorted Data")
    print("5: Selection Sort Random Data")
    print("6: Selection Sort Reversed Data")
    print("7: Selection Sort Few Unique Data")
    print("8: Selection Sort Nearly Sorted Data")
    print("9: Insertion Sort Random Data")
    print("10: Insertion Sort Reversed Data")
    print("11: Insertion Sort Few Unique Data")
    print("12: Insertion Sort Nearly Sorted Data")
    print("13: Exit")
    selection = input("Enter menu selection (1-13): ")

    # Process selection
    if (selection == "1"):
        print("Bubble Sort Random Data")
        arrayCopy = randomData[:] # Make a copy to preserve original list
        startTime = time.time()
        bubbleSort(arrayCopy)
        endTime = time.time()
        print("--- %s seconds ---" % (endTime - startTime))
    elif (selection == "2"):
        print("Bubble Sort Reversed Data")
        arrayCopy = reversedData[:] # Make a copy to preserve original list
        startTime = time.time()
        bubbleSort(arrayCopy)
        endTime = time.time()
        print("--- %s seconds ---" % (endTime - startTime))
    elif (selection == "3"):
        print("Bubble Sort Few Unique Data")
        arrayCopy = fewUniqueData[:] # Make a copy to preserve original list
        startTime = time.time()
        bubbleSort(arrayCopy)
        endTime = time.time()
        print("--- %s seconds ---" % (endTime - startTime))
    elif (selection == "4"):
        print("Bubble Sort Nearly Sorted Data")
        arrayCopy = nearlySortedData[:] # Make a copy to preserve original list
        startTime = time.time()
        bubbleSort(arrayCopy)
        endTime = time.time()
        print("--- %s seconds ---" % (endTime - startTime))
    elif (selection == "5"):
        print("Selection Sort Random Data")
        arrayCopy = randomData[:] # Make a copy to preserve original list
        startTime = time.time()
        selectionSort(arrayCopy)
        endTime = time.time()
        print("--- %s seconds ---" % (endTime - startTime))
    elif (selection == "6"):
        print("Selection Sort Reversed Data")
        arrayCopy = reversedData[:] # Make a copy to preserve original list
        startTime = time.time()
        selectionSort(arrayCopy)
        endTime = time.time()
        print("--- %s seconds ---" % (endTime - startTime))
    elif (selection == "7"):
        print("Selection Sort Few Unique Data")
        arrayCopy = fewUniqueData[:] # Make a copy to preserve original list
        startTime = time.time()
        selectionSort(arrayCopy)
        endTime = time.time()
        print("--- %s seconds ---" % (endTime - startTime))
    elif (selection == "8"):
        print("Selection Sort Nearly Sorted Data")
        arrayCopy = nearlySortedData[:] # Make a copy to preserve original list
        startTime = time.time()
        selectionSort(arrayCopy)
        endTime = time.time()
        print("--- %s seconds ---" % (endTime - startTime))
    elif (selection == "9"):
        print("Insertion Sort Random Data")
        arrayCopy = randomData[:] # Make a copy to preserve original list
        startTime = time.time()
        insertionSort(arrayCopy)
        endTime = time.time()
        print("--- %s seconds ---" % (endTime - startTime))
    elif (selection == "10"):
        print("Insertion Sort Reversed Data")
        arrayCopy = reversedData[:] # Make a copy to preserve original list
        startTime = time.time()
        insertionSort(arrayCopy)
        endTime = time.time()
        print("--- %s seconds ---" % (endTime - startTime))
    elif (selection == "11"):
        print("Insertion Sort Few Unique Data")
        arrayCopy = fewUniqueData[:] # Make a copy to preserve original list
        startTime = time.time()
        insertionSort(arrayCopy)
        endTime = time.time()
        print("--- %s seconds ---" % (endTime - startTime))
    elif (selection == "12"):
        print("Insertion Sort Nearly Sorted Data")
        arrayCopy = nearlySortedData[:] # Make a copy to preserve original list
        startTime = time.time()
        insertionSort(arrayCopy)
        endTime = time.time()
        print("--- %s seconds ---" % (endTime - startTime))
    elif (selection == "13"):
        loop = False
# end while loop
print("goodbye")
